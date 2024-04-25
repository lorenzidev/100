print("Welcome to the love calculator! \n")

name1 = input('What is his name? \n') 
name2 = input ('What is her name? \n')

combined_names = name1 + name2

lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

result1 = t + r + u + e

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')
e = lower_names.count('e')

result2 = l + o + v + e

score = int(str(result1) + str(result2))

if (score < 40):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) or (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}, don't keep trying.")