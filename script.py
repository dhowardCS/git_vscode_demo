import sys
import requests

print(sys.version)
msg = 'hello'
print(msg)

def greet(visitor):
    return 'hello '+ visitor

print(greet("Derek"))

r= requests.get("http://google.com").status_code 
print("Google status: ", r)

ans = input('Whats your name?__')
print(greet(ans))
