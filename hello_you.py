# Ask user for their name
name = input("Your name would be nice: ")
print(name)

# Ask user for their age
age = input("How old are you?: ")
print(age)

# Ask user for their town/city
town = input("Where do you live?: ")
print(town)

# Ask user what they enjoy doing
hobby = input("what do you enjoy doing?: ")
print(hobby)

# Ask user what they do
occupation = input("What do you do?: ")

# Create output text
string = "Hello {},you are {} years old. You live in {}. You are a {} but you love {}. Nice meeting you {}!"
output = string.format(name,age,town,occupation,hobby,name)

# Print output to screen
print(output)
