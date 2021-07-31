name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()


for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    wordi = words[1]
    if wordi not in counts:
        counts[wordi] = 1
    else:
        counts[wordi] = counts[wordi] + 1



bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
