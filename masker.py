import random

with open('out.txt', 'r') as file:
    data = file.read()

N 			= 	len(data)
charlocs 	= 	[i for i, letter in enumerate(data) if letter != ' ']
maskRatio   =   0.05  
Nmask     	=   int(maskRatio*len(charlocs))
picked 		= 	random.sample(charlocs, Nmask)

for pick in picked:
	data = data[:pick] +' '+ data[pick+1:]

print(data)