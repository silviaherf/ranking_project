import src.data_exportation as export


def main():
  
   students=export.get_pull_requests(i=1).json()

   #students=export.get_pages_students()
   
   students_toMongo=[]
   #for i in range(0,len(students)):
    #   students_toMongo.append(export.get_student(students,i=i))

   students_toMongo.append(export.get_student(students,i=5))
   export.export_json(students_toMongo)

    


if __name__=="__main__":
    main()