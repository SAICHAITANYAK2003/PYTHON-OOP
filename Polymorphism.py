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


#Student Evaluation:

        # Implement the Student, EssayWriter and DrawingArtist classes appropriately
        
        class Student:
            def __init__(self, student_id, name, class_section):
                self.student_id = student_id
                self.name = name
                self.class_section = class_section
                self.goal = None
            
            def evaluate(self):
                pass
            
            def set_goal(self,writer_goal):
                self.goal = writer_goal
        
        class EssayWriter(Student):
            def __init__(self, student_id, name, class_section, essays):
                super().__init__(student_id, name, class_section)
                self.goal = None
                self.essays = essays
            
            def evaluate(self):
                if(self.goal is None):
                    return "Goal Not Set"
                elif(self.essays >= self.goal):
                    return "Goal Met"
                elif (self.essays < self.goal):
                    return "Goal Not Met"
            
            def add_essays(self,essays_to_be_added):
                self.essays += essays_to_be_added
               
        
        class DrawingArtist(Student):
            def __init__(self, student_id, name, class_section, drawings):
                super().__init__(student_id, name, class_section)
                self.drawings = drawings
                self.goal = None
                
            def evaluate(self):
                if(self.goal is None):
                    return "Goal Not Set"
                elif(self.drawings >= self.goal):
                    return "Goal Met"
                elif (self.drawings < self.goal):
                    return "Goal Not Met"
                    
            def add_drawings(self,drawings_to_be_added):
                self.drawings += drawings_to_be_added
                
        
        # Do not change any code below.
        # Do not call this function anywhere.
        
        def main():
            student_id = input()
            name = input()
            class_section = input()
            writer_goal = input()
            artist_goal = input()
        
            essays = int(input())
            essays_to_be_added = int(input())
            drawings = int(input())
            drawings_to_be_added = int(input())
        
            essay_writer = EssayWriter(student_id, name, class_section, essays)
            if writer_goal == "None":
                essay_writer.set_goal(None)
            else:
                essay_writer.set_goal(int(writer_goal))
            essay_writer.add_essays(essays_to_be_added)
        
            drawing_artist = DrawingArtist(student_id, name, class_section, drawings)
            if artist_goal == "None":
                drawing_artist.set_goal(None)
            else:
                drawing_artist.set_goal(int(artist_goal))
            drawing_artist.add_drawings(drawings_to_be_added)
        
            print(essay_writer.evaluate())
            print(drawing_artist.evaluate())
        
        main()

#Vehicle Servicing

    # Implement the Vehicle, Car and Motorcycle classes appropriately
    
    class Vehicle:
        def __init__(self,tire_wear_limit,oil_change_limit,brake_service_limit):
            self.tire_wear_limit = tire_wear_limit
            self.oil_change_limit = oil_change_limit
            self.brake_service_limit = brake_service_limit
            
        def check_tire_wear(self):
            pass
        
        def check_oil_level(self):
            pass
        
        def check_brake_condition(self):
            pass
    
    class Car(Vehicle):
        def __init__(self, tire_wear_limit, oil_change_limit, brake_service_limit):
            super().__init__(tire_wear_limit, oil_change_limit, brake_service_limit)
        
        def check_tire_wear(self,car_tire_wear):
            if (car_tire_wear >= self.tire_wear_limit):
                return "Car tires need replacement"
            elif (car_tire_wear < self.tire_wear_limit):
                return " Car tires are in good condition"
                
        
        def check_oil_level(self,car_oil_level):
            if (car_oil_level < self.oil_change_limit):
                return "Car needs an oil change"
            elif(car_oil_level >= self.oil_change_limit):
                return "Car oil level is fine"
        
        def check_brake_condition(self,car_brake_condition):
            if (car_brake_condition < self.brake_service_limit):
                return "Car brakes require servicing"
            elif(car_brake_condition >= self.brake_service_limit):
                return "Car brakes are in good working condition"
            
            
            
    
    class Motorcycle(Vehicle):
        def __init__(self, tire_wear_limit, oil_change_limit, brake_service_limit):
            super().__init__(tire_wear_limit, oil_change_limit, brake_service_limit)
    
        
        def check_tire_wear(self,motorcycle_tire_wear):
            if(motorcycle_tire_wear >= self.tire_wear_limit):
                return "Motorcycle tires need replacement"
            elif(motorcycle_tire_wear < self.tire_wear_limit):
                return "Motorcycle tires are in good condition"
        
        def check_oil_level(self,motorcycle_oil_level):
            if(motorcycle_oil_level < self.oil_change_limit):
                return "Motorcycle needs an oil change"
            elif(motorcycle_oil_level >= self.oil_change_limit):
                return "Motorcycle oil level is fine"
        
        def check_brake_condition(self,motorcycle_brake_condition):
            if(motorcycle_brake_condition < self.brake_service_limit):
                return "Motorcycle brakes require servicing"
            elif(motorcycle_brake_condition >= self.brake_service_limit):
                return "Motorcycle brakes are in good working condition"
    # Do not change any code below.
    # Do not call this function anywhere.
    
    def main():
        car_tire_wear_limit = int(input())
        car_oil_change_limit = int(input())
        car_brake_service_limit = int(input())
        
        motorcycle_tire_wear_limit = int(input())
        motorcycle_oil_change_limit = int(input())
        motorcycle_brake_service_limit = int(input())
        
        car = Car(car_tire_wear_limit,car_oil_change_limit,car_brake_service_limit)
        motorcycle = Motorcycle(motorcycle_tire_wear_limit,motorcycle_oil_change_limit,motorcycle_brake_service_limit)
        
        car_tire_wear = int(input())
        car_oil_level = int(input())
        car_brake_condition= int(input())
        
        motorcycle_tire_wear = int(input())
        motorcycle_oil_level = int(input())
        motorcycle_brake_condition = int(input())
        
        print(car.check_tire_wear(car_tire_wear))
        print(car.check_oil_level(car_oil_level))
        print(car.check_brake_condition(car_brake_condition))
        print(motorcycle.check_tire_wear(motorcycle_tire_wear))
        print(motorcycle.check_oil_level(motorcycle_oil_level))
        print(motorcycle.check_brake_condition(motorcycle_brake_condition))
        
    main()
