import json
from database import db 



def main():

    students_dict={}

    with open('students.json') as students:
        students_dict=json.load(students)

    result = db.students.insert_many(students_dict)

    print('Students insertion to MongoDB done')


    labs_dict={}

    with open('labs.json') as labs:
        labs_dict=json.load(labs)

    result = db.labs.insert_many(labs_dict)
    print('Labs insertion to MongoDB done')



if __name__=="__main__":
    main()

