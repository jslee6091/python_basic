class MyClass(object):
    def __init__(self):
        self.num = 10
        # private attribute
        self.__name = 'lowry'

    def read_number(self):
        print('hahaha', self.num)

    def __str__(self):
        return str(self.num)

    # getter method
    @property
    def name(self):
        return self.__name

    # setter method
    @name.setter
    def name(self, new_name):
        if new_name != 'we':
            self.__name = new_name
        else:
            print('you should not input the name \'we\'')


# this is error
# print(myobj.__name)
myobj = MyClass()
print(myobj)
myobj.read_number()

# getter method call
print(myobj.name)

# setter method call
myobj.name = 'we'
print(myobj.name)
