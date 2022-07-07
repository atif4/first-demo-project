data_dic = {'clean_user_name_most_common_token_result4':'MOST COMMON USERNAME',
            'clean_source_most_common_token_result4':'MOST COMMON USER SOURCE',
            'clean_user_description_most_common_token_result4':'MOST COMMON USER DESCRIPTION',
            'clean_hashtags_most_common_token_result4':'MOST COMMON USER HASHTAGS',
            'clean_text_most_common_token_result4':'MOST COMMON USER TEXT'}

def get_plot_seabone_graph (data,title):
    plt.figure(figsize=(20,10))
    plt.xticks(rotation =45)
    plt.title(title)
    plot_info = sns.barplot(x = 'words' , y = 'score' , data=data_dic)
    plt.show()
    return plot_info