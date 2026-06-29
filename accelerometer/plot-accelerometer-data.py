import csv
import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

t = []
x = []
y = []
z = []

with open('C:\\code\\github\\hawky06\\microbit\\accelerometer\\microbit_v2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(reader)  # Skip the header row
    for row in reader:
        t.append(float(row[0]))
        x.append(int(row[1]))
        y.append(int(row[2]))
        z.append(int(row[3]))

t = np.array(t)
x = np.array(x) / 1000  # Convert milli-g to m/s²
y = np.array(y) / 1000
z = np.array(z) / 1000

mag = np.sqrt(x**2 + y**2 + z**2)

# time vs magnitude plot
plt.subplot(4, 1, 1)
plt.plot(t, mag)

plt.title("Magnitude")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")

plt.grid()
plt.tight_layout()


# time vs x-axis acceleration plot
plt.subplot(4, 1, 2)
plt.plot(t, x)

plt.title("X-axis")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")

plt.grid()
plt.tight_layout()


# time vs y-axis acceleration plot
plt.subplot(4, 1, 3)
plt.plot(t, y)

plt.title("Y-axis")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")

plt.grid()
plt.tight_layout()


# time vs z-axis acceleration plot
plt.subplot(4, 1, 4)
plt.plot(t, z)

plt.title("Z-axis")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")

plt.grid()
plt.tight_layout()

plt.suptitle("Accelerometer Data from Micro:bit")
plt.show()