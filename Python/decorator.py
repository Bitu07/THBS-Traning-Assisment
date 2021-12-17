class Employee:

    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.email = self.fname + "." + self.lname + "@gmail.com"
        self.name =  self.fname + " " + self.lname

    # @property
    # def email(self):
    #     return "{}.{}@gmail.com".format(self.fname,self.lname)

    @name.setter
    def name(self,name):
        f

    @name.deleter
    def name(self):
        self.fname=None
        self.lname=None

emp1 = Employee("abhishek","yadav")
emp1.lname='singh'
print(emp1.email)
# print(emp1.name)