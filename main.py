import src.api as api 
import re


def main():
  
    students=api.get_url().json()
    
   # students=api.get_pages_students()


    print(len(students))


if __name__=="__main__":
    main()