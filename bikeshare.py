import time
import pandas as pd
from datetime import datetime,timedelta

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

#added comment for git
#another comment for git

#added for refactoring 
#another for refactoring
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or
                      "all" to apply no month filter
        (str) day - name of the day of week to filter by, or
                    "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select a city to explore the bike share data. ' +
                     'Chicago, New York City, or Washington?\n')
        if city.lower() in CITY_DATA.keys():
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Specify the month of data to explore. All, January ' +
                      'February, March, April, May, or June?\n')
        if month.lower() in ['all', 'january', 'february', 'march',
                             'april', 'may', 'june']:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Specify the day of data to explore. ' +
                    'All, Monday, Tuesday, Wednesday, Thursday, Friday, ' +
                    'Saturday, Sunday?\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday',
                           'friday', 'saturday', 'sunday']:
            break

    print('-'*50)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month
    and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all"
                      to apply no month filter
        (str) day - name of the day of week to filter by, or "all"
                    to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_status(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # display the most common month
    print('\nMost Common Month of Travel:')
    print(df['month'].mode()[0])

    # display the most common day of week
    print('\nMost Common Day of Travel:')
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print('\nMost Common Start Hour of Travel:')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_status(df):
    
    start_time=time.time()
    #most common start station
    start_station=str(df['Start Station'].mode()[0])
    print("Most Common Start Station is: {}".format(start_station))
    
    # most common end station
    
    end_station=str(df['End Station'].mode()[0])
    print("Most Common End Station is: {}".format(end_station))
    
    
    # most common trip start to end
    
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))
  
    
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def duration(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()
    total_time=int(df['Trip Duration'].sum())
    print("Total time is:{} second".format(total_time))
    
    
    avg_time=int(df['Trip Duration'].mean())
    print("Average time is :{} second".format(avg_time))
    
    time=str(datetime.timedelta(seconds=total_time))
    print(time)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 
    

    
def user_type(df):
    
    start_time=time.time()
    
    #count type of users
    
    user_types=str(df['User Type'].value_counts().to_string())
    print(user_types)
    
    # count of each gender
    
    try:
        print(df['Gender'].value_counts())
    except:
        print('Data does not include genders')
        
        
    # earliest,recent,most common year of birth
    
    try:
        print('Earliest: {}\nLatest: {}\nMost Common: {}'
              .format(df['Birth Year'].min(), df['Birth Year'].max(),
                      df['Birth Year'].mode()[0]))
    except:
        print('Data does not include date of birth')
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df): 
    
    # initial input! 
    display_raw_input = input("\nWould you like to see individual raw data? Enter 'yes' or 'no'\n").strip().lower()    
    if display_raw_input in ("yes", "y"):
        i = 0
        
        # use while loop for the inputs that you want repeated! 
        # thus should start here, not at the beginning of the code

        while True: 
            # check if i is out of bounds, if upper limit is out of bounds, 
            # then print from lower limit to length of dataframe rows                     
            if (i + 5 > len(df.index) - 1):
                # remember that the slicing is lower bound inclusive and upper bound exclusive!! 
                # thus upper bound should be (len(df.index) --> won't print out that upper bound bc its exclusive)
                print(df.iloc[i:len(df.index), :])
                print("You've reached the end of the rows")
                break

            # if i is not out of bounds, then just print the dataframe normally
            print(df.iloc[i:i+5, :])
            i += 5
            
            # program temporarily halts at the input! 
            # thus while loop does not get executed 100000 times (exaggerated) a second lol 
            show_next_five_input = input("\nWould you like to see the next 5 rows? Enter 'yes' or 'no'\n").strip().lower()
            if show_next_five_input not in ("yes", "y"):
                break
    
    
def main():
    while True:
        city,month,day=get_filters()
        df=load_data(city,month,day)
        
        time_status(df)
        station_status(df)
        duration(df)
        user_type(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    
    
    


if __name__ == "__main__":
    main()
                
     