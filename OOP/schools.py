#plan for this project:
#Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (integer)
#Getters: all properties have getters
#Setters: the numberOfStudents property has a setter
#Methods: A __repr__ method that displays information about the school.
#Primary School
#Includes everything in the School class, plus one additional property
#Properties: pickupPolicy (string, like "Pickup after 3pm")
#Middle School
#Does not include any additional properties or methods
#High School
#Includes everything in the School class, plus one additional property
#Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])

#parent class
class School:
  #let's define our constructor
  def __init__(self, name, level, numberOfStudents) :
    #define our three properties
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents


  def get_name(self) :
    return self.name

  def get_level(self) :
    return self.level

  def get_numberOfStudents(self) :
    return self.numberOfStudents 

#create our setter for number of students
  def set_numberOfStudents(self, newnumberOfStudents):
    #just set it to whatever is passed in
    self.numberOfStudents = newnumberOfStudents

  def set_level(self, newlevel) :
    self.level = newlevel 

  def set_name(self, newname) :
    self.name = newname

#this method mean that: whenever school is printed, we get some relevant info abt the object.
  def __repr__(self) :
    return "A {level} school, named {name} , with {numberOfStudents} students!".format(level = self.level, name = self.name, numberOfStudents = self.numberOfStudents)
  
    
##testing

#School1 = School("Generic School", "secondary", 130)
#print(School.get_name(School1))
#School.set_name(School1, "my school")
#print(School.get_name(School1))


#now time for our primary school class, that inherits from the school class
class PrimarySchool(School) :
  #initialize with one extra property
  def __init__(self, name, numberOfStudents, pickupPolicy) :
    #we'll pass 'super()' any arguments that the parent constructor uses. allows us to access base methods of parent class
    super().__init__(name, "primary", numberOfStudents) 
    self.pickupPolicy = pickupPolicy 
    
  #since we've inherited all the other methods, we just need to make one new getter
  def get_pickupPolicy(self):
    return self.pickupPolicy

#now we override the repr method so that when primary school is printed, we get info on the pickup policy and the other properties.
  def __repr__(self) :
    rep = super().__repr__()
    return rep + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

#testing
#School2 = PrimarySchool("Potters Gate", 130, "diy")
#print(PrimarySchool.get_name(School2))
#repr(School2)

class Highschool(School) :

  def __init__(self, name, numberOfStudents, sportsTeams) :
    #same as for primary
    super().__init__(name, "High school", numberOfStudents) 
    self.sportsTeams = sportsTeams 

  def get_sportsTeams(self) :
    return self.sportsTeams 

  def __repr__(self) :
    repres = super().__repr__()
    return repres + "The sports teams are {sportsTeams}".format(sportsTeams = self.sportsTeams)


#testing:
School3 = Highschool("Newman", 130, "diy")
print(Highschool.get_name(School3))
print(School3) #this will call our repr method
  
