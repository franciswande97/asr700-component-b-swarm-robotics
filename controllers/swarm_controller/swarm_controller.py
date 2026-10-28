"""
True Differential Drive Swarm Controller.
Controls physical wheel motors for movement.
"""

from controller import Robot
import math

def run_robot():
    robot = Robot()
    timestep = int(robot.getBasicTimeStep())
    robot_name = robot.getName()

    # Initialize wheel motors
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')

    # Set motors to velocity control mode (infinite position)
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))

    # Start with zero velocity
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    print(f"[{robot_name}] Wheel motor controller started.")

    # Simple pattern: move forward and periodically turn to explore
    while robot.step(timestep) != -1:
        time_elapsed = robot.getTime()
        
        # Drive wheels: alternate turning and moving straight
        if int(time_elapsed) % 6 < 4:
            # Move straight forward
            left_motor.setVelocity(3.14)
            right_motor.setVelocity(3.14)
        else:
            # Turn to explore a new sector
            left_motor.setVelocity(3.14)
            right_motor.setVelocity(-3.14)

if __name__ == '__main__':
    run_robot()