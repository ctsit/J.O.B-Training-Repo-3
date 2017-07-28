# prompt for hours and rate to compute pay with overtime calculation
# catching exceptions with try and except
# updated with a function

def computepay(hours, rate):
    overtime = hours - 40
    if hours > 40:
        pay = (40 * rate) + (overtime * rate * 1.5)
        return pay
    else:
        pay = hours * rate
        return pay

try:
    hours = raw_input('How many hours did you work?')
    hours = float(hours)
    rate = raw_input('How much did you get payed each hour?')
    rate = float(rate)
except:
    print 'Error, please enter numeric input'

pay = computepay(hours, rate)

print 'pay:', pay
