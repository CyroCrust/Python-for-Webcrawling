hrs = input("Enter Hours:")
rat = input('Enter Rate:')
try:
    h = float(hrs)
    r = float(rat)
except:
    h = 0
    r = 0

if h <= 40 :
    print(h * rat)
else:
    xh = h - 40
    print(420 + (xh * r * 1.5))
