# Question 1 #######################
# Answer 1 Easy Solution
import ast
import math
import urllib.request
import json

str = "{'totalCount':'1','ID':'1029','IP':'10.0.0.1'}"
result = ast.literal_eval(str)
print(result)
for keys, values in result.items():
    print(keys)
    print(values)
# Answer 2
print("Parsing Question 1")

str2 = "{'totalCount':'1','ID':'1029','IP':'10.0.0.1'}"
str2 = str2.replace("{","")
str2 = str2.replace("}","")

list = str2.split(",")
dictionary ={}
for i in list:
    keyvalue = i.split(":")
    m = keyvalue[0].strip('\'')
    m = m.replace("\"", "")
    dictionary[m] = keyvalue[1].strip('"\'')

print(dictionary)
############################
#Question 2
print("Question 2")
endpoint ='https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyD01eydqbWnobrfsJp6Me4hD86uXEYlAbE'
origin = 'Seattle'
destination = 'Portland'
method = 'driving'

nav_request = 'origin=()&destination=()&mode=()&key=()'.format(origin,destination,method,api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print (directions)

############################
#Question 3
class Shape(object):
    sides = None
    name = None
    perimeter = None
    area = None

    def names(self):
        pass
    def perimeter(self):
        pass
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius, name):
        self.radius = radius
        self.name = name
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return self.radius * math.pi * 2


class Triangle(Shape):
    def __init__(self, sides, name):
        self.sides = sides
        self.name = name
    def area(self):
        return
    def perimeter(self):
        return

