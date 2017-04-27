import base64, re, sys
import xml.etree.ElementTree as ET

def main():
        tree = ET.parse('shadowhash')
        root = tree.getroot()
        entropy = root[0][1][1].text
	salt = root[0][1][5].text 
        pat=re.compile(r'\s+') 
        entropy = pat.sub('', entropy)
	salt = pat.sub('', salt)
        #print(salt)
	with open("./entropy", "w") as output:
		output.write(entropy.decode('base64'))
	with open("./salt", "w") as output:
		output.write(salt.decode('base64'))	

if __name__ == "__main__":
	main()
