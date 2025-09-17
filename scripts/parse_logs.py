import json

with open("ecu_output.log", "r") as f:
    logs = f.readlines()

parsed = {"lines": [line.strip() for line in logs]}
with open("logs.json", "w") as out:
    json.dump(parsed, out, indent=2)

print(json.dumps(parsed, indent=2))
