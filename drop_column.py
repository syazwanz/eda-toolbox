def drop_col(col_names_list, df): 
    df.drop(col_names_list, axis=1, inplace=True)
    return df
