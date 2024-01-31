class Student:
    def __init__(self,name,roll,age):
        self.name = name
        self._roll = roll
        self.__age = age

    def display_public_method(self):
        print(f'public member--{self.name}')

    def _diplay_protect_method(self):
        print(f'protect member calling--{self._roll}')

    def __display_private_method(self):
        print(f'private member called -- {self.__age}')

    def private_attr(self):
        self.__display_private_method()


class Subclass(Student):
    def display_details(self):
        _diplay_protect_method()

def fib(n):
    f = [0]*n
    f[1] = 1
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f

print(fib(5))
