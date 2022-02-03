import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#functions:
#----------
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input('Plese choose the city which you want analyze:\n'
                     'choose from (chicago , new york city ,washington)\n')
        if city.lower() in ['chicago', 'new york city', 'washington']:
            city = city.lower()
            break
        else:
            print('Sorry, you Enter invalid City, Try again, please')
    
    while True:
        # get user input for month (all, january, february, ... , june)
        month = input('Plese choose the month which you want analyze:\n'
                     'choose a month from january to june or all \n')
        if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            month = month.title()
            break
        else:
            print('Sorry, you Enter invalid input, Try again, please')
    
    while True:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input('Plese choose the day in the week which you want analyze:\n'
                     'choose a day from monday to sunday or all \n')
        if day.lower() in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            day = day.title()
            break
        else:
            print('Sorry, you Enter invalid input, Try again, please')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):    # recomment this fuction cause comment are coppied form prob3
    """
    Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    name = CITY_DATA[city]
    df = pd.read_csv(name)
    df.fillna(method='ffill',inplace=True)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # filter by month if applicable
    if month != 'All':
        # filter by month to create the new dataframe
        df = df[(df.month == month)]
    
    # filter by day of week if applicable
    if day != 'All':
        # filter by day to create the new dataframe
        df = df[(df.day_of_week == day)]
    
    return df


def time_stats(df):                 # prob1
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('Most Common Start Month:', common_month)
    
    # display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print('Most Common Start day:', common_day)
    
    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].value_counts().idxmax()
    print('Most Common Start Hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    common_station = df['Start Station'].value_counts().idxmax()
    print('Most Common Start station:', common_station)
    
    # display most commonly used end station
    common_station = df['End Station'].value_counts().idxmax()
    print('Most Common End station:', common_station)
    while True:
        global cont
        cont=input('Do you want to continue more 5 rows? Please enter yes or no \n')
        if cont.lower() == 'yes':
            cont = 'yes'
            break
        elif cont.lower() == 'no':
            cont = 'no'
            break
        else:
            print('Wrong entry, Try again ,please')
        
    if cont == 'yes':
        # display most frequent combination of start station and end station trip
        common_station_comb  = df.groupby(['Start Station','End Station']).size().idxmax()
        print('Most frequent combination of start station and end station trip:', common_station_comb)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):        # Is he mean for each trip or for all trips
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    print('Total travel time is {} sec'.format(np.sum(df['Trip Duration'])))    
    
    # display mean travel time
    print('Mean travel time is {} sec'.format(np.mean(df['Trip Duration'])))    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):                 #prob2 
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)
    
    # Display counts of gender
    if 'Gender' in df.columns:
        genders = df['Gender'].value_counts()
        print('Counts of user types:\n', genders)
    else:
        print('No Gender Data in washington city recorded')
    while True:
        global cont
        cont=input('Do you want to continue the rest of rows? Please enter yes or no \n')
        if cont.lower() == 'yes':
            cont = 'yes'
            break
        elif cont.lower() == 'no':
            cont = 'no'
            break
        else:
            print('Wrong entry, Try again ,please')
    if cont == 'yes':
        # Display earliest, most recent, and most common year of birth
        if 'Birth Year' in df.columns:
            print('Most recent year of birth {} '.format(int(np.max(df['Birth Year']))))    
            
            common_date = df['Birth Year'].value_counts().idxmax()
            print('Most Common year of birth:', int(common_date))
            
        else:
            print('No Birth Year Data in washington city recorded')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
        

def main():
    flag = True
    global cont
    while flag:
        cont ='yes'     # A flag from user to continue 5 rows or no
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if cont.lower() == 'yes':
            time_stats(df)
        if cont.lower() == 'yes':
            station_stats(df)
        if cont.lower() == 'yes':
            trip_duration_stats(df)
        if cont.lower() == 'yes':
            user_stats(df)
        index = 0
        while True:  
            need_rows = input('\nWould you like to show 5 rows? Enter yes or no.\n')
            if need_rows.lower() == 'yes':
                print(df.iloc[index:index+5])
                index += 5
            elif need_rows.lower() == 'no':
                break
            else:
                print('Wrong Entry, Try again,Please')
        
        while True:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'yes':
                print(restart)
                break
            elif restart.lower() == 'no':
                flag = False
                break
            else:
                print('Wrong Entry, Try again,Please')

#Main program:
#-------------
if __name__ == "__main__":
	main()

#Additional code To Analyze CSV files:
#-------------------------------------
#Note: This code will run after the main program at the end of the code
#-----

chicago = pd.read_csv('chicago.csv')
chicago_info = chicago.isnull().sum()
print('Origional DataFrame of Chicago before fill NaN\n',chicago_info)

chicago.fillna(method='ffill',inplace=True)
chicago_info = chicago.isnull().sum()
print('Origional DataFrame of Chicago after fill NaN\n',chicago_info) 
"""
It has NaN elements In 
->'Gender'=61052  ->'Birth Year'=61019
And has zero NaN elements after appling forward fill 
"""
#--------------------------------------------------
new_york = pd.read_csv('new_york_city.csv')
new_york_info = new_york.isnull().sum()
print('Origional DataFrame of New York before fill NaN\n',new_york_info) 

new_york.fillna(method='ffill',inplace=True)
new_york_info = new_york.isnull().sum()
print('Origional DataFrame of New York after fill NaN\n',new_york_info)
"""
It has NaN elements In 
->'User Type'=692  ->'Gender'=29209  ->'Birth Year'=28220
And has zero NaN elements after appling forward fill 4
"""
#--------------------------------------------------    
washington = pd.read_csv('washington.csv')
washington_info = washington.isnull().sum()
print('Origional DataFrame of Washington\n',washington_info) 
"""
Doesn't have 'Gender' or 'Birth Year' columns
Dosen't have NaN elements
"""
