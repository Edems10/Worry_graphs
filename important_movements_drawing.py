import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import json

base_dir = '/home/edems/Work/Worry_graphs'

movement_prediction_dir = os.path.join(base_dir,'graphs_movement_deviation','games_movement_prediction')
file_path = os.path.join(base_dir,'games.txt')
minimap_img = mpimg.imread('/home/edems/Work/Worry_graphs/dragontail-13.4.1/13.4.1/img/map/map11.png')
champion_dir = '/home/edems/Work/Worry_graphs/dragontail-13.4.1/13.4.1/img/champion'
threshold_path = os.path.join(base_dir,'graphs_winrate_deviation','thresholds')
output = os.path.join(base_dir,'images_crucial_moments_movement')


def read_files_in_directory(directory_path):
    file_list = []

    # Check if the given path is a directory
    if os.path.isdir(directory_path):
        # Iterate over all files in the directory
        for filename in os.listdir(directory_path):
            # Join the directory path with the filename to get the full file path
            file_path = os.path.join(directory_path, filename)

            # Check if the path is a file (not a subdirectory)
            if os.path.isfile(file_path):
                # Append the file path to the list
                file_list.append(file_path)

    return file_list


def create_plot_for_moment(positions, title,file_name_without_extension,mistake_type,moment_time,main_moment):
    plt.clf()  # Clear the figure
    plt.imshow(minimap_img, extent=[0, 1000, 0, 1000])
    # Plot champion images at current positions with larger size (twice as big)
    for champion_iter, position in enumerate(positions["current_position"]):
        if champion_iter <= 4:
            champion_image_path = os.path.join(champion_dir, 'Akali.png')  # Replace 'Akali.png' with the actual champion image file
        else:
            champion_image_path = os.path.join(champion_dir, 'Zed.png')  # Replace 'Zed.png' with the actual champion image file

        champion_img = mpimg.imread(champion_image_path)
        plt.imshow(champion_img, extent=[position[0] - 30, position[0] + 30, position[1] - 30, position[1] + 30])

    # Draw arrows from current position to next positions with reduced transparency
    for current, next_pos in zip(positions["current_position"], positions["next_positions"]):
        plt.arrow(current[0], current[1], next_pos[0] - current[0], next_pos[1] - current[1],
                  color='green', width=10, alpha=0.9)  # Adjust alpha value here

    # Draw arrows from current position to predicted positions with reduced transparency
    for current, predicted_pos in zip(positions["current_position"], positions["predicted_positions"]):
        plt.arrow(current[0], current[1], predicted_pos[0] - current[0], predicted_pos[1] - current[1],
                  color='red', width=10, alpha=0.9)  # Adjust alpha value here

    # Remove numbers from axes
    plt.axis('off')
    # Add labels and legend
    plt.title(title)
    plt.legend()
    result_dir = os.path.join(output,file_name_without_extension,mistake_type,main_moment)
    if not os.path.exists(result_dir):
    # Create the directory if it doesn't exist
        os.makedirs(result_dir)
    final_name = file_name_without_extension +'_'+ moment_time+'.png'
    result_filename = os.path.join(result_dir,final_name)
    
    # Save the plot as an image
    plt.savefig(result_filename, bbox_inches='tight')


# Example usage:
files = read_files_in_directory(movement_prediction_dir)

for file in files:
    file_name_with_extension = os.path.basename(file)
    path_current_threshold = os.path.join(threshold_path,file_name_with_extension)
    file_name_without_extension = os.path.splitext(file_name_with_extension)[0]
    
    with open(file, 'r') as json_file:
        positions = json.load(json_file)
    
    with open(path_current_threshold, 'r') as threshold_json:
        thresholds = json.load(threshold_json)

    red_thresholds = thresholds['red_threshold']
    orange_thresholds = thresholds['orange_threshold']
    yellow_thresholds = thresholds['yellow_threshold']
    
    for red_threshold in red_thresholds:
        
        red_threshold = red_threshold*10
        moment_before = str(red_threshold-10)
        moment_after = str(red_threshold+10)
        # Plot the minimap as background
        red_threshold = str(red_threshold)
        
        threshold_positions = positions[red_threshold]
        moment_before_position = positions[moment_before]
        moment_after_position = positions[moment_after]
        create_plot_for_moment(moment_before_position,'Moment before crucial moment',
                               file_name_without_extension,'Crucial',moment_before,red_threshold)
        create_plot_for_moment(threshold_positions,'Crucial moment',
                               file_name_without_extension,'Crucial',red_threshold,red_threshold)
        create_plot_for_moment(moment_after_position,'Moment after crucial moment',
                               file_name_without_extension,'Crucial',moment_after,red_threshold)
        
    for orange_threshold in orange_thresholds:
        
        orange_threshold = orange_threshold*10
        moment_before = str(orange_threshold-10)
        moment_after = str(orange_threshold+10)
        # Plot the minimap as background
        orange_threshold = str(orange_threshold)
        
        threshold_positions = positions[orange_threshold]
        moment_before_position = positions[moment_before]
        moment_after_position = positions[moment_after]
        create_plot_for_moment(moment_before_position,'Moment before Regular moment',
                               file_name_without_extension,'Regular',moment_before,orange_threshold)
        create_plot_for_moment(threshold_positions,'Regular moment',
                               file_name_without_extension,'Regular',orange_threshold,orange_threshold)
        create_plot_for_moment(moment_after_position,'Moment after Regular moment',
                               file_name_without_extension,'Regular',moment_after,orange_threshold)
        
    for yellow_threshold in yellow_thresholds:
        
        yellow_threshold = yellow_threshold*10
        moment_before = str(yellow_threshold-10)
        moment_after = str(yellow_threshold+10)
        # Plot the minimap as background
        yellow_threshold = str(yellow_threshold)
        
        threshold_positions = positions[yellow_threshold]
        moment_before_position = positions[moment_before]
        moment_after_position = positions[moment_after]
        create_plot_for_moment(moment_before_position,'Moment before Minor moment',
                               file_name_without_extension,'Minor',moment_before,yellow_threshold)
        create_plot_for_moment(threshold_positions,'Minor moment',
                               file_name_without_extension,'Minor',yellow_threshold,yellow_threshold)
        create_plot_for_moment(moment_after_position,'Moment after Minor moment',
                               file_name_without_extension,'Minor',moment_after,yellow_threshold)
        