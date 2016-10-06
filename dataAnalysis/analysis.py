import matplotlib.pyplot as plt
import numpy as np


with open("brTime_10/brTime_10_35.txt") as f:
    data = f.read()

data = data.split('\n')
del data[-1]  # remove last line (unwanted \n)


#x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[0] for row in data]

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("Packet broadcast time over network lifespan")
ax1.set_xlabel('Packet Sequence Number')
ax1.set_ylabel('Broadcast Time (s)')

axes = plt.gca()
#axes.set_xlim([xmin,xmax])
#axes.set_ylim([0,10])

#ax1.plot(x,y, c='r', label='the data')
ax1.plot(y, 'bo', y, 'r')

leg = ax1.legend()

plt.show()

