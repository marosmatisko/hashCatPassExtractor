import base64, re, sys
import xml.etree.ElementTree as ET

def main():
        tree = ET.parse('shadowhash')
        root = tree.getroot()
        iterations = root[0][1][3].text
	with open("./entropy2", "r") as input:
		entropy = input.read()
	with open("./salt2", "r") as input:
		salt = input.read()
        with open("./hash.txt", "a") as output:
               output.write('$ml$' + iterations + '$' + "".join(salt.split()) + '$' + "".join(entropy.split()) + '\n')


if __name__ == "__main__":
        main()
