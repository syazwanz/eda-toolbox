def convert_cat2num(col, df):
    # Convert categorical variable to numerical variable
    num_encode = {col : {1:'YES', 0:'NO'},
                  'col_2'  : {'WON':1, 'LOSE':0, 'DRAW':0}}  
    df.replace(num_encode, inplace=True)  
