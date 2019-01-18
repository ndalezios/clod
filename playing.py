import sys
import json
import argparse

program_name = sys.argv[0]
print(program_name)
#arguments = sys.argv[1:]
#print(arguments)

parser = argparse.ArgumentParser() 
parser.add_argument("-i","--input", required=True, 
	help="input file containing json CADF event records")
args = parser.parse_args()

input_file = args.input
print("Parsing file : %s" %(input_file))
	
with open(input_file, "r") as input_data:
    data = json.load(input_data)
print(json.dumps(data, indent=4))
