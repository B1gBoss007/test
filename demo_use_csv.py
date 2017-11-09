# -*- coding: cp936 -*-
import csv
import urllib2



with open("scv.csv","r+") as f:
    c = csv.DictReader(f)
    for row in c:
        print row
        print row["SKT"] #读取指定列
        if row["TEAM"]=="ADC":
            print row #读取指定行
