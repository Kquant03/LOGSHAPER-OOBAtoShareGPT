import json
import os

# Function to read JSON file and return its content
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# Function to convert JSON content into JSONL format
def convert_to_jsonl(file_path):
    json_data = read_json_file(file_path)
    conversations = []
    
    for entry in json_data["internal"]:
        conversations.append({"from": "human", "value": entry[0]})
        conversations.append({"from": "gpt", "value": entry[1]})
    
    jsonl_data = {"conversations": conversations}
    
    return jsonl_data

# Directory containing JSON files
input_directory = "/home/REDACTED/Documents/humanity/JSONS"

# Output file for JSONL
output_file = "/home/REDACTED/Documents/humanity/Converted.json"

# List to store JSONL data
jsonl_data_list = []

# Iterate through each file in the directory
for filename in os.listdir(input_directory):
    if filename.endswith(".json"):
        file_path = os.path.join(input_directory, filename)
        jsonl_data = convert_to_jsonl(file_path)
        jsonl_data_list.append(jsonl_data)

# Writing all JSONL data into a single file
with open(output_file, 'w', encoding='utf-8') as outfile:
    for jsonl_data in jsonl_data_list:
        json.dump(jsonl_data, outfile, ensure_ascii=False)
        outfile.write('\n')  # Add newline after each JSONL entry
