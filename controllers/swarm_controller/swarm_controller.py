"""
Swarm Controller for Component B: Multi-Agent Area Coverage.
Handles initialization, sensor polling, and basic velocity commands.
"""

from controller import Robot
import math

def run_robot():
    # Initialize the Webots Robot instance
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())

    # Enable distance sensors (e-puck has 8 IR sensors: ps0 to ps7)
    ds = []
    ds_names = ['ps0', 'ps2', 'ps5', 'ps7']
    for name in ds_names:
        sensor = robot.getDevice(name)
        sensor.enable(timestep)
        ds.append(sensor)

    # Initialize wheel motors for differential drive
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    # Main control loop
    while robot.step(timestep) != -1:
        # Base forward velocity
        left_speed = 3.14
        right_speed = 3.14

        # Simple obstacle avoidance reaction
        front_obstacle = ds[0].getValue() > 80.0 or ds[3].getValue() > 80.0
        if front_obstacle:
            # Turn away from obstacle
            left_speed = 2.0
            right_speed = -2.0

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == '__main__':
    run_robot()