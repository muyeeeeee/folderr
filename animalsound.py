#function to print animal sounds
def animal_sounds(animals):
    for animal in animals:
        if animal == "cat":
            print("cat - meow")
        elif animal == "dog":
            print("dog - woof")
        elif animal == "cow":
            print("cow - moo")
        elif animal == "duck":
            print("duck - quack")
        else: 
            print(f"{animal} - unknown sound")
            
#list of animals
my_animals = ["cat", "dog", "cow", "duck", "tiger"]

#call the function
animal_sounds(my_animals)
