plot_wordcloud(clean_user_wordcloud)
def plot_wordcloud(tokens):
    my_wordcloud = WordCloud().generate(tokens)
    plt.imshow(my_wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()
def get_token_name (token_result):
    token_name = ' '.join(token_result)
    return token_name
tokens_list=['clean_source_token_result2',
             'clean_hashtags_token_result2',
             'clean_text_token_result2',
             'clean_user_description_token_result2',
             'clean_user_location_token_result2',
             'clean_user_token_result2']
for token_list in tokens_list:
    #print(token_list)
    if token_list == 'clean_user_token_result2':
        clean_user_wordcloud = get_token_name(clean_user_token_result2)
    elif token_list == 'clean_user_location_token_result2':
        clean_user_location_wordcloud = get_token_name(clean_user_location_token_result2)
    elif token_list == 'clean_user_description_token_result2':
        clean_user_description_wordcloud = get_token_name(clean_user_description_token_result2)
    elif token_list == 'clean_text_token_result2':
        clean_text_wordcloud = get_token_name(clean_text_token_result2)   
    elif token_list == 'clean_hashtags_token_result2':
        clean_hashtags_wordcloud = get_token_name(clean_hashtags_token_result2)   
    elif token_list == 'clean_source_token_result2':
        clean_source_wordcloud = get_token_name(clean_source_token_result2)   
plot_wordcloud(clean_user_wordcloud)        
        
 
