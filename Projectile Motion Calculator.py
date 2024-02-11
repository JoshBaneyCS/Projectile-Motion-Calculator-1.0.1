#Version 1.0.1
#By Joshua Baney
#2/2/24
#Portfolio for a BS student in Computer Science and Mathematics
#Project- Projectile motion calculator 


import matplotlib.pyplot as plt
import numpy as np

def calculate_trajectory(v0, angle, mass, density, launch_height):
    g = 9.81  # acceleration due to gravity (m/s^2)
    dt = 0.01  # time step for numerical integration

    # Convert input values to SI units
    launch_height = launch_height / 3.281  # convert launch height from feet to meters

    # Initialize variables
    x, y, vx, vy, t = [0], [launch_height], [v0 * np.cos(np.radians(angle))], [v0 * np.sin(np.radians(angle))], [0]

    for i in range(1, 10000):
        # Calculate acceleration components
        ax = 0
        ay = -g

        # Update velocities
        vx.append(vx[-1] + ax * dt)
        vy.append(vy[-1] + ay * dt)

        # Update positions
        x.append(x[-1] + vx[-1] * dt)
        y.append(y[-1] + vy[-1] * dt)

        # Update time
        t.append(t[-1] + dt)

        # Check for impact with the ground
        if y[-1] < 0:
            break

    return x, y, vx, vy, t

def plot_trajectory(x, y, vx, vy, t, points):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="Plot of particle trajectory")

    plt.scatter(np.array(x)[points], np.array(y)[points], color='red')

    plt.title("Launch Trajectroy Calculator by Josh Baney")
    plt.xlabel("Horizontal Distance (meters)")
    plt.ylabel("Vertical Distance (meters)")
    plt.legend()

    for point in points:
        plt.text(x[point], y[point], f'({x[point]:.2f}, {y[point]:.2f})', fontsize=8, color='blue')

    plt.grid(True)
    plt.show()

def main():
    # Get user input
    v0 = float(input("Enter the velocity in meters per second: "))
    launch_angle = float(input("Enter the launch angle in degrees: "))
    mass = float(input("Enter the mass in kilograms: "))
    density = float(input("Enter the density in kg/m^3: "))
    launch_height = float(input("Enter the launch height in feet: "))

    # Calculate trajectory without air resistance
    x_no_air, y_no_air, vx_no_air, vy_no_air, t_no_air = calculate_trajectory(v0, launch_angle, mass, density, launch_height)

    # Output information at the start, top of the curve, and when the object hits the ground
    start_point = 0
    top_point = np.argmax(y_no_air)
    equal_dist_point_1 = int(len(x_no_air)/4)
    equal_dist_point_2 = int(3*len(x_no_air)/8)  # Adjusted to be further from midpoint
    end_point = -1

    points = [start_point, top_point, equal_dist_point_1, equal_dist_point_2, end_point]

    for point in points:
        vx_val = vx_no_air[point]
        vy_val = vy_no_air[point]

        print(f"Point {point + 1} - Elapsed Time: {t_no_air[point]:.2f}s, Displacement: {x_no_air[point]:.2f}m, Vertical Velocity: {vy_val:.2f}m/s, Horizontal Velocity: {vx_val:.2f}m/s, Tangential Velocity: {np.sqrt(vx_val**2 + vy_val**2):.2f}m/s")

    # Plot trajectory with data points
    plot_trajectory(x_no_air, y_no_air, vx_no_air, vy_no_air, t_no_air, points)

if __name__ == "__main__":
    main()
