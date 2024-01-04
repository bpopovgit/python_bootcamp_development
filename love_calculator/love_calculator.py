print("The Love Calculator is calculating your score...")
name1 = input()
name2 = input()
combined_names = name1 + name2
lower_names = combined_names.lower()

t = lower_names.count('t')
r = lower_names.count('r')
u = lower_names.count('u')
e = lower_names.count('e')

l = lower_names.count('l')
o = lower_names.count('o')
v = lower_names.count('v')

true_num = t + r + u + e
love_num = l + o + v + e

total_score = str(true_num) + str(love_num)


if int(total_score) < 10 or int(total_score) > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40 <= int(total_score) <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")







