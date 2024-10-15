class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender= gender
    def introduce(self):
        print(f"hello, my name is {self.name}, I am {self.age} years old, and I am a {self.gender}")
        
Person1 = Person("brandon",19,"male")
Person1.introduce()
        
    
