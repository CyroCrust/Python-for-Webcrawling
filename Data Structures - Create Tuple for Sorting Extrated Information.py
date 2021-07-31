name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()

    hour = words[5]
    hours = hour.split(':')
    hoursm = hours[0]
    if hoursm not in counts:
    	counts[hoursm] = 1
    else:
        counts[hoursm] = counts[hoursm] + 1


listy = list()

for key,val in counts.items():
    newtup = (key,val)
    listy.append(newtup)

listy = sorted(listy)

for val,key in listy:
    print(val,key)
