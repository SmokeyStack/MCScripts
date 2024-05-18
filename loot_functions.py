import glob
import json
import os

def get_json_from_file(fh):
    try:
        # If possible, read the file as JSON
        return json.loads(fh)
    except:
        # If not, read the file as a string, and try to parse it as JSON
        contents = ""
        for line in fh.splitlines():
            cleanedLine = line.split("//", 1)[0]
            if len(cleanedLine) > 0 and line.endswith("\n") and "\n" not in cleanedLine:
                cleanedLine += "\n"
            contents += cleanedLine
        while "/*" in contents:
            preComment, postComment = contents.split("/*", 1)
            contents = preComment + postComment.split("*/", 1)[1]
        return json.loads(contents)

def main():
    # Define the root directory where you want to search
    root_directory = "."  # Assuming you're starting from the root directory
    global_function_values = []

    # Recursively search for JSON files within loot_tables folders
    for folder, _, files in os.walk(root_directory):
        if "loot_tables" in folder:
            for file in files:
                if file.endswith(".json"):
                    try:
                        file_path = os.path.join(folder, file)
                        with open(file_path, "r", encoding="utf-8") as fh:
                            json_data = get_json_from_file(fh.read())
                            # Extract the "condition" values
                            condition_values = []
                            for pool in json_data.get("pools", []):
                                for entries in pool.get("entries", []):
                                    for function in entries.get("functions", []):
                                        condition_values.append(function.get("function"))
                                        global_function_values.append(function.get("function"))

                            print(f"Functions in {file_path}: {condition_values}")
                    except Exception as e:
                        print(f"Error in file: {file_path}")
                        print(e)
                        raise
    print(f"Complete sest of functions: {set(global_function_values)}")

main()
