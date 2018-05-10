#!/usr/bin/env python
from pandas import DataFrame, Series, concat, read_csv, read_hdf
import os
from os.path import basename
from os.path import splitext
import time
import sys

# possible packet states
PKT_RECEIVING = 0
PKT_RECEIVED = 1
PKT_CORRUPTED = 2
PKT_GENERATED = 3
PKT_QUEUE_DROPPED = 4

# name of fields
FIELDS = ['lambda', 'dst']


def is_number(string):
    """ Determine whether a string contains a parsable number
    """
    try:
        float(string)
        return True
    except:
        return False


def get_data_files(folder, suffix=".csv"):
    """ Gets the list of files with a certain prefix and suffix in a folder
    """
    files_list = []
    for f in os.listdir(folder):
        if f.endswith(suffix):
            files_list.append(f)
    return files_list


def get_params(filename, fields, fields_index):
    """ Splits the name of an output file by _ and extracts the values of
    simulation parameters
    """
    d = DataFrame()
    p = splitext(basename(filename))[0].split("_")
    for f in fields_index:
        v = p[f]
        if is_number(v):
            s = Series([float(v)])
        else:
            s = Series([v])
        d.loc[:, fields[f]] = s
    return d


def offered_load(l, n_nodes, packet_size=(1460+32)/2):
    """ Total offered load in Mbps
    """
    return l * n_nodes * packet_size * 8 / 1024 / 1024


def stats(x, sim_time):
    """ Computes throughput, collision rate, and drop rate for a specific node
    and a specific simulation
    """
    inc_pkts = x.loc[(x.event == PKT_RECEIVED) | (x.event == PKT_CORRUPTED)]
    rcv_pkts = x.loc[x.event == PKT_RECEIVED]
    gen_pkts = x.loc[x.event == PKT_GENERATED]
    drp_pkts = x.loc[x.event == PKT_QUEUE_DROPPED]
    return DataFrame({'tr': [rcv_pkts['size'].sum() * 8 / sim_time / 1024**2],
                      'cr': [1-float(len(rcv_pkts))/len(inc_pkts)],
                      'dr': [float(len(drp_pkts))/len(gen_pkts)]})


def compute_stats(d, sim_time):
    """ Computes throughput, collision rate, and drop rate for all nodes and
    simulation runs
    """
    grouped = d.groupby(FIELDS)
    thr = grouped.apply(lambda x: stats(x, sim_time))
    return thr.reset_index(level=2, drop=True).reset_index()


def replicate_rows(d, fields, n):
    """ Generates a data frame replicating the row of a single-entry dataframe
    n times
    """
    df = DataFrame()
    for f in fields:
        df = concat([df, DataFrame({f: [d[f][0]]*n})], axis=1)
    return df


def event(ev):
    return DataFrame({'ev': [ev], 't': [time.time()]})

res_folder = "./"

if len(sys.argv) != 1:
    res_folder = sys.argv[1]

aggregated_file = "%s/alld.h5" % res_folder

if not os.path.isfile(aggregated_file):
    # if there is no aggregated file, load all csv files into a single dataframe
    alld = DataFrame()
    data_files = get_data_files(res_folder, ".csv")
    for f in data_files:
        full_path = "%s/%s" % (res_folder, f)
        print(f)
        # get the simulation parameters from the file name
        pars = get_params(full_path, ['prefix', 'lambda', 'seed'], [1, 2])
        d = read_csv(full_path)
        # replicate the parameters n times, with n being the number of records
        # in the csv file
        ext_pars = replicate_rows(pars, ['lambda', 'seed'], len(d))
        # join the csv data file with the parameters
        d = d.join(ext_pars)
        alld = concat([alld, d])

    # store the full database to a single file
    ######### alld.to_hdf(aggregated_file, 'table')
else:
    # otherwise simply load the aggregated file
    alld = read_hdf(aggregated_file, 'table')

# get simulation duration and number of nodes
sim_time = alld.time.max()
n_nodes = len(alld.src.unique())

# compute the statistics
st = compute_stats(alld, sim_time)

st.to_csv("tmep.csv")
print "jkdsaj"