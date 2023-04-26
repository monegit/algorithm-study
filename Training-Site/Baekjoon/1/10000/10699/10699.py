from datetime import datetime

d = datetime.now()

month = d.month
day = d.day

if len(str(d.month)) < 2:
    month = "{0}{1}".format(0, d.month)

if len(str(d.day)) < 2:
    day = "{0}{1}".format(0, d.day)

print("{0}-{1}-{2}".format(d.year, month, day))
