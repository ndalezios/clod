import sys
import json

program_name = sys.argv[0]
print(program_name)
#arguments = sys.argv[1:]
#print(arguments)

if len(sys.argv) != 2 :
	print("Usage: python3 playing.py input_file")
	sys.exit(1)
else :
	print("Parsing file : %s" %(sys.argv[1]))
	
with open(sys.argv[1], "r") as input_raw:
    data = json.load(input_raw)
print(json.dumps(data, indent=4))
