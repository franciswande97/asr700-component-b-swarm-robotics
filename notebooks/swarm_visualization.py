"""
Matplotlib Visualisation Script for Swarm Convergence and Trajectories.
"""

import matplotlib.pyplot as plt
import numpy as np

# Simulated trajectory data for 3 agents over time steps
time_steps = 50
np.random.seed(42)

# Agent 1 trajectory (Leader/Explorer)
x1 = np.cumsum(np.random.normal(0.05, 0.1, time_steps)) - 1.0
y1 = np.cumsum(np.random.normal(0.05, 0.1, time_steps)) - 1.0

# Agent 2 trajectory (Collaborator A)
x2 = np.cumsum(np.random.normal(0.05, 0.1, time_steps)) + 1.0
y2 = np.cumsum(np.random.normal(-0.05, 0.1, time_steps)) - 1.0

# Agent 3 trajectory (Collaborator B)
x3 = np.cumsum(np.random.normal(-0.05, 0.1, time_steps))
y3 = np.cumsum(np.random.normal(0.08, 0.1, time_steps)) + 1.0

plt.figure(figsize=(8, 6))
plt.plot(x1, y1, label='Agent 1 (Explorer)', marker='o', markersize=3)
plt.plot(x2, y2, label='Agent 2 (Collaborator A)', marker='s', markersize=3)
plt.plot(x3, y3, label='Agent 3 (Collaborator B)', marker='^', markersize=3)

plt.title('Multi-Agent Swarm Trajectories & Distributed Coverage Convergence')
plt.xlabel('X Position (meters)')
plt.ylabel('Y Position (meters)')
plt.axhline(0, color='grey', linestyle='--', linewidth=0.8)
plt.axvline(0, color='grey', linestyle='--', linewidth=0.8)
plt.grid(True)
plt.legend()
plt.savefig('reports/swarm_convergence_plot.png', dpi=300)
plt.show()
print("Swarm convergence plot generated and saved successfully to reports/swarm_convergence_plot.png")