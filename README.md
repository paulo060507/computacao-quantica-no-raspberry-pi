# Computação Quântica no Raspberry Pi (Open Source)

**Tema provocante:** trazer conceitos e **simulações quânticas** para a borda, usando Raspberry Pi.
A proposta aqui é prática, didática e totalmente open source.

## O que tem aqui
- Tutoriais de setup (Qiskit & PennyLane com simuladores clássicos).
- Exemplos executáveis no Pi: estados de Bell, teleporte quântico (simulado), VQE simples.
- Scripts prontos e *notebooks* leves.

## Requisitos
- Raspberry Pi 4/5 com Python 3.11+
- Recomenda-se swap habilitado e *virtualenv*.

## Instalação rápida
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Exemplos
- `examples/hello_bell.py` – gera e mede um par emaranhado (simulado).
- `examples/teleport_sim.py` – teleporte quântico passo a passo (simulado).
- `examples/vqe_min.py` – VQE mínimo com ansatz curta.

## Observação importante
Este repositório usa **simuladores clássicos**. É ideal para aprender conceitos e prototipar, sem depender de hardware quântico.
Quando precisar, dá para conectar a *backends* remotos (ex.: provedores públicos) – configure as credenciais localmente.

## Licença
MIT

## Ambiente Qiskit 1.x
Recomenda-se criar um **ambiente novo** (você evita conflitos ao migrar de versões anteriores):
```bash
python -m venv .venv && source .venv/bin/activate
pip install --upgrade pip
pip install qiskit
```
> Dica: Qiskit Aer e alguns extras podem compilar dependências. No Pi, seja paciente e garanta swap habilitado.

## Visualização no Sense HAT (opcional)
Se tiver um **Sense HAT**, instale a lib `sense-hat` e rode `examples/sense_hat_probs.py` para visualizar probabilidades.
