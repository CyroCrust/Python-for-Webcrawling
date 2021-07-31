
fname = input("Enter file name: ")
fh = open(fname)
my_list = []
my_list2 = []
my_list3 = []
l = 0

for line in fh:

    word = line.split()
    my_list.append(word)


for sublist in my_list:
    for item in sublist:
        my_list2.append(item)


counts = {}
for word in my_list2:
    if word not in counts:
        counts[word] = 0
        my_list3.append(word)


my_list3.sort()
print(my_list3)
