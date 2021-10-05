import signal
import argparse
import time
from xml.etree import ElementTree as ET


def signal_handler(signal, frame):
    # if needed to stop some kind of main loop
    config.loop = 0
    print("\nStopping PROGRAM NAME. Thanks for using.")
    print("Please visit https://github.com/timgold81/")
    print("contact timgold@gmail.com\n")
    exit()


def myPause(sec):
    dev = 50  # devision - how many times in second to pause
    maximum = sec * dev
    i = 0
    while (config.loop and i < maximum):
        time.sleep(1 / dev)
        i = i + 1


class Config:
    loop = 1
    source_file = ""

    def handle_args(self):
        parser = argparse.ArgumentParser(description="XML SOAP precess")
        parser.add_argument("-s", "--source_file", help="source file to process", required=True)
        args = parser.parse_args()

        if args.source_file:
            self.source_file = args.source_file
        else:
            self.source_file = "NONE"


def main():
    if config.source_file == "NONE":
        print("No source file")
        return -1

    namespaces = {
        'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
        'soap-enc': 'http://schemas.xmlsoap.org/soap/encoding/',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xsd': 'http://www.w3.org/2001/XMLSchema',
        'cwmp': 'urn:dslforum-org:cwmp-1-2',
    }
    # namespaces = {
    #     'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    #     'a': 'http://www.etis.fskab.se/v1.0/ETISws',
    # }
    tree=ET.parse(config.source_file)
    # ET.indent(tree)
    # ET.dump(tree)
    # tree.write("cwmp-idented.xml")
    print("************************")
    for item in tree.findall("soap:Body",namespaces):
        for i in item.findall('.//'):
            print (f"tag: {i.tag} , attribute: {i.attrib}")


    # xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap-enc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:cwmp="urn:dslforum-org:cwmp-1-2"


if (__name__ == "__main__"):
    signal.signal(signal.SIGINT, signal_handler)
    global config
    config = Config()
    config.handle_args()
    main()
