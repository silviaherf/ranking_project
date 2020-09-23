import src.data_exportation as export
import src.api_gen as gen



def main():
  

   students=export.get_pages_students()
   
   export.export_json(students,'students')



   labs=export.get_pages_labs()
   

   export.export_json(labs,'labs')


if __name__=="__main__":
    main()
    