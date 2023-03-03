import time
year = 1970
exDays = 13 # кол-во високосных дней с 1970
def numMonth(days):
    num = 0
    end = False
    while(not(end)):
        if (num in [3, 5, 8, 10]):
            if(days <= 30):
                end = True
            else:
                days -= 30
                num += 1

        if (num in [0, 2, 4, 6, 7, 9, 11]):
            if (days <= 31):
                end = True
            else:
                days -= 31
                num += 1

        if (num == 1):
            if (days <= 28):
                end = True
            else:
                days -= 28
                num += 1

    return [(num + 1), days]

timestamp = int(time.time())

Year = timestamp // 31536000
Days = (timestamp % 31536000) // 86400 - exDays + 1 # +1 т.к. отсчет начинается с 1 января

hour = timestamp % 86400 // 3600
minutes = timestamp % 3600 // 60
sec = timestamp % 60

DateNow = str(year + Year) + "-" + str('{:02}'.format(numMonth(Days)[0])) + "-"\
          + str('{:02}'.format(numMonth(Days)[1])) + "  " + str('{:02}'.format(hour)) \
          + ":" + str('{:02}'.format(minutes)) + ":" + str('{:02}'.format(sec))

print(timestamp)
print(DateNow)
