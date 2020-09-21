import src.api as api 


def main():
data=get_url(i=1).json()
students = [get_students(data,i=j) for j in range(2,len(data))]


print('Loading page 1')

i=2
while len(re.findall('last',response.headers['link']))==0:
    try:
        print(f'Loading page {i+1}')
        data=get_url(i).json()
        students.append(students = [get_students(data,i=j) for j in range(i,len(data))])
        i+=1
        
    except ValueError:
        break


print(students)

"""
if __name__=="__main__":
    main()