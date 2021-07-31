smallest = None
largest = None
my_list = []

while True:


    numb = input("Enter Number:")

    if numb == ("done"):
        break

    try:
        my_list.append (int(numb))


    except:
        print('Invalid input')
    continue

for i in my_list:
    if largest is None:
        largest = i
    elif i > largest:
    	largest = i
print ('Maximum is',largest)


for i in my_list:
    if smallest is None:
        smallest = i
    elif i < smallest:
    	smallest = i
print ('Minimum is',smallest)
