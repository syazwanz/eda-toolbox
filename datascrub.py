def remove_char(df, col, char):
    df[col] = df[col].str.strip(char)


def cat2num(df, col):
    num_encode = {col : {'YES':1, 'NO':0}}  
    df.replace(num_encode, inplace=True)


def change_int_float(df, col_name, integer = True):
    if integer:
        df[col_name] = df[col_name].astype('int32')
    else:
        df[col_name] = df[col_name].astype('float32')


def missing_data(df):
    return df.isnull().sum().sort_values(ascending=False)


def concat_col_condition(df, col1, col2, char, col_replace = False):
    mask = df[col1].str.endswith(char, na=False)
    col_new = df[mask][col1] + df[mask][col2]
    col_new.replace(char, ' ', regex=True, inplace=True)
    
    if col_replace:
        df[col1] = col_new
    else:
        df['col_new'] = col_new


def drop_col(df, col_names_list): 
    df.drop(col_names_list, axis=1, inplace=True)
