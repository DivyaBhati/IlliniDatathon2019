import pandas as pd

data = pd.read_csv('Honeywell.csv')

closelist = data['Close']
vollist = data['Volume']
dates = data['Date']

closed = []
vold = []
for i in range(len(closelist)):
	if i > 30:
		closed.append(sum(closelist[i-30:i]) / float(30))
		vold.append(sum(vollist[i-30:i]) / float(30))
	else:
		closed.append(0)
		vold.append(0)

done = pd.DataFrame({'Date': dates, 'close30d':closed, 'vol30d': vold})

done.to_csv('honeywell30d.csv')




