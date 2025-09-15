import pennylane as qml
from pennylane import numpy as np

dev = qml.device('default.qubit', wires=2)

@qml.qnode(dev)
def circuit(params):
    qml.RY(params[0], wires=0)
    qml.CNOT(wires=[0,1])
    return qml.expval(qml.PauliZ(0))

def cost(params):
    return circuit(params)

params = np.array([0.1], requires_grad=True)
opt = qml.GradientDescentOptimizer(stepsize=0.1)
for _ in range(50):
    params = opt.step(cost, params)
print("Parâmetro final:", params)
