import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
WEEKDAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("You can choose the following cities: - Chicago, New York City, Washington")
    is_valid = True
    while is_valid:
        city = input("Enter the city : ").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Please enter a valid city name")
        else: 
            is_valid = False
    is_valid = True  
    
    while is_valid:
        print("Choose any month from January upto June or all")
        month = input("Enter the month : ").lower()
        if month not in MONTHS:
            print("Please enter a valid month name")
        else: 
            is_valid = False
    is_valid = True
    
    while is_valid:
        day = input("Enter the week day : ").lower()
        if day not in WEEKDAYS:
            print("Please enter a valid week day name")
        else: 
            is_valid = False

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        month_index = MONTHS.index(month) + 1
        df = df[df['month'] == month_index]
    if day != 'all':
        df = df[df['day'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print("Most common month")
    print(df['month'].mode()[0])

    print("Most common day of week")
    print(df['day'].mode()[0])

    print("most common start hour")
    df['hour'] = df['Start Time'].dt.hour
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print("most common start station")
    print(df['Start Station'].mode()[0])

    print("most commone end staion")
    print(df['End Station'].mode()[0])

    print("Most Common Bike Trip")
    df['Start End'] = df['Start Station'].map(str) + df['End Station'].map(str)
    print(df['Start End'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    print("Total Travel Time")
    print((df['End Time'] - df['Start Time']).sum())

    print("Average Travel Time")
    print((df['End Time'] - df['Start Time']).sum() / len(df['Start Time']) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print("Types of Users")
    print(df['User Type'].value_counts())
    
    try:
        print("Gender Types Counts")
        print(df['Gender'].value_counts())

        print("Earlist Birth Year")
        print(df['Birth Year'].min())

        print("Most recent birth year")
        print(df['Birth Year'].max())

        print("Most common year of birth")
        print(df['Birth Year'].mode())
    
    except KeyError:
        print("There is no birth/gender column for washington dataset")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
