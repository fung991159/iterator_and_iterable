#a property decorator turns a class method into a property.
#a setter can change a instance attributes, invoked whenever the attribute were assigned a new value
#a deleter can delete a instance attributes, invoked whenever the attribute were deleted

class Person:
    def __init__(self):
        self.first = 'John'
        self.last = 'Doe'
        self.age = '20'
        self.hobby = 'Jogging'

    def jogging(self):
        return 'Yes let\'s go!'

    def reading(self):
        return 'no this is so boring'

    @property
    def fav_food(self):
        self.food = 'yogurt'
        return self.food

    @property
    def summary(self):
        return f'{self.first} {self.last} is age {self.age} and like {self.hobby}'

    @summary.setter
    def summary(self, new_name):
        first, last = new_name.split(' ')
        self.first = first
        self.last = last

    @summary.deleter
    def summary(self):
        print('Person\'s name has been deleted!')
        self.first = None
        self.last = None

p = Person()

#testing property decorator
print(p.summary) #John Doe is age 20 and like Jogging

#testing setter
p.summary = 'Fung Yeung'
print(p.summary) #Fung Yeung is age 20 and like Jogging
print(p.first, p.last, sep='|') #Fung|Yeung

#testing deleter
del p.summary    #Person's name has been deleted!
print(p.summary) #None None is age 20 and like Jogging