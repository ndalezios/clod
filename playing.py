import sys
import json
from json import JSONDecodeError
import argparse


def parse_file(infile):
	print("Parsing file : %s" %(infile))
	with open(infile, "r") as indata:
		try:
			outdata = json.load(indata)
		except JSONDecodeError:
			print("Not a valid JSON file")
			outdata = []
	return outdata
    
program_name = sys.argv[0]
print(program_name)
#arguments = sys.argv[1:]
#print(arguments)

parser = argparse.ArgumentParser() 
parser.add_argument("-i","--input", required=True, 
	help="input file containing json CADF event records")
args = parser.parse_args()

input_file = args.input
data = parse_file(input_file)
if len(data) == 0 :
	pass
else:
	#print(json.dumps(data, indent=4))
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




