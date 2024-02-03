import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

data = {
    "current_position": [
        [346, 396], [252, 563], [351, 490], [371, 660], [492, 543],
        [384, 155], [522, 338], [911, 558], [566, 439], [660, 472]
    ],
    "next_positions": [
        [304, 391], [212, 508], [533, 609], [459, 514], [498, 546],
        [291, 159], [545, 323], [874, 198], [549, 462], [807, 152]
    ],
    "predicted_positions": [
        [292, 375], [208, 458], [458, 542], [458, 542], [458, 542],
        [375, 125], [625, 375], [875, 458], [625, 375], [625, 542]
    ]
}

# Load minimap image
minimap_img = mpimg.imread('/home/edems/Work/Worry_graphs/dragontail-13.4.1/13.4.1/img/map/map11.png')
champion_dir = '/home/edems/Work/Worry_graphs/dragontail-13.4.1/13.4.1/img/champion'

# Plot the minimap as background
plt.imshow(minimap_img, extent=[0, 1000, 0, 1000])

# Plot champion images at current positions with larger size (twice as big)
for champion_iter, position in enumerate(data["current_position"]):
    if champion_iter <= 4:
        champion_image_path = os.path.join(champion_dir, 'Akali.png')  # Replace 'Akali.png' with the actual champion image file
    else:
        champion_image_path = os.path.join(champion_dir, 'Zed.png')  # Replace 'Zed.png' with the actual champion image file

    champion_img = mpimg.imread(champion_image_path)
    plt.imshow(champion_img, extent=[position[0] - 30, position[0] + 30, position[1] - 30, position[1] + 30])

# Draw arrows from current position to next positions with reduced transparency
for current, next_pos in zip(data["current_position"], data["next_positions"]):
    plt.arrow(current[0], current[1], next_pos[0] - current[0], next_pos[1] - current[1],
              color='green', width=10, alpha=0.9)  # Adjust alpha value here

# Draw arrows from current position to predicted positions with reduced transparency
for current, predicted_pos in zip(data["current_position"], data["predicted_positions"]):
    plt.arrow(current[0], current[1], predicted_pos[0] - current[0], predicted_pos[1] - current[1],
              color='red', width=10, alpha=0.9)  # Adjust alpha value here

# Remove numbers from axes
plt.axis('off')

# Add labels and legend
plt.title('League of Legends Player Positions with Arrows and Larger Champion Icons')
plt.legend()

# Show the plot
plt.show()
