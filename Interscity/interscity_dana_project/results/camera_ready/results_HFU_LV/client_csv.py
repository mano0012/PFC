import json
import datetime

startTime = ""
endTime = ""

matrix = [["" for i in range(3)] for j in range(120)]

row = -1
controller = 0
for files in range(30):
	file = open("NewResults" + str(files+1) + ".data")
	for line in file:
		if line != "\n":
			j = json.loads(line)
			if controller == 0:
				row += 1
				startTime = j['metrics'][0]['startTime']
				helper = startTime.split(" ")
				hour = helper[1].split(":")[0]
				minute = helper[1].split(":")[1]
				second = helper[1].split(":")[2]
				matrix[row][0] = hour + ":" + minute + ":" + second
				controller += 1
			elif controller == 14:
				arch = j['metrics'][0]['source']
				endTime = j['metrics'][0]['endTime']
				helper = endTime.split(" ")
				hour = helper[1].split(":")[0]
				minute = helper[1].split(":")[1]
				second = helper[1].split(":")[2]
				matrix[row][1] = hour + ":" + minute + ":" + second
				matrix[row][2] = arch 
				controller = 0
			else:
				controller += 1
	file.close()

#for count in range(120):
#	print (matrix[count][0] + " - " + matrix[count][1] + " - " + matrix[count][2]) 

file = open("request-file-burst-1.data", "r")
output = open("client.csv", "a")

count = 0
for line in file:
	data = line.split(" ")
	helper = data[0].split(":")
	
	hour = helper[0].split("[")[1]
	minute = helper[1]
	second = helper[2].split("]")[0]

	start = datetime.datetime.strptime(matrix[count][0], "%H:%M:%S")
	end = datetime.datetime.strptime(matrix[count][1], "%H:%M:%S")
	middle = datetime.datetime.strptime(hour + ":" + minute + ":" + second, "%H:%M:%S")

	#print(str(start) + " - " + str(middle) + " - " + str(end))
	
	if (start <= middle <= end):
		output.write(data[0] + "," + data[1][:-1] + "," + matrix[count][2] + "\n")
	elif (middle < start):
		continue
	else:
		count += 1
		if (count >= 120):
			print("ERROR!!!!")
			file.close()
			output.close()
			exit(1)
		else:
			output.write(data[0] + "," + data[1][:-1] + "," + matrix[count][2] + "\n")

file.close()
output.close()
