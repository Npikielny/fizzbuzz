"""
fizzbuzz.py
Author: Noah Pikielny
Credit: None
Assignment:
Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.
We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:
How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""
n = int(input("How many numbers shall we print? "))
f = int(input("For multiples of what number shall we print 'Fizz'? "))
b = int(input("For multiples of what number shall we print 'Buzz'? "))
terms = list(range(1, n + 1))


for i in terms:
    output = ""
    if i % (f) == 0:
        output = output + "Fizz"
    if i % b == 0:
        output = output + "Buzz "
    if output == "":
        output = output + str(i)
    print(output)
    


