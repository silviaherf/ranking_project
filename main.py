import src.data_exportation as export


def main():
  
    students=export.get_url().json()

   # students=api.get_pages_students()

    export.get_student(students)
    
    


if __name__=="__main__":
    main()