# object oriented programming

class employee:
    empno = 102
    salary =12345
    grade = 'A'
    
    def __init__(self,a,b,c):
        self.empno = a
        self.salary = b
        self.grade = c
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)
    def __del__(self):
        print("bye destuctrur called")

obj = employee(101,12000,"b")
obj.show()
obj2 = employee(102,23000,'c')
obj.show()

