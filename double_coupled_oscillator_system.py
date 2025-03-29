import os
import numpy as np
import argparse

class CoupledOscillators:
    def __init__(self, mass, k, k_coupling, x1_0, v1_0, x2_0, v2_0):
        """Inicializa el sistema de osciladores acoplados."""
        self.mass = mass
        self.k = k  # Constante del resorte externo
        self.k_coupling = k_coupling  # Constante del resorte de acoplamiento
        self.state = np.array([x1_0, v1_0, x2_0, v2_0])
    
    def equations_of_motion(self, state, t):
        """Ecuaciones de movimiento del sistema."""
        x1, v1, x2, v2 = state
        dx1_dt = v1
        dv1_dt = (-self.k * x1 - self.k_coupling * (x1 - x2)) / self.mass
        dx2_dt = v2
        dv2_dt = (-self.k * x2 - self.k_coupling * (x2 - x1)) / self.mass
        return np.array([dx1_dt, dv1_dt, dx2_dt, dv2_dt])


def runge_kutta_step(system, state, t, dt):
    """Realiza un paso de integración usando Runge-Kutta de 4to orden."""
    k1 = dt * system.equations_of_motion(state, t)
    k2 = dt * system.equations_of_motion(state + 0.5 * k1, t + 0.5 * dt)
    k3 = dt * system.equations_of_motion(state + 0.5 * k2, t + 0.5 * dt)
    k4 = dt * system.equations_of_motion(state + k3, t + dt)
    return state + (k1 + 2*k2 + 2*k3 + k4) / 6


def simulate_coupled_oscillators(system, t_max, dt, filename="coupled_oscillators_data"):
    """Ejecuta la simulación del sistema de osciladores acoplados y guarda los datos en un archivo."""
    os.makedirs("data", exist_ok=True)
    filepath = f"data/{filename}.dat"
    
    steps = int(t_max / dt)
    state = system.state.copy()
    
    with open(filepath, "w") as file:
        file.write("# t x1 v1 x2 v2 E_kin E_pot E_tot\n")
        time = 0.0
        for _ in range(steps):
            x1, v1, x2, v2 = state
            E_kin = 0.5 * system.mass * (v1**2 + v2**2)
            E_pot = 0.5 * system.k * (x1**2 + x2**2) + 0.5 * system.k_coupling * (x1 - x2)**2
            E_tot = E_kin + E_pot
            
            file.write(f"{time:.5f} {x1:.5f} {v1:.5f} {x2:.5f} {v2:.5f} {E_kin:.5f} {E_pot:.5f} {E_tot:.5f}\n")
            
            state = runge_kutta_step(system, state, time, dt)
            time += dt

    print(f"Simulación completada. Datos guardados en {filepath}")


def main(mass=1.0, k=1.0, k_coupling=0.5, x1_0=0.1, v1_0=0.0, x2_0=-0.1, v2_0=0.0, dt=0.01, t_max=10.0, filename="test_coupled_oscillators"):
    system = CoupledOscillators(mass, k, k_coupling, x1_0, v1_0, x2_0, v2_0)
    simulate_coupled_oscillators(system, t_max, dt, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulador de osciladores acoplados usando Runge-Kutta de 4to orden.")
    parser.add_argument("--mass", type=float, default=1.0, help="Masa de cada oscilador (kg)")
    parser.add_argument("--k", type=float, default=1.0, help="Constante elástica de los resortes externos (N/m)")
    parser.add_argument("--k_coupling", type=float, default=0.5, help="Constante elástica del resorte de acoplamiento (N/m)")
    parser.add_argument("--x1_0", type=float, default=0.1, help="Posición inicial de m1 (m)")
    parser.add_argument("--v1_0", type=float, default=0.0, help="Velocidad inicial de m1 (m/s)")
    parser.add_argument("--x2_0", type=float, default=-0.1, help="Posición inicial de m2 (m)")
    parser.add_argument("--v2_0", type=float, default=0.0, help="Velocidad inicial de m2 (m/s)")
    parser.add_argument("--dt", type=float, default=0.01, help="Paso de tiempo para la simulación (s)")
    parser.add_argument("--t_max", type=float, default=10.0, help="Tiempo total de simulación (s)")
    parser.add_argument("--filename", type=str, default="test_coupled_oscillators", help="Nombre del archivo de salida")
    
    args = parser.parse_args()
    main(args.mass, args.k, args.k_coupling, args.x1_0, args.v1_0, args.x2_0, args.v2_0, args.dt, args.t_max, args.filename)

