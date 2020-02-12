class Cat(object):
    def say(self):
        print("i am a cat")


class Dog(object):
    def say(self):
        print("i am a dog")


class Duck(object):
    def say(self):
        print("i am a duck")


animal_list = [Cat, Dog, Duck]

for animal in animal_list:
    animal().say()


