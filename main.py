import src.data_exportation as export


def main():
  
   # students=export.get_url().json()

   # students=export.get_pages_students()

    
   data=export.get_url(i=1).json()
   export.get_student(data,i=0)
   

    


if __name__=="__main__":
    main()