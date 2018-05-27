import csv
import sys
import numpy

def CiscoObject():
	#opens output file
	file = open("../output/pyObject.txt","a+")
	continueQuery = "y"



	while (continueQuery == "y"):

#Object type definition
		tunnelObject = input ("Are these objects for an IPsec Tunnel? (y/n)")
		if tunnelObject == "y":

#CSV READ
			loadFile = input ("Did you load the localObjects.csv and remoteObjects.csv in /files? (y/n) ")
			if loadFile == "y":

#opens Local and remote CSV
				with open('../files/localObjects.csv', 'rt') as csvLoc:
			    		localAddr = csv.reader(csvLoc, delimiter=',', quotechar='|')
			    		localAddr = list(localAddr)

				with open('../files/localObjects.csv', 'rt') as csvRem:
			    		remoteAddr = csv.reader(csvRem, delimiter=',', quotechar='|')
			    		remoteAddr = list(remoteAddr)
			else:
				print ("WTF are you doing here then? Exiting Program")
				sys.exit()
#Local object Creation
			objectType = input ("Please enter the object type (network, service) ")
			if objectType == "network":
				netType = input ("What type of network object? (host, subnet) ")
				if netType == "host":
					for i in range(len(localAddr)):
						print("object", objectType, localAddr[i][1], "\n", "host", localAddr[i][0], file=open("../output/pyObject.txt", "a"))
				else:
					print ("invalid input")
				continueQuery = input ("Do you have any more objects? (y/n) ")
			elif netType == "subnet":
				for i in range(len(localAddr)):
					print("object", objectType, localAddr[i][1], "\n", "subnet", localAddr[i][0], localAddr[i][2], file=open("../output/pyObject.txt", "a"))
				continueQuery = input ("Do you have any more object files? (y/n) ")
			else:
				print ("Invalid input; exiting...")
				sys.exit()