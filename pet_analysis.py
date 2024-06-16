#Kristen Clifford - Task3b 
import pandas as pd 
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
 
#Load the csv file into a pandas Data Frame - Task1a
def load_data(file_path):
    return pd.read_csv(file_path)

#Function that checks for and handles any missing values. - Task1b 
#Also ensures data types are appropriate for analysis. 
def clean_data(df):
    # Renaming columns
    df.columns = ['Name', 'Birthdate', 'Price', 'Species', 'SpecialFeature', 'Extra']
    
    # Dropping the 'Extra' column as it appears to be completely NaN
    df = df.drop(columns=['Extra'])
    
    # Checking for and handling missing values
    df = df.dropna()  # Drop rows with any missing values

    # Ensuring data types are appropriate for analysis
    df['Birthdate'] = pd.to_datetime(df['Birthdate'])
    df['Price'] = pd.to_numeric(df['Price'])

    return df

#Calculate and print the average price for a given species - Task2a
def calculate_average_price(df, species):
    species_df = df[df['Species'] == species]
    average_price = species_df['Price'].mean()
    return average_price

# Find and print the names of pets with a specific feature - Task2b 
def find_pets_with_feature(df, feature): 
    pets_with_feature = df[df['SpecialFeature'] == feature]['Name'].tolist() 
    return pets_with_feature 

#Calculate and print the average price for a given species - Task3a
def get_species_statistics(df):
    statistics = {}
    for species in df['Species'].unique():
        species_df = df[df['Species'] == species]
        average_price = species_df['Price'].mean()
        average_age = species_df['Birthdate'].apply(lambda x: (pd.Timestamp.now() - x).days / 365).mean()
        statistics[species] = {
            'Average Price': average_price,
            'Average Age': average_age
        }
    return statistics


# Function to plot the distribution of prices - Task4ab
def plot_price_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Price'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Price Distribution')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('/Users/ktcli/VSC/python/MyPetStoreDataAnalysisProject/price_distribution.png')
    plt.show() 


#Function to plot average price by species - Task4cd
def plot_average_price_by_species(df):
    average_prices = df.groupby('Species')['Price'].mean().sort_values()
    plt.figure(figsize=(10, 6))
    average_prices.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Price by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Price')
    plt.grid(True, axis='y')
    plt.savefig('/Users/ktcli/VSC/python/MyPetStoreDataAnalysisProject/average_price_by_species.png')
    plt.show() 


#Function to plot price vs. age - Task5abc
def plot_price_vs_age(df):
    sns.scatterplot(x='Age', y='Price', data=df)
    plt.xlabel('Age (Years)')
    plt.ylabel('Price')
    plt.title('Price vs. Age of Pets')
    plt.savefig('/Users/ktcli/VSC/python/MyPetStoreDataAnalysisProject/price_vs_age.png')
    plt.show() 

# Function to plot age distribution by species - Task5de
def plot_age_distribution_by_species(df):
    current_date = pd.to_datetime('2024-06-15')
    df['Age'] = (current_date - df['Birthdate']).dt.days / 365.25
    fig = px.box(df, x='Species', y='Age', title='Age Distribution by Species')
    fig.write_image('/Users/ktcli/VSC/python/MyPetStoreDataAnalysisProject/age_distribution_by_species.png')
    fig.show() 