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

print("==============================================================")
print("Found %s CADF event records" %(len(data)))
print("==============================================================")
print(json.dumps(data[:1], indent=4))
print("==============================================================")
print("OBSERVER %s" %data[0]["observer"])
print("--------------------------------------------------------------")
print("WHO (initiator) %s" %data[0]["initiator"])
print("--------------------------------------------------------------")
print("TARGET %s" %data[0]["target"])
print("--------------------------------------------------------------")
print("EVENT_TYPE %s" %data[0]["eventType"])
print("--------------------------------------------------------------")
print("WHEN (eventTime UTC) %s" %data[0]["eventTime"])




