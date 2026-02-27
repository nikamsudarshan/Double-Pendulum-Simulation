# Chaotic Motion Simulation: Double Pendulum
**Computational Modeling Project for Internship Application**

This repository contains a Python-based computational model of a double pendulum system. The project demonstrates **Chaos Theory**—specifically, how a deterministic system exhibit sensitive dependence on initial conditions.

## 🚀 Demonstration
![Double Pendulum Animation](Untitled-2026-02-27_19_49_47-1.mp4)

---

## 📝 Theoretical Background

### Lagrangian Mechanics
To model the system, we use the **Lagrangian ($L$)**, defined as the difference between the Kinetic Energy ($T$) and Potential Energy ($V$):
$$L = T - V$$

For a double pendulum with masses $m_1, m_2$ and lengths $l_1, l_2$, the state is defined by angles $\theta_1$ and $\theta_2$. The equations of motion are derived using the **Euler-Lagrange Equation**:
$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{\theta}_i} \right) - \frac{\partial L}{\partial \theta_i} = 0$$

### Chaos & Nonlinear Dynamics
Unlike a single pendulum, the double pendulum's motion is **non-linear** and **coupled**. 
- **Deterministic but Unpredictable:** While the laws of motion are deterministic, the system is chaotic. Tiny variations in starting angles lead to exponentially divergent trajectories.
- **Phase Space:** The plots of $(\theta, \omega)$ show that the system does not settle into a simple periodic loop. Instead, it "fills" the phase space in a complex pattern, indicating it never returns to the exact same state twice.

---

## 🛠️ Technical Implementation
- **Numerical Solver:** Utilized `scipy.integrate.odeint` to solve the four coupled first-order ordinary differential equations (ODEs).
- **Visualization:** - **Dynamic Trace:** Tracks the non-repeating path of the lower mass.
  - **Phase Space Mapping:** Real-time plotting of Angular Velocity ($\omega$) vs. Angle ($\theta$) to visualize the system's "Strange Attractor" behavior.

---

## 💻 How to Run Locally

This project is built using Python 3. Follow these steps to set up the environment:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Double-Pendulum-Simulation.git](https://github.com/YOUR_USERNAME/Double-Pendulum-Simulation.git)
   cd Double-Pendulum-Simulation
2. **Install Dependencies:**
   ```bash
   pip install numpy scipy matplotlib
3. **Execute the Simulation:**
   ```bash
   python simulation.py
