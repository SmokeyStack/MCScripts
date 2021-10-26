import uuid
import json
import os
from pathlib import Path

def yes_no(variable):
    while variable not in ["y", "n"]:
        variable = input("Please enter 'y' or 'n'\n").lower()
    if variable == "y":
        return True
    return False

def new_manifest(manifest_name, manifest_description, manifest_type):
    manifest = {
        "format_version": 2,
        "header": {
            "name": manifest_name,
            "manifest_description": manifest_description,
            "manifest_uuid": str(uuid.uuid4()),
            "version": [1, 0, 0],
            "min_engine_version": [1, 17, 0]
        },
        "modules": [
            {
                "type": manifest_type,
                "uuid": str(uuid.uuid4()),
                "version": [1, 0, 0]
            }
        ]
    }
    return manifest

new_manifest_name = input("Please enter the name of the new manifest\n")
new_manifest_description = input("Please enter a description for the new manifest\n")
new_manifest_type = input("Please enter the type for the new manifest\n")
new_manifest = new_manifest(new_manifest_name, new_manifest_description, new_manifest_type)
print(json.dumps(new_manifest, indent=4))

main_path = "output"
path = os.path.join(main_path, "manifest")
Path(path).mkdir(parents=True, exist_ok=True)
file = os.path.join(path, "manifest.json")
f = open(file, "w")
f.write(json.dumps(new_manifest, indent=4))
f.close()
print("Manifest file was successfully created")