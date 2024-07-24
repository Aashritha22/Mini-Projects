target = int(input())
calculation = 0 
for number in range(1,target):
    if number % 2 == 0:
       calculation += number
print(calculation)
    