class Person:
    
    # Class Variable
    total_person = 0
    
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        self.university = kwargs['university']
        
        Person.total_person +=1
        
    def __str__(self):
        return self.name # TODO
    
    # De Constructor
    def __del__(self):
        Person.total_person -= 1
        print("Objected Deleted")


x = Person("Sazzad",18,university="IUBAT")
y = Person("Hossain",20,university="IUBAT")
print("Person Name: ", x.name)
print("Person Age: ", x.age)
print("Person University: ", x.university)

print("Total Person: ", Person.total_person)

del y
print("Total Person: ", Person.total_person)

# del Person
