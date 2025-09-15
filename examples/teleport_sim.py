# Teleporte quântico (simulado) com Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(3, 3)
# Estado a ser teleportado no qubit 0 (|+>)
qc.h(0)
# Par de Bell entre 1 e 2
qc.h(1); qc.cx(1,2)
# Medidas de Bell no qubit 0 e 1
qc.cx(0,1); qc.h(0)
qc.measure(0,0); qc.measure(1,1)
# Correções condicionais
qc.cx(1,2); qc.cz(0,2)
qc.measure(2,2)

sim = AerSimulator()
result = sim.run(transpile(qc, sim), shots=1024).result()
print("OK, rodou. Veja o circuito com qc.draw() se quiser visualizar.")
