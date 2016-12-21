import os

for filename in os.listdir("."):
	if filename.find("-"):
		os.rename(filename, filename.replace("-", "_"))