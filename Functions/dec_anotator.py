def welcome(x):
    def wrapper():
        print("Hello")
        x()
        print("Bye!")
    return wrapper

# This are annotators
@welcome
def morning():
    print("GOOD MORNING!")
morning()

@welcome
def evening():
    print("GOOD EVENING!")
evening()