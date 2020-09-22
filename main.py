import src.data_exportation as export
import src.api_gen as gen


def main():
  
   students=export.get_pull_requests(i=1).json()

   #students=export.get_pages_students()
   
   students_toMongo=[]

   #for i in range(0,len(students)):
   for i in range(0,3):
        students_toMongo.append(export.get_student(students,i=i))

   #export.export_json(students_toMongo)
   
   for student in students_toMongo:
        gen.createStudent(student)


if __name__=="__main__":
    main()