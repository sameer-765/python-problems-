 **Iterating through a list of numbers**
for i  in 10,20,30,40:
  print(i)
**Counting down with range**
for i in range (102,-2,-1):
    print(i)
****Loop with variable manipulation and string iteration**
x=10
for i in range(20,10,-2):
    x=x+2
    print("Hi")
for i in "Hi":
  print(x,end=" ")
**Summation with string length and range loop**
z=3
for i in "island":
  z=z+1
s=z
for i in range (z):
    s=s+i
print(s)
** Pattern printing with loops **
for i in range (5):
    print ("*",end=" ")
print()
for i in range (5):
    print ("*       *")
for i in range (5):
    print ("*",end=" ")
**Multiplication table based on even/odd input**
a = int (input("Enter any num : "))
if a%2==0:
    for i in range (1,11):
        print("{} x {} = {} ".format(i,a,i*a))
else:
    for i in range(1,a+1):
        print("{} x {} = {} ".format(i,a,i*a))
**Word counter for a sentence**
a = input("Enter any sentence: ")
c = 0

for i in range(len(a)):
    if a[i] != " " and (i == 0 or a[i-1] == " "):
        c += 1

print("The total words:", c)
**Player Guessing Game**
import random

p1 = input("Enter player1: ")
p2 = input("Enter player2: ")

s1 = 10
s2 = 10

d1 = random.randint(1, 10)
d2 = random.randint(1, 10)

print("----- PLAYER1 TURN -----")
while True:
    g1 = int(input("Enter ur guess: "))
    s1 = s1 - 1
    if g1 == d1:
        break

print("----- PLAYER2 TURN -----")
while True:
    g2 = int(input("Enter ur guess: "))
    s2 = s2 - 1
    if g2 == d2:
        break

print("----- SUMMARY -----")
print("{}:{}".format(p1, s1))
print("{}:{}".format(p2, s2))
print("----------------------")

if s1 > s2:
    print("Winner is", p1)
elif s2 > s1:
    print("Winner is", p2)
else:
    print("DRAW")



