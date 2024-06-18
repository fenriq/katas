# IP adress validation

import re
ip = '4.140.5.02'

xip = ip.split('.')
result = True
if xip == '':
    result = False
elif len(xip) < 4:
    result = False
else:
    for i in xip:
        if int(i.isdecimal()) and int(i) in range(256):
            if i != '0':
                if re.match(r"^[1-9]", i):
                    result = True
                else:
                    result = False
                    break
            elif i == '0':
                result = True
        else:
            result = False
            break

print(result)