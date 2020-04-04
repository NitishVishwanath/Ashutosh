class Employee:
    def __init__(self, name, id, age, gender):
        self.name= name
        self.id= id
        self.age= age
        self.gender= gender

class Organisation:
    def __init__(self, OrgName, employees):
        self.OrgName= OrgName
        self.employees= employees

    def addEmployee(self,name, id, age, gender):
        object= Employee(name, id, age, gender)
        self.employees.append(object)

    def getEmployeecount(self):
        return len(self.employees)

    def findEmployeeAge(self, id):
        for i in range(len(self.employees)):
            if self.employees[i].id==id:
                a = True
                return self.employees[i].age
            else:
                a=False

        if a==False:
            return -1
    def countEmployees(self, age):
        count=0
        for i in range(len(self.employees)):
            if self.employees[i].age>=age:
                count+=1
            return count

if __name__=='__main__':
    employees=[]
    o = Organisation('XYZ',employees)
    n=int(input())
    for i in range(n):
        name= input()
        id= int(input())
        age= int(input())
        gender= input()
        o.addEmployee(name, id, age, gender)

    id= int(input())
    age= int(input())
    print(o.getEmployeecount())
    print(o.findEmployeeAge(id))
    print(o.countEmployees(age))
