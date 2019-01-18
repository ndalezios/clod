import json

print ("hello world")

with open("tiny_dataset", "r") as input_raw:
    data = json.load(input_raw)
print(json.dumps(data, indent=4))
