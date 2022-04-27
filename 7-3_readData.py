import matplotlib.pyplot as plt
import numpy as np

with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype = int)

timeStep = tmp[0]
voltStep = tmp[1]

nMeasurements = len(data_array)
allTime = timeStep * nMeasurements

minVoltage = 0
maxVoltage = data_array.max() / 256 * 3.3

data_arrayGr = data_array / 256 * 3.3
data_timeGr = nMeasurements * [0]

for i in range (0, nMeasurements):
    data_timeGr[i] = timeStep * i 

fig, ax = plt.subplots(figsize = (16, 10), dpi = 400)

ax.set_xlabel('time, s', fontsize = 15, color = 'blue')
ax.set_ylabel('Voltage, V', fontsize = 15, color = 'blue')

ax.grid(which='major',
        color = 'orange', 
        linewidth = 1)

ax.grid(which='minor', 
        color = 'black',
        ls = ':')

ax.set_title('Процесс зарядки и разрядки конденсатора в RC-цепочке',
             loc = 'center',
             fontsize = 15,
             color = 'white',
             backgroundcolor = 'black')

plt.xlim([0, allTime + 10 * timeStep])
plt.ylim([0, maxVoltage])

nCharge = 0
nDisCharge = 0

maxData = data_array.max()

wasMax = 0

while (data_array[nCharge] < maxData):
    nCharge += 1

chargeTime = timeStep * nCharge
dischargeTime = allTime - chargeTime

#plt.text (6.1, 2.6, 'Charge time: %.2g \nDischarge time: %.2g', chargeTime , dischargeTime, family='monospace', color='#11aa55', weight='demibold')
plt.text (6.1, 2.6, f'Charge time: {chargeTime:.2f} \nDischarge time: {dischargeTime:.2f}', family='monospace', color='#11aa55', weight='demibold')
ax.plot(data_timeGr, data_arrayGr,
        color = 'darkmagenta', 
        linewidth = 1, 
        marker = '^',
        markersize = 3)

fig.savefig("test.svg")