# Simulación de Osciladores Acoplados

Este proyecto simula un sistema de dos osciladores armónicos acoplados, resolviendo las ecuaciones de movimiento con el método de Runge-Kutta de 4to orden. Se analizan modos normales, batimiento y resonancia mediante visualizaciones de trayectorias, espacio fase y energía.

## Análisis y Resultados
El notebook de análisis incluye gráficas interactivas y explicaciones detalladas:

- `coupled_oscillators_analysis.ipynb` [![Ver Análisis en Jupyter](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/isaultirado77/coupled-oscillators/blob/main/coupled_oscillators_analysis.ipynb)

## Ejecución de la Simulación

### 1. Valores predefinidos:
```python
mass, k, k_coupling = 1.0, 1.0, 0.5
x1_0, v1_0, x2_0, v2_0 = 0.1, 0.0, -0.1, 0.0
dt, t_max = 0.01, 10.0

system = CoupledOscillators(mass, k, k_coupling, x1_0, v1_0, x2_0, v2_0)
simulate_coupled_oscillators(system, t_max, dt)
```

### 2. Personalización vía terminal:
```bash
python double_coupled_oscillator_system.py \
    --mass 1.0 --k 1.0 --k_coupling 0.5 \
    --x1_0 0.1 --v1_0 0.0 --x2_0 -0.1 --v2_0 0.0 \
    --dt 0.01 --t_max 10.0 --filename osciladores
```

## Requisitos
- Python 3.7+
- Dependencias:
  ```bash
  pip install numpy matplotlib
  ```

