f = open("test.txt")
fileLines = f.readlines()
for line in fileLines:
    print(line)
introString =  "My Name is Harshika. I am 12 years old"
words = introString.split()
print(words)
phrases = introString.split(".")
print(phrases)
def greet(name):
    print("Hello, "+name+". How are you?")
greet("Harshika")