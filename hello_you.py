# Introduction
print("Hello there, I'm James Darko Amponsah...")

# Ask user for their name
name = input("Your name would be nice: ").title()

# Ask user for their age
age = input("{},how old are you?: ".format(name))
print("Wow,that's good to know!")

# Ask user for their town/city
town = input("Where do you live?: ")

# Ask user for their region
region = input("{},where is {} located?(eg.Volta region): ".format(name,town))

# Ask user what they enjoy doing
hobby = input("what do you enjoy doing?: ")

# Ask user what they do
occupation = input("What do you do?: ")

# Create output text
string = "Hello {},you are {} years old and from {} in the {} region. You are a {} but you love {}. Nice meeting you {}!"
output = string.format(name,age,town,region,occupation,hobby,name)

# Print output to screen
print(output)

