import src.api as api 

def main():
    response=api.get_pr()

    print('Loading page 1')

    """
    reviews=api.api_to_df(response)
    i=1
    while response['has_more']==True:
        try:
            print(f'Loading page {i+1}')
            reviews=reviews.append(api.api_to_df(api.get_pr(args,i=i))).reset_index()
            i+=1
        except ValueError:
            break


"""
if __name__=="__main__":
    main()