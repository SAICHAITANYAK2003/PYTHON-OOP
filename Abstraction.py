#SHAPES:
        # Implement the Shape, Circle and Rectangle classes appropriately
        from abc import ABC,abstractmethod
        
        class Shape(ABC):
            @abstractmethod
            def calculate_area(self):
                pass
            
            @abstractmethod
            def calculate_perimeter(self):
                pass
        
        class Circle:
            def __init__(self, radius):
                self.radius = radius
            
            def calculate_area(self):
                circle_radius=3.14*self.radius*self.radius
                return round(circle_radius,2)
            
            def calculate_perimeter(self):
                circle_perimeter = 2*3.14*self.radius
                return round(circle_perimeter,2)
        
        class Rectangle:
            def __init__(self, length, breadth):
                self.length = length
                self.breadth = breadth
                
            def calculate_area(self):
                rectangle_radius=self.length*self.breadth
                return round(rectangle_radius,2)
            
            def calculate_perimeter(self):
                reactangle_perimeter = 2*(self.length + self.breadth)
                return round(reactangle_perimeter,2)
        
        
                
        # Do not change any code below.
        # Do not call this function anywhere.
        
        def main():
            radius = input()
            length = int(input())
            breadth = int(input())
            
            circle = Circle(int(radius))
            print(circle.calculate_area())
            print(circle.calculate_perimeter())
            
            rectangle = Rectangle(int(length), int(breadth))
            print(rectangle.calculate_area())
            print(rectangle.calculate_perimeter())
        
        main()

#Employee:

      # Implement the Employee, PartTimeEmployee and FullTimeEmployee classes appropriately
      from abc import ABC,abstractmethod
      class Employee(ABC):
          def __init__(self, employee_id, name, email, department):
              self.employee_id = employee_id
              self.name = name
              self.email = email
              self.department = department
          
          @abstractmethod
          def calculate_salary(self):
              pass
      
      class PartTimeEmployee(Employee):
          def __init__(self, employee_id, name, email, department, hourly_rate):
              super().__init__(employee_id, name, email, department)
              self.hourly_rate = hourly_rate
              self.total_hours_worked = 0
          
          
          
          def update_hours(self,part_time_employee_worked_hours):
              self.total_hours_worked += part_time_employee_worked_hours
          
          def calculate_salary(self):
              salary  = self.hourly_rate*self.total_hours_worked
              return salary
              
          
          
      
      
      class FullTimeEmployee(Employee):
          def __init__(self, employee_id, name, email, department, annual_salary):
              super().__init__(employee_id, name, email, department)
              self.annual_salary = annual_salary
          
          def give_raise(self,full_time_employee_raise):
              self.annual_salary += full_time_employee_raise
          
          def calculate_salary(self):
              return self.annual_salary
      
      
      # Do not change any code below.
      # Do not call this function anywhere.
      
      def main():
          part_time_employee_id = input()
          part_time_employee_name = input()
          part_time_employee_email = input()
          part_time_employee_department = input()
          part_time_employee_hourly_rate = int(input())
          part_time_employee_worked_hours = int(input())
          full_time_employee_id = input()
          full_time_employee_name = input()
          full_time_employee_email = input()
          full_time_employee_department = input()
          full_time_employee_annual_salary = int(input())
          full_time_employee_raise = int(input())
          
          part_time_emp = PartTimeEmployee(part_time_employee_id, part_time_employee_name, 
                          part_time_employee_email, part_time_employee_department, 
                          part_time_employee_hourly_rate)
          part_time_emp.update_hours(part_time_employee_worked_hours)
          print(part_time_emp.calculate_salary())
      
          full_time_emp = FullTimeEmployee(full_time_employee_id, full_time_employee_name, 
                          full_time_employee_email, full_time_employee_department, 
                          full_time_employee_annual_salary)
          full_time_emp.give_raise(full_time_employee_raise)
          print(full_time_emp.calculate_salary())
      
      
      main()

#Appliance:

                # Implement the Appliance, WashingMachine and Refrigerator classes appropriately
                from abc import ABC,abstractmethod
                
                
                class Appliance(ABC):
                    
                    @abstractmethod
                    def switch_on(self):
                        pass
                    
                    @abstractmethod
                    def switch_off(self):
                        pass
                
                class WashingMachine(Appliance):
                    def __init__(self, load_capacity):
                        self.load_capacity = load_capacity
                        self.current_load = 0
                        self.is_operating = False
                        
                    def switch_on(self):
                        if(self.is_operating) :
                            return "Washing Machine is already switched on"
                        elif(self.current_load ==0):
                                return "Add clothes to start the machine"
                        else:
                                self.is_operating = True
                            
                            
                    
                    def switch_off(self):
                        if(self.is_operating):
                            self.is_operating = False
                        else:
                            return "Washing Machine is already switched off"
                    
                    def add_clothes(self,num_clothes):
                        if(num_clothes > self.load_capacity):
                            return "Exceeds load capacity"
                        
                        if( num_clothes > 0):
                            self.current_load = num_clothes
                        
                        if(num_clothes <= 0):
                            return "Cannot add zero or negative number of clothes"
                    
                    def remove_clothes(self):
                        if(self.current_load > 0):
                            self.current_load = 0
                        else:
                            return "No clothes to remove"
                
                class Refrigerator:
                    def __init__(self, temperature):
                        self.temperature = temperature
                        self.is_operating = False
                        
                    def switch_on(self):
                        if(self.is_operating):
                            return "Refrigerator is already switched on"
                            
                        else:
                            self.is_operating = True
                            
                    
                    def switch_off(self):
                        if(self.is_operating):
                            self.is_operating = False
                        else:
                            return "Refrigerator is already switched off"
                    
                    def adjust_temperature(self,new_temperature):
                        self.temperature = new_temperature
                
                # Do not change any code below.
                # Do not call this function anywhere.
                
                def main():
                    list = input()
                    input_list = list.split(",")
                
                    load_capacity = int(input())
                    initial_temperature = int(input())
                        
                    washing_machine = WashingMachine(load_capacity)
                    refrigerator = Refrigerator(initial_temperature)
                
                    wm_operations = {
                        'add_clothes': lambda num_clothes: print(washing_machine.add_clothes(num_clothes)) if washing_machine.add_clothes(num_clothes) is not None else None,
                        'switch_on': lambda: print(washing_machine.switch_on()) if washing_machine.switch_on() is not None else None,
                        'switch_off': lambda: print(washing_machine.switch_off()) if washing_machine.switch_off() is not None else None,
                        'remove_clothes': lambda: print(washing_machine.remove_clothes()) if washing_machine.remove_clothes() is not None else None
                    }
                
                    fridge_operations = {
                        'adjust_temperature': lambda: print(refrigerator.adjust_temperature(new_temperature)) if refrigerator.adjust_temperature(new_temperature) is not None else None,
                        'switch_on': lambda: print(refrigerator.switch_on()) if refrigerator.switch_on() is not None else None,
                        'switch_off': lambda: print(refrigerator.switch_off()) if refrigerator.switch_off() is not None else None
                    }
                
                    for operation in input_list[:4]:
                        if 'add_clothes' in operation:
                            _, num_clothes = operation.split()
                            wm_operations['add_clothes'](int(num_clothes))
                        elif operation in wm_operations:
                            wm_operations[operation]()
                    for operation in input_list[5:]:
                        if 'adjust_temperature' in operation:
                            _, new_temperature = operation.split()
                            fridge_operations['adjust_temperature'](int(new_temperature))
                        elif operation in wm_operations:
                            fridge_operations[operation]()
                
                
                main()


