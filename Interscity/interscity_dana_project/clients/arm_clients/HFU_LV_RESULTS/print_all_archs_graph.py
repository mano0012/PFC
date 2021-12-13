import matplotlib
import matplotlib.pyplot as plt
import json

#var prepping
list = []
yValues = []
xValues = []

yValues1 = []
xValues1 = []

yValues2 = []
xValues2 = []

yValues3 = []
xValues3 = []

xController = 0
xController1 = 0
xController2 = 0
xController3 = 0

counter = 0
list = []
file = open("NewResults.data", "r") 
for line in file:
	if line != "\n":
		j = json.loads(line)
		if ((counter >= 0) and (counter < 75)):
			if counter == 0:
				arch1 = j['metrics'][0]['source'] 
			xValues.append(xController)
			yValues.append(j['metrics'][0]['value']/j['metrics'][0]['count'])
			xController = xController + 5
		if ((counter >= 75) and (counter < 150)):
			if counter == 75:
				arch2 = j['metrics'][0]['source'] 
			xValues1.append(xController1)
			yValues1.append(j['metrics'][0]['value']/j['metrics'][0]['count'])
			xController1 = xController1 + 5
		if ((counter >= 150) and (counter < 225)):
			if counter == 150:
				arch3 = j['metrics'][0]['source'] 
			xValues2.append(xController2)
			yValues2.append(j['metrics'][0]['value']/j['metrics'][0]['count'])
			xController2 = xController2 + 5		
		if ((counter >= 225) and (counter < 300)):
			if counter == 225:
				arch4 = j['metrics'][0]['source'] 
			xValues3.append(xController3)
			yValues3.append(j['metrics'][0]['value']/j['metrics'][0]['count'])
			xController3 = xController3 + 5
		counter = counter + 5

fig, ax = plt.subplots()
ax.plot(xValues, yValues, label=arch1)
ax.plot(xValues1, yValues1, label=arch2)
ax.plot(xValues2, yValues2, label=arch3)
ax.plot(xValues3, yValues3, label=arch4)
ax.legend()
ax.set(xlabel='Time (s)', ylabel='Response time (ms)', title='')
ax.grid()
fig.savefig("all_archs_graphs.png")
plt.show()
