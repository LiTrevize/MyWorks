class Course:
    def __init__(self, rank, name, credit, score):
        self.rank=rank
        self.name=name
        self.credit=credit
        self.score=score
        self.gpa=-1
    def getgpa(self):
        if 95<=self.score<=100:
            self.gpa=4.3
        elif 90<=self.score<95:
            self.gpa=4.0
        elif 85 <= self.score < 90:
            self.gpa=3.7
        elif 80 <= self.score < 85:
            self.gpa=3.3
        elif 75 <= self.score < 80:
            self.gpa=3.0
        elif 70 <= self.score < 75:
            self.gpa=2.7
        elif 67 <= self.score < 70:
            self.gpa=2.3
        elif 65 <= self.score < 67:
            self.gpa=2.0
        elif 62 <= self.score < 65:
            self.gpa=1.7
        elif 60 <= self.score < 62:
            self.gpa=1.0
        else:
            self.gpa=0
        return self.gpa
class AllCourses:
    def __init__(self):
        self.courses=[]
        self.majorgpa=-1
        self.compulsorygpa=-1
        self.overallgpa=-1
    def add(self,course):
        self.courses.append(course)
        course.getgpa()
    def getmajor(self):
        weighed=0
        credit = 0
        for course in self.courses:
            if course.rank==2:
                weighed+=course.credit*course.gpa
                credit+=course.credit
        self.majorgpa=weighed/credit
        return self.majorgpa
    def getcompulsory(self):
        weighed=0
        credit = 0
        for course in self.courses:
            if course.rank==1 or course.rank==2:
                weighed+=course.credit*course.gpa
                credit+=course.credit
        self.compulsorygpa=weighed/credit
        return self.compulsorygpa
    def getoverall(self):
        weighed=0
        credit = 0
        for course in self.courses:
            weighed+=course.credit*course.gpa
            credit+=course.credit
        self.overallgpa=weighed/credit
        return self.overallgpa
def print_rank(rank):
    if int(rank)==0:
        return "optional"
    elif int(rank)==1:
        return "compulsory"
    elif int(rank)==2:
        return "major"
def main():
    print("Grade Management System")
    semester=AllCourses()
    try:
        f=open("grade.txt","r")
        print("Existed records:")
        print("{:^10}{:^16}{:^7}{:^7}{:^7}".format("Rank","Name","Credit","Score","GPA"))
        while True:
            line=f.readline().strip()
            if len(line)==0:
                break
            rank, name, credit, score = line.split()
            new=Course(int(rank),name,int(credit),int(score))
            semester.add(new)
            print("{:^10}{:^16}{:^7}{:^7}{:^7}".format(print_rank(rank),name,credit,score,round(new.gpa,3)))
        f.close()
        f=open("grade.txt",'a')
    except:
        f=open("grade.txt","w")
        print("No existed records.")
    while True:
        s=input()
        if s=="":
            break
        rank,name,credit,score=s.split()
        semester.add(Course(int(rank),name,int(credit),int(score)))
        f.write("{} {} {} {}\n".format(rank,name,credit,score))
    print("{:^20}{:.3f}".format("Major GPA",semester.getmajor()))
    print("{:^20}{:.3f}".format("Compulsory GPA", semester.getcompulsory()))
    print("{:^20}{:.3f}".format("Overall GPA", semester.getoverall()))
    f.close()


main()