# importing the requests library
import requests
import os
import json
 
# api-endpoint
URL = "http://localhost:1337/edems_swag/legue_predict/1.0.0/predictionWinrateJson"
 
 

 
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'games.txt')  # Replace 'file.txt' with the path to your text file

print(file_path)

with open(file_path, 'r') as file:
    for line in file:
        game = line.strip()  # Remove any extra whitespace or newline characters
        game_json = game +'.json'
        PARAMS = {'game':game_json}
        r = requests.get(url = URL, params = PARAMS)
        game_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'games_winrate',game_json)
        try:
            data = r.json()
            with open(game_path, 'w') as file_game:
                json.dump(data, file_game, indent=4)  # Use 'json.dump()' to write JSON data to the file
        except json.JSONDecodeError as e:
            # Handle the JSON decoding error here
            data = None  # Assign None or handle the situation accordingly
            print("JSONDecodeError with:",game)
            with open(game_path, 'w') as file_game:
                json.dump(data, file_game, indent=4)  # Use 'json.dump()' to write JSON data to the file
        except requests.RequestException as e:
            # Handle the request exception here
            print("RequestException with:",game)
            data = None  # Assign None or handle the situation accordingly
            json.dump(data, file_game, indent=4)  # Use 'json.dump()' to write JSON data to the file
        


