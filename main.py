def hello(to="friend"):
    print("hello,", to)
def main():
    hello()
    name = input("What's your name?").strip().capitalize()
    hello(name)


main()

print("Lets experiment with numbers")

x = float(input("What's x"))
y = float(input("What's y"))

z= round(x/y, 1)
print(f"{z:,}")
