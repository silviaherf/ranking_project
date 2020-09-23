import src.data_exportation as export
import src.api_gen as gen



def main():
  
   #data=export.get_pull_requests(i=1).json()

   students=export.get_pages_students()
   
   students_toMongo=[]

   for i in range(0,len(students)):
        students_toMongo.append(export.get_student(data,i=i))

   export.export_json(students_toMongo)


   labs=export.get_pages_labs()
   
   labs_toMongo=[]

   for i in range(0,len(students)):
        labs_toMongo.append(export.get_lab(data,i=i))

   export.export_json(labs_toMongo)




   """
   for student in students_toMongo:
       studentname=student['name']
       #gen.createStudent(name)
       #export.student_toMongo(studentname)
    """

if __name__=="__main__":
    main()
    