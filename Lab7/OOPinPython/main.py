from Models import Animal,Dog,Cat
def main():
    a = Animal()
    d = Dog()
    c = Cat()

    animals = [a,d,c]
    for animal in animals:
        print(animal)
        print(animal.info())
        print(animal.speak())
        print("-" * 20)

    print(d.eat())
    print(c.play())

    if __name__ == "__main__":
        main()

