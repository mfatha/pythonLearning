#reading csv
import csv

result = ""

with open("C:/Users/LENOVO/Desktop/1.csv") as csvFile:
    readCsv = csv.reader(csvFile, delimiter=',')

print('''
    Multi line printing..
    hello world
''')

#try/catch block
    try:
        value = input("enter the Number? to find its Index")
        row = 0
        for l in readCsv:
            row = row+1
            for i in l:
                if(i == value):
                    #print("Value found  in : row = ",row," cloumn = ",(l.index(i)+1))
                    result = "Value found  in : row = {}  cloumn = {}".format(row,(l.index(i)+1))
                    break

    except Exception as e:
        print(e)

print(result)

#Reading CSV iwth pandas library
import pandas as pd

df = pd.read_csv('C:/Users/LENOVO/Desktop/1.csv')
df.head()

#urlLib Request parse
import urllib.request
import urllib.parse

#x= urllib.request.urlopen('https://jsonplaceholder.typicode.com')
#print(x.read())

url ='http://pythonprogramming.net'
values = {  's':'basics',
            'submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
res = urllib.request.urlopen(req)
resData = res.read()

print(resData)
