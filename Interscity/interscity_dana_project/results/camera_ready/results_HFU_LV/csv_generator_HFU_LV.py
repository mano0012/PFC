import json

matrix1 = [["" for i in range(31)] for j in range(15)]
matrix2 = [["" for i in range(31)] for j in range(15)]
matrix3 = [["" for i in range(31)] for j in range(15)]
matrix4 = [["" for i in range(31)] for j in range(15)]

xController = 0
xController1 = 0
xController2 = 0
xController3 = 0

row = 0
column = 0
for i in range(30):
	column = i
	counter = 0
	file = open("NewResults" + str(i+1) + ".data", "r")
	row = 0 
	for line in file:
		if line != "\n":
			j = json.loads(line)
			if ((counter >= 0) and (counter < 75)):
				if counter == 0:
					row = 0
					arch1 = j['metrics'][0]['source'] 
				matrix1[row][column] = str(j['metrics'][0]['value']/j['metrics'][0]['count'])
				if (column == 29):
					matrix1[row][column+1] = str(xController)
					xController = xController + 5
			if ((counter >= 75) and (counter < 150)):
				if counter == 75:
					row = 0
					arch2 = j['metrics'][0]['source'] 
				matrix2[row][column] = str(j['metrics'][0]['value']/j['metrics'][0]['count'])
				if (column == 29):
					matrix2[row][column+1] = str(xController1)
					xController1 = xController1 + 5
			if ((counter >= 150) and (counter < 225)):
				if counter == 150:
					row = 0
					arch3 = j['metrics'][0]['source'] 
				matrix3[row][column] = str(j['metrics'][0]['value']/j['metrics'][0]['count'])
				if (column == 29):
					matrix3[row][column+1] = str(xController2)
					xController2 = xController2 + 5		
			if ((counter >= 225) and (counter < 300)):
				if counter == 225:
					row = 0
					arch4 = j['metrics'][0]['source'] 
				matrix4[row][column] = str(j['metrics'][0]['value']/j['metrics'][0]['count'])
				if (column == 29):
					matrix4[row][column+1] = str(xController3)
					xController3 = xController3 + 5
			counter = counter + 5
			row += 1


hfuLvFile = open("HFU_LV.csv", "a")
hfuLvFile.write(arch1 + ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
for i in range(15):
	for j in range(31):
		hfuLvFile.write(matrix1[i][j] + ",")
	hfuLvFile.write("\n")

hfuLvFile.write("\n")
hfuLvFile.write("\n")
hfuLvFile.write(arch2 + ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
for i in range(15):
	for j in range(31):
		hfuLvFile.write(matrix2[i][j] + ",")
	hfuLvFile.write("\n")

hfuLvFile.write("\n")
hfuLvFile.write("\n")
hfuLvFile.write(arch3 + ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
for i in range(15):
	for j in range(31):
		hfuLvFile.write(matrix3[i][j] + ",")
	hfuLvFile.write("\n")

hfuLvFile.write("\n")
hfuLvFile.write("\n")
hfuLvFile.write(arch4 + ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n")
for i in range(15):
	for j in range(31):
		hfuLvFile.write(matrix4[i][j] + ",")
	hfuLvFile.write("\n")

hfuLvFile.close()