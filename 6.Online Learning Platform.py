from abc import ABC, abstractmethod
class Course(ABC):
    def __init__(self,name,duration):
        self.name=name
        self.duration=duration
    @abstractmethod
    def course_details(self):
        pass
class ProgrammingCourse(Course):
    def course_details(self):
        print(self.name,self.duration,"Programming Course")
class DesignCourse(Course):
    def course_details(self):
        print(self.name,self.duration,"Design Course")
class MarketingCourse(Course):
    def course_details(self):
        print(self.name,self.duration,"Marketing Course")
p=ProgrammingCourse("Python","3 Months")
d=DesignCourse("UI","2 Months")
m=MarketingCourse("Digital","1 Month")
p.course_details()
d.course_details()
m.course_details()