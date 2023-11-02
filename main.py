your_name = input("Enter your name: ")
love_name = input("Enter your love's name: ")
lower_name = your_name.lower()
lower_love = love_name.lower()
true_love = lower_name + " " + lower_love
print(f"Your true love is '{true_love}'")
love_percent_01 = true_love.count('t') + true_love.count('r') + true_love.count('u') + true_love.count('e')
love_percent_02 = true_love.count('l') + true_love.count('o') + true_love.count('v') + true_love.count('e')
love_percent = str(love_percent_01) + str(love_percent_02)
print(f"Your love percentage is {love_percent}")
if int(love_percent) < 10:
    print("Your love percentage is below 10 and it's too low.")
elif int(love_percent) > 40 and int(love_percent) < 50:
    print("Your love percentage is between 40 and 50, and it's in a normal go.")
elif int(love_percent) > 90:
    print("Your love percentage is greater than 90 and it's a blast")
