import sys
import requests 
import math 
import datetime
import os

print(sys.version)
msg = 'hello'
print(msg)

def greet(visitor):
    return 'hello '+ visitor

print(greet("Derek"))

r= requests.get("http://google.com").status_code 
print("Google status: ", r)

print(hex(123))
print(bin(2323)) 
print(chr(65))
nums = range(1, 100)
print(sum(nums))
print(nums[1:5])
print("_".join({"1", "2", "3"}))
currTime= datetime.datetime(2021, 6, 21)
print(currTime.strftime("%c"))
f = open("demofile.txt")
print(f.read(2))
for x in f:
    print(x)

f.close()

file = open("MyFile.txt" , "x")
file.write("Hi")
file.close()
file = open("MyFile.txt", "r")
f = file.read()
for i in f:
    print(i)

file.close()

if os.path.exists("MyFile.txt"):
    os.remove("MyFile.txt")
else:
    print("File does not exist")
