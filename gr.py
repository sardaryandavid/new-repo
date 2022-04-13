import matplotlib.pyplot as plt

measured_data = [200, 150, 100, 16, 24, 401]

plt.plot (measured_data)
plt.show ()

measured_data_str = [str (item) for item in measured_data]
print (measured_data, measured_data_str)

with open ("data.txt", "w") as outfile:
    outfile.write ()