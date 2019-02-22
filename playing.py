import json
from json import JSONDecodeError
import argparse
import constants


def parse_file(infile):
    """deserialize infile to a Python object"""
    print("Parsing file : %s" % (infile))
    with open(infile, "r") as indata:
        try:
            outdata = json.load(indata)
        except JSONDecodeError:
            print("Not a valid JSON file")
            outdata = []
    return outdata


def parse_as_json(infile):
    outdata = []
    with open(infile, "r") as indata:
        line = indata.readline()
        print(constants.START_KEY)
        print(constants.END_KEY)
        while line:
                # print(line)
            start_pos = line.find(constants.START_KEY)
            end_pos = line.rfind(constants.END_KEY)
            if (start_pos != -1) and (end_pos != -1):
                outdata.append(line[start_pos:end_pos + 1])
            line = indata.readline()
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True,
                        help="input file containing json CADF event records")
    args = parser.parse_args()
    input_file = args.input
    data = parse_file(input_file)
    # data = parse_as_json(input_file)
    print("==============================================================")
    print("Found %s CADF event records" % (len(data)))
    print("==============================================================")
    print("%s" % data[0])
    print("")

    # print(json_load)

    """for i in range(len(data)):
        print("--------------------------------------------------------------------")
        print("%s" % data[i])
        print("--------------------------------------------------------------------")
        print(json.dumps(data[i], indent=4))
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
