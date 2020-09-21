import src.api as api 
import re


def main():
    print('Loading page 1')
    data=api.get_url(i=1).json()
    students = [api.get_student(data,i=j) for j in range(0,len(data))]

    i=2
    """revisar regex
    num=re.findall(r'\d{2}\>\;\srel="last"',response.headers['link'])
    for i in range(0,num):
        try:
            print(f'Loading page {i-1}')
            data=api.get_url(i=i).json()
            students.append(students = [api.get_student(data,i=j) for j in range(0,len(data))])
            i+=1
            
        except ValueError:
            raise ValueError

"""
    print(len(students))


if __name__=="__main__":
    main()