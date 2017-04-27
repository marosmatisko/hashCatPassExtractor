import base64, re, sys
import xml.etree.ElementTree as ET

def main(username):
	tree = ET.parse(username + '.plist')
	root = tree.getroot()
	hashFound = False
	for child in root[0]:
		if hashFound:
			hash = child[0].text
			break
		if child.text == "ShadowHashData":
			hashFound = True
	pat=re.compile(r'\s+')
	hash = pat.sub('', hash).strip()
	#print(hash)
	with open("./shadowhash", "w") as output:
		output.write(hash.decode('base64'))

if __name__ == "__main__":
	main(sys.argv[1])
