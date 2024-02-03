import requests
import os
import json

# api-endpoint
BASE_URL = "http://90.180.16.91:1337/edems_swag/legue_predict/1.0.0/predictionJson"

# Directory to store the prediction files
output_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'games_movement_prediction')
output_directory_error = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'games_movement_prediction_error')

# Create the directory if it doesn't exist
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    
# Create the directory if it doesn't exist
if not os.path.exists(output_directory_error):
    os.makedirs(output_directory_error)

file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'games.txt')

print(file_path)

with open(file_path, 'r') as file:
    for line in file:
        game = line.strip()  # Remove any extra whitespace or newline characters
        url = f"{BASE_URL}?game={game}&scale=1000&scale=1000"
        print(url)
        r = requests.get(url)

        game_path = os.path.join(output_directory, game)
        game_error = os.path.join(output_directory_error, game)
        try:
            data = r.json()
            with open(game_path, 'w') as file_game:
                json.dump(data, file_game, indent=4)
        except json.JSONDecodeError as e:
            # Handle the JSON decoding error here
            data = None  # Assign None or handle the situation accordingly
            print("JSONDecodeError with:", game)
            with open(game_error, 'w') as file_game:
                json.dump(data, file_game, indent=4)
        except requests.RequestException as e:
            # Handle the request exception here
            print("RequestException with:", game)
            data = None  # Assign None or handle the situation accordingly
            json.dump(data, file_game, indent=4)
