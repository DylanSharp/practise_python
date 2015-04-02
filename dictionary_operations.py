teachers = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
            'Kenneth Love': ['Python Basics', 'Python Collections']}


def most_classes(teachers):
    max_count = 0
    most_classes = ""
    for teacher in teachers:
        cnt = len(teachers[teacher])
        if cnt > max_count:
            max_count = cnt
            most_classes = teacher
    print("most_classes:\n" + most_classes + " has " + str(max_count) + " classes.\n")
    return most_classes

def num_teachers(teachers):
    print("num_teachers:\n" + str(len(teachers)) + "\n")
    return len(teachers)

def stats(teachers):
    statistics = []

    for teacher in teachers:
        classes = len(teachers[teacher])
        teach = [teacher, classes]
        statistics.append(teach)
    print("stats:\n" + str(statistics) + "\n")
    return statistics

def courses(teachers):
    courses = []

    for teacher in teachers:
        courses += (teachers[teacher])
    print("courses:\n" + str(courses) + "\n")
    return courses


most_classes(teachers)
num_teachers(teachers)
stats(teachers)
courses(teachers)