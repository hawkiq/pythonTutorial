import json
with open("api.json","r") as f:
    content = json.loads(f.read())

print(content["osama"])