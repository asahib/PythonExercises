class Student:
  def __init__(self,name,student_id):
    self.name = name
    self.student_id = student_id
    self.totalcredits = 0
    self.gradepoints = 0
    self.gpa = 0
    self.classStanding = 'Freshman'
  
  def calculateClassStanding(self):
    if self.totalcredits < 30:
      self.classStanding = 'Freshman'
    elif self.totalcredits < 60:
      self.classStanding = 'Sophomore'
    elif self.totalcredits < 90:
      self.classStanding = 'Junior'
    elif self.totalcredits < 120:
      self.classStanding = 'Senior'
    else:
      self.classStanding = 'Graduated'
  
  def getClassCreditsAndGrade(self):
    print(f"Please enter the Class credits and grades for {self.name}")
    while True:
      classname = input("\nPlease enter the class name : ")
      classcredit = int(input(f"Please enter the Credits for {self.name} in {classname}: "))
      classgrade = (input(f"Please enter the grades for {self.name} in {classname} (A - F) : "))
      classgrade = classgrade.lower()
      if classgrade == 'a':
        self.gradepoints += (classcredit * 4)
      elif classgrade == 'b':
        self.gradepoints += (classcredit * 3)
      elif classgrade == 'c':
        self.gradepoints += (classcredit * 2)
      elif classgrade == 'd':
        self.gradepoints += (classcredit * 1)
      self.totalcredits += classcredit 
      Yes_Or_No = input("Please enter 'Y' if you want to add another class with grade and credit : ").lower()
      if Yes_Or_No != 'y' :
        break
    self.gpa = self.gradepoints/self.totalcredits
    self.calculateClassStanding()
  
  def __repr__(self):
    temp_str = f'\n {self.name} is a {self.classStanding} with GPA of {self.gpa} \n Total Credits : {self.totalcredits} \n Total Grade Points:{self.gradepoints}  '
    return temp_str

# class 
  
def main():
  student1 = Student("Azhar","001")
  student1.getClassCreditsAndGrade()
  
  print(student1)

if __name__ == '__main__':
  main()

  
