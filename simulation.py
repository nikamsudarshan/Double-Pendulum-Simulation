import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Configuration & Constants ---
G = 9.81      # acceleration due to gravity (m/s^2)
L1, L2 = 1.0, 1.0  # lengths of pendulum arms (m)
M1, M2 = 1.0, 1.0  # masses of pendulums (kg)

def equations(y, t, L1, L2, M1, M2):
    """
    Defines the system of ODEs for the double pendulum.
    y = [theta1, omega1, theta2, omega2]
    """
    t1, w1, t2, w2 = y

    cos_diff = np.cos(t1 - t2)
    sin_diff = np.sin(t1 - t2)

    # Common denominator term for both accelerations
    den = (2*M1 + M2 - M2 * np.cos(2*t1 - 2*t2))

    # Equation for d(omega1)/dt
    dw1dt = (-G * (2*M1 + M2) * np.sin(t1)
             - M2 * G * np.sin(t1 - 2*t2)
             - 2 * sin_diff * M2 * (w2**2 * L2 + w1**2 * L1 * cos_diff)) / (L1 * den)

    # Equation for d(omega2)/dt
    dw2dt = (2 * sin_diff * (w1**2 * L1 * (M1 + M2)
             + G * (M1 + M2) * np.cos(t1)
             + w2**2 * L2 * M2 * cos_diff)) / (L2 * den)

    return [w1, dw1dt, w2, dw2dt]

# --- Initial Conditions & Integration ---
# theta1, omega1, theta2, omega2 (rad, rad/s)
initial_state = [np.pi/2, 0, np.pi/2, 0]
t_stop = 30   # total time (s)
dt = 0.02     # time step
t = np.arange(0, t_stop, dt)

sol = odeint(equations, initial_state, t, args=(L1, L2, M1, M2))

# Extracting coordinates
t1, w1, t2, w2 = sol[:, 0], sol[:, 1], sol[:, 2], sol[:, 3]

# Convert to Cartesian for plotting
x1 = L1 * np.sin(t1)
y1 = -L1 * np.cos(t1)
x2 = x1 + L2 * np.sin(t2)
y2 = y1 - L2 * np.cos(t2)

# --- Visualization ---
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(121, aspect='equal', autoscale_on=False, xlim=(-2, 2), ylim=(-2, 1.5))
ax1.grid()

# Animation elements
line, = ax1.plot([], [], 'o-', lw=2, color='#2c3e50')
trace, = ax1.plot([], [], '-', lw=1, color='#e74c3c', alpha=0.6)
history_x, history_y = [], []

# Phase Space Plot
ax2 = fig.add_subplot(122)
ax2.set_title("Phase Space: $\omega$ vs $\\theta$")
ax2.set_xlabel("Angle (rad)")
ax2.set_ylabel("Angular Velocity (rad/s)")
phase1, = ax2.plot([], [], lw=1, label="Pendulum 1")
phase2, = ax2.plot([], [], lw=1, label="Pendulum 2")
ax2.legend()

def animate(i):
    # Pendulum animation
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)

    # Trace logic
    history_x.append(x2[i])
    history_y.append(y2[i])
    trace.set_data(history_x[-50:], history_y[-50:]) # Show last 50 steps

    # Phase Space updates
    phase1.set_data(t1[:i], w1[:i])
    phase2.set_data(t2[:i], w2[:i])
    ax2.relim()
    ax2.autoscale_view()

    return line, trace, phase1, phase2

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=dt*1000, blit=True)
plt.tight_layout()
plt.show()
