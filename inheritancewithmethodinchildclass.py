class person:
  def __init__(self,name,age,lname):
    self.name=name
    self.age=age
    self.lname=lname

    
  def poor(self):
    print("my name is "+self.name+" "+self.lname)

class child(person):
  def __init__(self,name,age,lname):
    person.__init__(self,name,age,lname)
  
p1= person("ali",22,"ahsan")
p1.poor()
x=child("moiz",12,"abc")
print(x.name,x.lname)
print(x.age)
print(x.lname)
x.poor()

  
  

  