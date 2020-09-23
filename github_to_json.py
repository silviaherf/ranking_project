import src.data_exportation as export
import src.api_gen as gen



def main():
  

   students=export.get_pages_students()
   
   export.export_json(students,'students')



   labs=export.get_pages_labs()
   

   export.export_json(labs,'labs')




   """
   for student in students_toMongo:
       studentname=student['name']
       #gen.createStudent(name)
       #export.student_toMongo(studentname)
    """

if __name__=="__main__":
    main()
    