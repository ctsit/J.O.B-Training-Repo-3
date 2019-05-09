# prompt for hours and rate to compute pay with overtime calculation
# catching exceptions with try and except
# updated with a function
# Kevin was here 1/29/2018
# Roukna was here 01/29/2018
# Taryn was here on 1/29/18
# Tiago was here on 2/20/18
# Tiago was here on 2/20/18 again
# Surya was here on 2/20/18
# Angela was here on 05-09-2019

def computepay(hours, rate):
    overtime = hours - 40
    if hours > 40:
        pay = (40 * rate) + (overtime * rate * 1.5)
        pay = float2dollar(pay)
        return pay
    else:
        pay = hours * rate
        pay = float2dollar(pay)
        return pay

def float2dollar(num):
    return '${:,.2f}'.format(num)

try:
    hours = raw_input('How many hours did you work? ')
    hours = float(hours)
    rate = raw_input('How much did you get payed each hour? ')
    rate = float(rate)
except:
    print 'Error, please enter numeric input.'

pay = computepay(hours, rate)


print 'Pay:', pay
print 'Hours worked overtime', hours - 40
