import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit import QuantumCircuit
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit_ibm_runtime.fake_provider import FakeBelemV2
from qiskit.quantum_info import Statevector


service = QiskitRuntimeService()
backend = service.least_busy(simulator=False, operational=True)
# backend = FakeBelemV2()

x = Statevector([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
y = Statevector([1/np.sqrt(2), 1/np.sqrt(2), 0, 0])

qc = QuantumCircuit(4)
# The initial state is q_3 q_2 q_1 q_0 = y_1 y_0 x_1 x_0. This gets mapped to (y plus x) mod 4 tensor x.
# qc.prepare_state(y.tensor(x))
qc.ccx(0, 2, 3)
qc.cx(0, 2)
qc.cx(1, 3)
qc.measure_all()

pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
isa_circuit = pm.run(qc)
isa_circuit.draw("latex", filename="physical_adder.png", idle_wires=False)
qc.draw("latex", filename="adder.png")

# sampler = Sampler(mode=backend)
# sampler.options.default_shots = 256 

# job = sampler.run([isa_circuit])
# print(f"Job ID: {job.job_id()}")

# counts = job.result()[0].data.meas.get_counts()
# plot_histogram(counts)
# plt.show()