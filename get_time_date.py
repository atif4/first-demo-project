import datetime

def get_time_date(column_name,new_column_name_year,
                  new_column_name_month,
                  new_column_name_day,
                  new_column_name_hour,
                  new_column_name_minute,
                  new_column_name_second):
    
    #it is in object type to convert into datetime 
    df[column_name] = pd.to_datetime(df[column_name])
    df[new_column_name_year]=df[column_name].dt.year
    df[new_column_name_month]=df[column_name].dt.month
    df[new_column_name_day]=df[column_name].dt.day
    df[new_column_name_hour]=df[column_name].dt.hour
    df[new_column_name_minute]=df[column_name].dt.minute
    df[new_column_name_second]=df[column_name].dt.second
    
get_time_date(column_name = 'user_created',
              new_column_name_year = 'years',
              new_column_name_month = 'months',
              new_column_name_day = 'days',
              new_column_name_hour='hours',
              new_column_name_minute='minutes',
              new_column_name_second='seconds')