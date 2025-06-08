
def num():
    guess = int(input("Guess a number"))
    add = str(int(guess + 2))
    print( "The result is " + add)
    print("good job")


def hello():
    print("hello")
    name = input("What's your name")
    print("hello" + name)

num()
hello()
print("bye")
