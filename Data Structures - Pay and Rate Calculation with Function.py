hrs = input("Enter Hours:")
rat = input('Enter Rate:')
try:
    h = float(hrs)
    r = float(rat)
except:
    h = 0
    r = 0


def computepay(h,r):

    if h <= 40 :
        return h * r
    else:
        xh = h - 40
        return(420 + (xh * r * 1.5))


p = computepay(h,r)
print("Pay",p)
