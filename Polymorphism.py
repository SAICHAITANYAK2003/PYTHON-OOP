#Animal:

    # Implement the Dog, Cat and Cow classes appropriately
    
    class Dog:
        def info(self):
            return ('I am a Dog and I say Woof!')
        
        def perform_special_action(self):
            return "I fetch the ball"
    
    class Cat:
        def info(self):
            return ('I am a Cat and I say Meow!')
        
        def perform_special_action(self):
            return "I chase a mouse"
    
    class Cow:
        def info(self):
            return ('I am a Cow and I say Moo!')
        
        def perform_special_action(self):
            return "I am grazing in the field"
    
    # Do not change any code below.
    # Do not call this function anywhere.
    
    def main():
        dog1 = Dog()
        cat1 = Cat()
        cow1 = Cow()
    
        animals = [dog1, cat1, cow1]
    
        for animal in animals:
            print(animal.info())
            print(animal.perform_special_action())
    
    main()
