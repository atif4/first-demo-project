def get_token (function_name):
    # here i made nested for loop to get token by splitting each sentence and save them in the variable
    tokens = [token for line in function_name for token in line.split()]
    return tokens

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
        # here i call function get_token in different variables
        clean_user_token_result2 =  get_token(get_clean_list(column_list))
    elif column_list == 'cleaning_user_location':
        clean_user_location_token_result2 = get_token(get_clean_list(column_list))
    elif column_list == 'cleaning_user_description':
        clean_user_description_token_result2 = get_token(get_clean_list(column_list))
    elif column_list == 'cleaning_text':
        clean_text_token_result2 = get_token(get_clean_list(column_list))
    elif column_list == 'cleaning_hashtags':
        clean_hashtags_token_result2 = get_token(get_clean_list(column_list))
    elif column_list == 'cleaning_source':
        clean_source_token_result2 = get_token(get_clean_list(column_list))