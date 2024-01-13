class Person:
    
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        self.university = kwargs['university']
        
        
    def __str__(self, *args, **kwargs):
        
        text = f"Name: {self.name}, Age: {self.age}, "
        
        if kwargs:
            
            for key, value in kwargs.items():
                text += "{0}: {1},".format(key,value)
        
        # # any(key in kwargs for key in kwargs) check that any key present in the keywords or not
        # if kwargs is not None and any(key in kwargs for key in kwargs):
        #     return f"Name: {self.name}, Age: {self.age}, Designation: {kwargs['designation']},"
            
        # return f"Name: {self.name}, Age: {self.age}"
        
        return text
    

class Worker(Person):
    
    def __init__(self, name, age, salary,*args, **kwargs):
        super().__init__(name, age, *args, **kwargs)
        self.salary = salary
    
    def CalculateSalary(self):
        return self.salary * 12
    
    def __str__(self, *args, **kwargs):
        text = super(Worker,self).__str__(designation = "Engineer", work_area = "Dhaka")
        text += " Salary: {}".format(self.salary)
        return text



worker1= Worker("Sazzad", 18, 25000, university='Dhaka')
print(worker1)
print("Name: ", worker1.name)
print("Salary: ", worker1.salary)
print("Yearly Salary: ", worker1.CalculateSalary())