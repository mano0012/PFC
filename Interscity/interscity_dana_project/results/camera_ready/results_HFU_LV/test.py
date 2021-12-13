import json

startTime = ""
endTime = ""

controller = 0
for files in range(30):
	file = open("NewResults" + str(files+1) + ".data")
	for line in file:
		if line != "\n":
			j = json.loads(line)
			if controller == 0:
				startTime = j['metrics'][0]['startTime']
				helper = startTime.split(" ")
				hour = helper[1].split(":")[0]
				minute = helper[1].split(":")[1]
				second = helper[1].split(":")[2]
				print("startTime: " + hour + " : " + minute + " : " + second)
			elif controller == 14:
				endTime = j['metrics'][0]['startTime']
				helper = endTime.split(" ")
				hour = helper[1].split(":")[0]
				minute = helper[1].split(":")[1]
				second = helper[1].split(":")[2]
				print("endTime: " + hour + " : " + minute + " : " + second)
				controller = 0
				break
			controller += 1

file = open("request-file-burst-1.data", "r")
for line in file:
	data = line.split(" ")
	grossTime = data[0].split(":")
	hour = grossTime[0].split("[")[1]
	minute = grossTime[1]
	second = grossTime[2].split("]")[0]
	print(hour + " : " + minute + " : " + second)
	break





















	
