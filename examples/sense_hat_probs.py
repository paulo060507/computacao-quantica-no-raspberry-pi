# Visualiza probabilidades de um circuito simples no Sense HAT (LED 8x8).
# Requer: sudo apt install sense-hat  (ou pip install sense-hat) e enable I2C.
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
try:
    from sense_hat import SenseHat
except Exception as e:
    raise SystemExit("Sense HAT não disponível: " + str(e))

# Circuito: |0> --H---> |+>
qc = QuantumCircuit(1)
qc.h(0)
sv = Statevector.from_instruction(qc)
probs = sv.probabilities_dict()

# Mapeia probabilidade de |0> e |1> para colunas no LED
sense = SenseHat()
sense.clear()
p0 = probs.get('0', 0.0)
p1 = probs.get('1', 0.0)

def col(val):
    # intensidade 0-255
    v = max(0, min(255, int(val * 255)))
    return [v, v, 0]  # amarelo proporcional

for y in range(8):
    sense.set_pixel(2, y, col(p0))
    sense.set_pixel(5, y, col(p1))

print(f"P(|0>)={p0:.3f}  P(|1>)={p1:.3f}")
