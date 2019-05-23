
import random
import configparser

config = configparser.ConfigParser()
config.read("prog.properties")
random_limit = int(config['DEFAULT']['random_limit'])
exp_sum = int(config['DEFAULT']['exp_sum'])

no_of_loop = int(input("Enter number for loop: "))
i=1
count=0
while i <= no_of_loop:
    a = random.randint(1, random_limit)
    b = random.randint(1, random_limit)

    total = a + b

    if total == exp_sum:
        print(a, b, total)
        count = count + 1
        
    i = i + 1
print("Total count:", count)
prob_of_sum = ( 100 * count ) / no_of_loop
print(prob_of_sum)
