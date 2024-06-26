import json
import sys

def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except json.JSONDecodeError:
        print("zły plik json.")
        sys.exit(1)

if __name__ == "__main__":
    input_file = "C:\\Users\\Asus-pc\\Desktop\\Projekt\\input.json"
    data = load_json(input_file)
    print(data)
