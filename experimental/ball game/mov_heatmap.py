import numpy as np
import matplotlib.pyplot as plt
import random

# Board dimensions
rows, cols = 9, 16

# Initialize heatmap to count cell visits
heatmap = np.zeros((rows, cols))

# Movement directions (8 possible directions)
# Each tuple is in the form (row_change, col_change)
directions = [
    (-1, 0),   # up
    (1, 0),    # down
    (0, -1),   # left
    (0, 1),    # right
    (-1, -1),  # up-left
    (-1, 1),   # up-right
    (1, -1),   # down-left
    (1, 1)     # down-right
]

# Number of cycles (steps) per direction per run
cycles_per_direction = 1000

# Number of times each direction is simulated with a random initial position
sampling_size = 100

# Simulate ball movement for each initial direction
for direction in directions:
    for _ in range(sampling_size):
        # Random initial position within board boundaries (not on the walls)
        ball_pos = [random.randint(1, rows - 2), random.randint(1, cols - 2)]
        current_direction = direction  # Start with the chosen direction

        # Perform a fixed number of cycles in this direction
        for _ in range(cycles_per_direction):
            # Increment heatmap at the current ball position
            heatmap[ball_pos[0], ball_pos[1]] += 1

            # Calculate the next position
            new_row = ball_pos[0] + current_direction[0]
            new_col = ball_pos[1] + current_direction[1]

            # Check if the ball hits a vertical wall
            if new_row <= 0 or new_row >= rows - 1:
                # Bounce vertically by reversing the vertical component
                current_direction = (-current_direction[0], current_direction[1])
                new_row = ball_pos[0] + current_direction[0]  # Adjust position post-bounce

            # Check if the ball hits a horizontal wall
            if new_col <= 0 or new_col >= cols - 1:
                # Bounce horizontally by reversing the horizontal component
                current_direction = (current_direction[0], -current_direction[1])
                new_col = ball_pos[1] + current_direction[1]  # Adjust position post-bounce

            # Update the ball position
            ball_pos = [new_row, new_col]

# Plotting the heatmap
plt.figure(figsize=(8, 4))
plt.imshow(heatmap, cmap='hot', interpolation='nearest')
plt.colorbar(label='Frequency of Visits')
plt.title("Heatmap of Ball Movements")
plt.xlabel("Columns")
plt.ylabel("Rows")
plt.show()
