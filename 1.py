# -*- coding:utf8 -*-
import unicodedata
import csv

headers = ["成语","长度","拼音","成语解释","出自","去调拼音","首字拼音","末字拼音"]
def calc(t):
    ans = 0
    for i in t:
        if i != '，' and i != ' ':
            ans += 1
    return ans

def first(t):
    ans = ''
    for i in t:
        if i == ' ':
            return ans
        else:
            ans += i


def last(t):
    ans = ''
    for i in reversed(t):
        if i == ' ':
            return ans
        else:
            ans = i + ans           

with open('成语词典（30972）-utf8.csv',mode = 'r',encoding = 'utf-8')as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        with open('cyyy.csv',mode = 'a',newline = '',encoding = 'utf-8')as f:
            f_csv = csv.writer(f)
            #f_csv.writeheader()
            ttt = []
            ttt.append(row[0])
            ttt.append(calc(row[0]))
            ttt.append(row[1])
            ttt.append(row[2])
            ttt.append(row[3])
            mystr = unicodedata.normalize('NFKD', row[1]).encode('ascii','ignore')
            mystr = mystr.decode("utf8")
            ttt.append(mystr)

            ttt.append(first(mystr))
            ttt.append(last(mystr))

            f_csv.writerow(ttt)

