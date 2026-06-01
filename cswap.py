import matplotlib.pyplot as plt
import numpy as np
from qiskit.visualization import plot_histogram
from qiskit.primitives import StatevectorSampler
from qiskit import QuantumCircuit
from qiskit.circuit.library import UnitaryGate
from qiskit.quantum_info import Operator

V_op = Operator(np.array([[(1-1j)/2, (1+1j)/2], 
                          [(1+1j)/2, (1-1j)/2]]))

controlled_V = UnitaryGate(V_op, label="V").control()
controlled_V_dagger = UnitaryGate(V_op.adjoint(), label="Vdg").control()

qc = QuantumCircuit(3)
qc.prepare_state("011")
qc.cx(2, 1)
qc.append(controlled_V, [1, 2])
qc.cx(0, 1)
qc.append(controlled_V_dagger, [1, 2])
qc.cx(0, 1)
qc.append(controlled_V, [0, 2])
qc.cx(2, 1)
qc.measure_all()
qc.draw("latex", filename="cswap.png")

sampler = StatevectorSampler()
result = sampler.run([qc], shots=32).result()
counts = result[0].data.meas.get_counts()
# plot_histogram(counts)
# plt.show()
print(counts)
print(qc)