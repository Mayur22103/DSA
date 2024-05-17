class Test:
    z=5
    def __init__(self,a,b):
        self.x=a
        self.y=b
        
    def show(self):
        print(self.x,self.y)

    @staticmethod
    def f2():
       print("hello")

    @classmethod
    def f3(cls):
        print(cls.z)


t1 = Test(14,17)
t1.show()
Test.f3()
Test.f2()


class Emp :
    def __init__(self,empId,empName,empAge):
        self.empId = empId
        self.empName = empName
        self.empAge = empAge
    
    def getData(self): 
        return self.empId,self.empName,self.empAge
    
t2 = Emp(1,"Mayur",22)
print(t2.getData())

    


