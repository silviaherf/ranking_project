import src.api as api 


def main():
    response=api.get_pr()

    print('Loading page 1')

    
    
    i=2
    while len(re.findall('last',response.headers['link']))==0:
        try:
            print(f'Loading page {i+1}')
            reviews=reviews.append(api.api_to_df(api.get_pr(args,i=i))).reset_index()
            i+=1
        except ValueError:
            break


"""
if __name__=="__main__":
    main()