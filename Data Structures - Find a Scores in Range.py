Num = input("Enter a Number Between 0.0 and 1.0:")
try:
    n = float(Num)

except:
    print('Only Use numbers please')


if n >= 1.0:
    print ('Not in Range')
    quit()
if n >= 0.6:
    if n >= 0.9:
        print('A')
    elif n >= 0.8:
        print('B')
    elif n >= 0.7:
        print('C')
    elif n >= 0.6:
        print('D')
    elif n < 0.0:
        print ('Not in Range')
        quit()

else:
    print ('F')
