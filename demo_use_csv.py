# -*- coding: cp936 -*-
import csv
import urllib2

# http://www.lfhacks.com/tech/python-read-specific-row-csv

with open("scv.csv","r+") as f:
    c = csv.DictReader(f)
    for row in c:
        print row
        print row["SKT"] #读取指定列
        if row["TEAM"]=="ADC":
            print row #读取指定行
