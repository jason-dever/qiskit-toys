import matplotlib.pyplot as plt
import numpy as np
from qiskit.visualization import plot_histogram
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector
from qiskit import QuantumCircuit

x = Statevector([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
# x = Statevector([0, 1, 0, 0])
y = Statevector([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
qc = QuantumCircuit(4)
qc.prepare_state(y.tensor(x))

qc.ccx(0, 2, 3)
qc.cx(0, 2)
qc.cx(1, 3)
qc.measure_all()

sampler = StatevectorSampler()
result = sampler.run([qc], shots=256).result()
counts = result[0].data.meas.get_counts()
print(counts)
print(qc)