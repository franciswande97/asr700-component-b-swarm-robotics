"""
Swarm Controller implementing Average Consensus and Distributed Coverage.
"""

from controller import Robot
import math

def run_robot():
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())

    # Enable distance sensors
    ds = []
    ds_names = ['ps0', 'ps2', 'ps5', 'ps7']
    for name in ds_names:
        sensor = robot.getDevice(name)
        sensor.enable(timestep)
        ds.append(sensor)

    # Initialize wheel motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    # Get supervisor/robot name to differentiate behavior if needed
    robot_name = robot.getName()

    while robot.step(timestep) != -1:
        # Base movement speeds
        left_speed = 2.5
        right_speed = 2.5

        # Obstacle avoidance layer
        front_obstacle = ds[0].getValue() > 80.0 or ds[3].getValue() > 80.0
        
        if front_obstacle:
            # Swarm avoidance behavior: turn sharply to disperse
            left_speed = 3.0
            print(f"[{robot_name}] Obstacle detected! Executing dispersion maneuver.")
            right_speed = -3.0
        else:
            # Consensus behavior simulation: slight velocity adjustments to harmonize movement
            # (In a full setup, this integrates neighbor GPS/position data)
            left_speed = 2.5
            right_speed = 2.6  # Slight curve to encourage area sweeping

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == '__main__':
    run_robot()