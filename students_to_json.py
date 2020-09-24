import src.data_exportation as export
import src.api_gen as gen



def main():
  

   students,labs=export.get_pages_students_labs()
   
   export.export_json(students,'students')
 

   export.export_json(labs,'labs')


if __name__=="__main__":
    main()
    