import matplotlib.pyplot as plt
from diode_experiment import DiodeExperiment

Experiment_1 = DiodeExperiment()
measurements = Experiment_1.scan(450, 1023)

plt.scatter(measurements[0], measurements[1])
plt.ylabel("Current [A]")
plt.xlabel("Voltage [V]")
plt.show()
