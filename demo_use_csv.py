# -*- coding: cp936 -*-
import csv
import urllib2



with open("scv.csv","r+") as f:
    c = csv.DictReader(f)
    for row in c:
        print row
        print row["SKT"] #��ȡָ����
        if row["TEAM"]=="ADC":
            print row #��ȡָ����
