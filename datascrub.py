def remove_col_white_space(df,col):
    df[col] = df[col].str.lstrip()

def convert_cat2num(col, df):
    num_encode = {col : {1:'YES', 0:'NO'},
                  'col_2'  : {'WON':1, 'LOSE':0, 'DRAW':0}}  
    df.replace(num_encode, inplace=True)

def change_dtypes(col_int, col_float, df): 
    df[col_int] = df[col_int].astype('int32')
    df[col_float] = df[col_float].astype('float32')

def check_missing_data(df):
    return df.isnull().sum().sort_values(ascending=False)

def concat_col_str_condition(df):
    # concat 2 columns with strings if the last 3 letters of the first column are 'pil'
    mask = df['col_1'].str.endswith('pil', na=False)
    col_new = df[mask]['col_1'] + df[mask]['col_2']
    col_new.replace('pil', ' ', regex=True, inplace=True)  # replace the 'pil' with emtpy space

def convert_str_datetime(df): 
    df.insert(loc=2, column='timestamp', value=pd.to_datetime(df.transdate, format='%Y-%m-%d %H:%M:%S.%f'))

def drop_col(col_names_list, df): 
    df.drop(col_names_list, axis=1, inplace=True)
    return df
