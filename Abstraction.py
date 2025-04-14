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

#

