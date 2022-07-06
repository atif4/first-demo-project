'''here i made a function to take all columns than remove
stopwords from that further convert them into list'''
def get_clean_list (new_column_name):
    clean_list = df[new_column_name].apply(nfx.remove_stopwords).tolist()
    return clean_list

# this is list in which each column is mentioned 

columns_list = ['cleaning_user_name',
                'cleaning_user_location',
                'cleaning_user_description',
                'cleaning_text',
                'cleaning_hashtags',
                'cleaning_source']

# this is the for loop in columns_list

for column_list in columns_list:

    # here i give some conditions for each columns 
    if column_list == 'cleaning_user_name':
        # here i call function get_clean_list in different variables
        clean_user_name_result1 = get_clean_list(column_list)
    elif column_list == 'cleaning_user_location':
        clean_user_loaction_result1 = get_clean_list(column_list)
    elif column_list == 'cleaning_user_description':
        clean_user_description_result1 = get_clean_list(column_list)
    elif column_list == 'cleaning_text':
        clean_text_result1 = get_clean_list(column_list)
    elif column_list == 'cleaning_hashtags':
        clean_hashtags_result1 = get_clean_list(column_list)
    elif column_list == 'cleaning_source':
        clean_source_result1 = get_clean_list(column_list)