
import os





for x in range(0, 309):
    t="main.py -c config.json -s simulation -r "+str(x)
    os.system(t)
    print(x)

