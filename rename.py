# change the name to fit Github listing convention
import os

for file in os.listdir():
	if file.startswith(("ex3", "ex4", "ex5", "ex6", "ex7", "ex8",  "ex9")):
		os.rename(file, file.replace("ex", "ex0"))
		