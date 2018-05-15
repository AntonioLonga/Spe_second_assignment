
import os
import matplotlib.pyplot as plt
import json

a="[[8.193, 22.631], [10.007, 15.253], [23.093, 22.907], [0.26, 23.356], [10.322, 24.609], [19.605, 4.392], [14.732, 17.132], [20.345, 2.116], [1.806, 19.106], [21.5, 13.835]]"
t=json.loads(a)
x=[]
y=[]
for a in range(0, 10):
    x.append(t[a][0])
    y.append(t[a][1])


plt.plot(x, y, 'ro')
plt.axis([0, 25, 0, 25])
plt.show()


fig, ax = plt.subplots()
ax.plot(x[0],y[0],"ro",color="black")
ax.plot(x[1],y[1],"ro",color="red")
plt.axis([0, 25, 0, 25])
circle0 = plt.Circle((x[0], y[0]), 10, color="black", linewidth=3,fill=False)
circle1 = plt.Circle((x[1], y[1]), 10, color='red', linewidth=3,fill=False)
circle2 = plt.Circle((x[2], y[2]), 10, color='blue')
circle3 = plt.Circle((x[3], y[3]), 10, color='blue')
circle4 = plt.Circle((x[4], y[4]), 10, color='blue')
ax.add_artist(circle0)
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)
ax.add_artist(circle4)

for x in range(0, 30):
    t="main.py -c config.json -s simulation -r "+str(x)
    os.system(t)
    print(x)
