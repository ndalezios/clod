import json
from json import JSONDecodeError
import argparse
import constants


def parse_as_json(indata):
    """deserialize indata to a Python object"""
    print("Parsing file : %s" % (indata))
    with open(indata, "r") as indata:
        try:
            outdata = json.load(indata)
        except JSONDecodeError:
            print("Not a valid JSON file")
            outdata = []
    return outdata


def parse_as_text(infile):
    outdata = []
    print("Assuming %s file is a text file containing mixed JSON and text" % infile)
    print("Trying to clear lines from garbage in head (START_KEY) and tail...")
    print("START_KEY : %s" % constants.START_KEY1)
    # print("END_KEY : %s" % constants.END_KEY)
    print("to change START_KEYs edit file constants.py")
    with open(infile, "r") as indata:
        line = indata.readline()
        while line:
            if (line.find(constants.START_KEY1) != -1):
                start_pos = line.find(constants.START_KEY1)
            elif (line.find(constants.START_KEY2) != -1):
                start_pos = line.find(constants.START_KEY2)
            elif (line.find(constants.START_KEY3) != -1):
                start_pos = line.find(constants.START_KEY3)
            elif (line.find(constants.START_KEY4) != -1):
                start_pos = line.find(constants.START_KEY4)
            # print("############################################")
            tmp_line = line[start_pos:]
            # print("Just printing line1 from start_pos to end BEFORE %s" %
            #     tmp_line)
            while(tmp_line.count("{") < tmp_line.count("}")):
                # print("tmp_line has %s occurances of { " % tmp_line.count("{"))
                # print("tmp_line has %s occurances of } " % tmp_line.count("}"))
                end_pos = tmp_line.rfind("}")
                tmp_line = tmp_line[: end_pos]

            end_pos = tmp_line.rfind("}") + 1
            tmp_line = tmp_line[: end_pos]

            # print("Just printing line1 from start_pos to end AFTER %s " %
            #     tmp_line)
            # print("############################################")
            outdata.append(tmp_line)
            """end_pos = line.rfind(constants.END_KEY)
            if (start_pos != -1) and (end_pos != -1):
                outdata.append(line[start_pos:end_pos])
            else:
                outdata.append(line)"""

            line = indata.readline()
    print("Processed %s lines" % len(outdata))
    return outdata


def print_resource(data_dict):
    """Print all the Resource fields.

    input is data_dict, a dictionary in python which represents a JSON object
    eg. print_resource(data[0]["initiator"]) where data is a python list
    """
    default = "not set / empty"
    print("typeURI       : %s" % data_dict.get("typeURI", default))
    print("id            : %s" % data_dict.get("id", default))
    print("name          : %s" % data_dict.get("name", default))
    print("domain        : %s" % data_dict.get("domain", default))
    print("credential    : %s" % data_dict.get("credential", default))
    print("addresses     : %s" % data_dict.get("addresses", default))
    print("host          : %s" % data_dict.get("host", default))
    print("geolocation   : %s" % data_dict.get("geolocation", default))
    print("geolocationId : %s" % data_dict.get("geolocationId", default))
    print("attachments   : %s" % data_dict.get("attachments", default))


def main():
    data = []
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True,
                        help="input file containing json CADF event records")
    args = parser.parse_args()
    input_file = args.input
    # assume input is a text file
    data = parse_as_text(input_file)
    # json_data = parse_as_json(data) 

    print("==============================================================")
    print("Found %s CADF event records" % (len(data)))
    print("==============================================================")
    input("Press Enter to continue...")
    print(data[0])
    print(data[1])
    print(data[2])
    # print(data[3])
    print(data.__class__)
    print(data[0].__class__)


"""
    

    print(json.dumps(data, indent=4))
    print(constants.BIG_DOC)
    print("===========================================")
    print("What (Event)")
    print("===========================================")
    print("%s" % data[0]["eventType"])
    print("%s" % data[0]["action"])
    print("%s" % data[0]["outcome"])
    print("%s" % data[0]["reason"])
    print("===========================================")
    print("When (Event,Reporter)")
    print("===========================================")
    print("%s" % data[0]["eventTime"])
    print("===========================================")
    print("Who & FromWhere (Initiator)")
    print("===========================================")
    print_resource(data[0]["initiator"])
    print("===========================================")
    print("OnWhat & ToWhere (Target)")
    print("===========================================")
    print_resource(data[0]["target"])
    print("===========================================")
    print("Where (Observer)")
    print("===========================================")
    print_resource(data[0]["observer"])

"""
"""
    print("==============================================================")
    print("OBSERVER %s" % data[0]["observer"])
    print("--------------------------------------------------------------")
    print("WHO (initiator) %s" % data[0]["initiator"])
    print("--------------------------------------------------------------")
    print("TARGET %s" % data[0]["target"])
    print("--------------------------------------------------------------")
    print("EVENT_TYPE %s" % data[0]["eventType"])
    print("--------------------------------------------------------------")
    print("WHEN (eventTime UTC) %s" % data[0]["eventTime"])
"""


"""
else:
	# print(json.dumps(data, indent=4))
"""


if __name__ == "__main__":

    main()
