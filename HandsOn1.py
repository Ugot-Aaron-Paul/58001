class Person:
    def __init__(self, student, pre, mid, fin):
        self.student = student
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def Grade(self):
        return (self.__pre + self.__mid + self.__fin) / 3

    def display(self):
        print(f"{self.student} have {self.__pre} for prelims, {self.__mid} for midterms, and {self.__fin} for finals with an avererage of {self.Grade()}")


class std1(Person):
    def __init__(self):
        student = "Student 1"
        print(f"{student} Grades:")
        pre = float(input("prelim: "))
        mid = float(input("midterm: "))
        fin = float(input("final: "))
        super().__init__(student, pre, mid, fin)


class std2(Person):
    def __init__(self):
        student = "Student 2"
        print(f"{student} Grades:")
        pre = float(input("prelim: "))
        mid = float(input("midterm: "))
        fin = float(input("final: "))
        super().__init__(student, pre, mid, fin)


class std3(Person):
    def __init__(self):
        student = "Student 3"
        print(f"{student} Grades:")
        pre = float(input("prelim: "))
        mid = float(input("midterm: "))
        fin = float(input("final: "))
        super().__init__(student, pre, mid, fin)


Std1 = std1()
Std2 = std2()
Std3 = std3()

Std1.display()
Std2.display()
Std3.display()
