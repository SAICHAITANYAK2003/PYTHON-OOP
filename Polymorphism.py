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

