'''Create a Triangle class that accepts three side-lengths of the triangle as a, b 
and cas parameters at the time of object creation. 
Class Triangle should have the following methods:
Is_valid():- Returns valid if triangle is valid otherwise returns Invalid.
A triangle is valid when the sum of its two side-length are greater than the third one.
That means the triangle is valid if all three condition are satisfied:
a+b>c
a+c>b
b+c>a
Side_Classification(): If the triangle is invalid then return Invalid. 
Otherwise, it returns the type of triangle according to the sides of the triangle as follows:
Return Equilateral if all sides are of equal length.
Return Isosceles if any two sides are of equal length and third is different.
Return Scalene if all sides are of different lengths.
Angle_Classification(): If the triangle is invalid then return Invalid. 
Otherwise, return type of triangle using Pythagoras theorem.
For example if a < b <= c. then
If a ^ 2 + b ^ 2 > c ^ 2 return Acute
If a ^ 2 + b ^ 2 = c ^ 2 return Right
If a ^ 2 + b ^ 2 < c ^ 2 return obtuse
In the formula of angle classification, 
the square of the largest side length should be compared to the sum of squares of the other two side lengths.
Area(): If the triangle is invalid then return Invalid. Otherwise, return the area of the triangle.
Area = √[s(s-a) (s-b) (s-c)]
Wheres s = (a + b + c) / 2'''

import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Is_valid(self):  # Note: Capital 'I' to match your main code
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Valid"
        return "Invalid"

    def Side_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isosceles"
        else:
            return "Scalene"

    def Angle_Classification(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
        sides = sorted([self.a, self.b, self.c])
        a, b, c = sides
        if a**2 + b**2 > c**2:
            return "Acute"
        elif a**2 + b**2 == c**2:
            return "Right"
        else:
            return "Obtuse"

    def Area(self):
        if self.Is_valid() == "Invalid":
            return "Invalid"
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())