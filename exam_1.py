"""
program will compare and then determine which pay option is better
First option will pay 100 dollars per day for 10 days. The second option is 
1 dollar per day, and it will be doubled every day for 10 days.
There will be 2 functions, The first will calculate the pay rate for the first option
Function 2 will calculate the amount of the second function.
Function1 will return $100 * 10 days.
Function2 will be a loop function and it will loop 10 times, each time doubling the amount and adding the amount to the total.
If Option1 is better we will output "Option1 is better"
If Option2 is better, we will output "Option2 is better"
If Option1 and Option2 are equal, we will output, "Option1 and Option2 have the same payrate"


"""


"""
# option1
return 100 * 10 

# option2
amount = 1 
list1 = []
loop 10 times
  add amount to list1
  amount *=2
return amount

var1 = option1
var2 =option2

if var1 > var2 
  "Option1 is better"
If var1 < var2 
  "Option2 is better" 
  else
    "Option1 and Option2 pay the same"
"""

def option1():
  return 100 * 10

def option2():
  amount = 1 
  list1 = []
  for i in range (0,10)
    list1.append(amount)
    amount *= 2
  total = sum(list1)
  return total

def main():
var1 = option1() 
var2 = option2()

answer = ""
if var1 == var2:
  answer ="Option1 and Option2 pay the same"
If var1 < var2
  answer = "Option2 is better"
  else:
    "Option1 is better"
print(answer)