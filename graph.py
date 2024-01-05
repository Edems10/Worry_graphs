import json
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.realpath(__file__))
print(base_dir)

# Load data from JSON file
file_list = os.listdir(os.path.join(base_dir, 'games_winrate'))

for file_name in file_list:
    with open(os.path.join(base_dir, 'games_winrate', file_name), 'r') as file:
        data = json.load(file)
        
    if data is not None:
        # Extract win rate probabilities for team 1
        last_key = list(data['probabilities'].keys())[-1]
        win_rates_team_1 = [data['probabilities'][str(i)]['team_1'] for i in range(10, int(last_key) + 1, 10)]

        # Generate x-axis values
        x_values = list(range(10, int(last_key) + 1, 10))

        # Find the differences in win rates between consecutive intervals
        differences = [abs(win_rates_team_1[i] - win_rates_team_1[i - 1]) for i in range(1, len(win_rates_team_1))]

        # Define thresholds
        threshold_yellow = [0.02, 0.045]
        threshold_orange = [0.045, 0.07]
        threshold_red = 0.07

        # Get file name without extension
        file_name_without_extension = os.path.splitext(file_name)[0]

        # Plotting the graph with different types of mistakes highlighted by differences
        fig, ax = plt.subplots(figsize=(10, 6))

        # Plot all data points as a line
        ax.plot(x_values, win_rates_team_1, linestyle='-', color='blue', linewidth=2, label='Win Rate')

        # Categorize mistakes based on thresholds
        yellow_indices = [i for i, diff in enumerate(differences) if threshold_yellow[0] < diff <= threshold_yellow[1]]
        orange_indices = [i for i, diff in enumerate(differences) if threshold_orange[0] < diff <= threshold_orange[1]]
        red_indices = [i for i, diff in enumerate(differences) if diff > threshold_red]

        # Create scatterplots for different types of mistakes
        ax.scatter([x_values[ind] for ind in yellow_indices],
                   [win_rates_team_1[ind] for ind in yellow_indices],
                   color='yellow',
                   marker='o',
                   s=150,
                   label=f' {threshold_yellow[0]} > Winrate change >= {threshold_yellow[1]} ')

        ax.scatter([x_values[ind] for ind in orange_indices],
                   [win_rates_team_1[ind] for ind in orange_indices],
                   color='orange',
                   marker='o',
                   s=150,
                   label=f'{threshold_orange[0]} > Winrate change >= {threshold_orange[1]} ')

        ax.scatter([x_values[ind] for ind in red_indices],
                   [win_rates_team_1[ind] for ind in red_indices],
                   color='red',
                   marker='o',
                   s=150,
                   label=f'Winrate change > {threshold_red} ')


        file_name_without_extension = os.path.splitext(file_name)[0]
        file_path = os.path.join(base_dir,'games.txt')
        text_to_find = file_name_without_extension   

        name_found = -1
        # Open the file and search for the exact text match
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines, start=1):
                if line.strip() == text_to_find:
                    name_found = line_number
                    break  # Stops after finding the first occurrence
            else:
                print(f"The text '{text_to_find}' was not found in '{file_path}'")

        file_path = os.path.join(base_dir,'LCS_Week.txt')
        line_number_to_select = name_found # Replace this with the line number you want to select

        
        # Open the file and select the specific line
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= line_number_to_select:
                selected_line = lines[line_number_to_select - 1].strip()  # Subtract 1 for zero-based indexing
                lcs_week = selected_line
            else:
                print(f"Line number {line_number_to_select} does not exist in '{file_path}'")
         
        file_path = os.path.join(base_dir,'names.txt')       
         # Open the file and select the specific line
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) >= line_number_to_select:
                selected_line = lines[line_number_to_select - 1].strip()  # Subtract 1 for zero-based indexing
                game_name = selected_line
            else:
                print(f"Line number {line_number_to_select} does not exist in '{file_path}'")


        # Add labels, title, legend, etc.
        ax.set_ylim(0, 1)
        ax.set_xlim(min(x_values), max(x_values))
        ax.set_xticks(range(0, max(x_values) + 1, 150))
        ax.set_xlabel('Time (in seconds)', fontsize=12)
        ax.set_ylabel('Win Percentage', fontsize=12)
        ax.axhline(y=0, color='gray', linestyle='--', linewidth=1, alpha=0.7)
        ax.set_title(f'Win Rate for {lcs_week}: {game_name}', fontsize=14)
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()

        plt.savefig(os.path.join(base_dir, 'graphs', file_name_without_extension), bbox_inches='tight')  # Save as PNG format, adjust filename and extension as needed