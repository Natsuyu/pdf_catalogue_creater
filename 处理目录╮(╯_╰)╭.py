#usr/bin/env python
#-*- coding:utf-8 -*-

import re, sys

reload(sys)
sys.setdefaultencoding('utf8')

filename = "catagory.txt"
output = "result.txt"

file = open(filename, "r")
out = open(output, "w")

ret = "["
pat = re.compile(r'(.*?)(\d{1,4}$)')
for line in file.readlines():
    try:
        tmp =  re.findall(pat, line)
        print tmp[0][0], tmp[0][1]
        ret += "['" + tmp[0][0].strip() + "', " + tmp[0][1] + "],\n"
    except:
        ret += "['" + line.strip() + "'],\n"

ret += "]"
out.write(ret)

file.close()
out.close()