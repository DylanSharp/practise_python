from peewee import *

db = SqliteDatabase('students.db')


class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

students = [
    {"username": "dylsharp",
     "points": 48452},
    {"username": "martmey",
     "points": 59423},
    {"username": "soloshni",
     "points": 14854},
    {"username": "stinjus",
     "points": 65297},
    {"username": "malcdawg",
     "points": 25478}
]

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                          points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])  #Get the student object that already exists
            student_record.points = student['points']  # Update the points in the student object with the current value (may or may not have changed - one could check for this first)
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()  # Get all students and the sort and the just "get" the first one.
    return student

if __name__ == '__main__':  #If file is run directly and not imported
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("Our top student right now is {0.username}".format(top_student()))