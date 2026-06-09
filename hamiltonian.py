import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import Statevector
from qiskit.primitives import StatevectorSampler
from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector

# Hamiltonian is X tensor Y tensor Z
def evolution(dt):
    qc = QuantumCircuit(4, 1)
    qc.prepare_state([1/np.sqrt(2), 1j/np.sqrt(2)], 1)

    qc.h(0)
    qc.sdg(1)
    qc.h(1)

    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(2, 3)
    qc.rz(2*dt, 3)
    qc.cx(2, 3)
    qc.cx(1, 3)
    qc.cx(0, 3)

    qc.h(0)
    qc.h(1)
    qc.s(1)

    qc.measure(0, 0)
    return qc

# state = Statevector.from_instruction(qc)
# plot_bloch_multivector(state)
# plt.show()

print(evolution(np.pi))
num_shots = 64
probs_of_zero = []
x_axis = np.linspace(0, 2*np.pi, 48)
for dt in x_axis:
    qc = evolution(dt)

    sampler = StatevectorSampler()
    result = sampler.run([qc], shots=num_shots).result()
    counts = result[0].data.c.get_counts()

    prob = int(counts.get("0", 0))/num_shots
    # print(prob)
    probs_of_zero.append(prob)

ideal = (lambda x: np.cos(x)**2)(x_axis)
plt.plot(x_axis, probs_of_zero, "bo", label="prob. of measuring 0")
plt.plot(x_axis, ideal, "r-", label="cos^2(dt)")
plt.xlabel("dt")
plt.legend(loc="upper right")
plt.show()