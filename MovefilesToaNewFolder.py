

import os, shutil

currentLocation = raw_input("Enter the path of the current folder: ")
FutureLocation = raw_input("Enter the path of the future folder: ")

if not os.path.exists(FutureLocation):
	os.makedirs(FutureLocation)

dirs = os.listdir(currentLocation)

for file in dirs:
	sd = os.path.join(currentLocation, file)
	lst = os.listdir(sd)
	for f in lst:
		curF = os.path.join(sd, f)
		futF = os.path.join(FutureLocation, f)
		shutil.copy2(curF, futF)