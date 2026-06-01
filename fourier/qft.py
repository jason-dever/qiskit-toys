import matplotlib.pyplot as plt
from qiskit.visualization import plot_state_city, plot_state_qsphere, plot_bloch_multivector
import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from qiskit.quantum_info import Statevector

# n-Qubit Quantum Fourier Transform circuit builder.
# Qubit 0 in the circuit is intended to be the least 
# significant qubit in the input.
def qft_builder(n):
    angles = [2*np.pi/(2**k) for k in range(2, n+1)]
    qc = QuantumCircuit(n)

    # Working on qubits in order of most to least significant
    for k in range(n-1, -1, -1):
        qc.h(k)
        for (idx, angle) in enumerate(angles[:k]):
            control = k-idx-1
            qc.cp(angle, control, k)
            
    # Now we have the transformed amplitudes; we need only reverse the order of the output.
    for k in range(n//2):
        qc.swap(k, n-k-1)
    return qc

n = 4
qft = qft_builder(n)
# state = Statevector.from_instruction(qft)
# plot_state_city(state)
# plt.show()

qft.draw("mpl", filename=f"fourier/images/qft_{n}.png")