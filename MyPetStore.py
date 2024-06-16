#Kristen Clifford -Task3b/c 
import pandas as pd 
from pet_analysis import load_data, clean_data, calculate_average_price, find_pets_with_feature, get_species_statistics, plot_price_distribution, plot_average_price_by_species, plot_price_vs_age, plot_age_distribution_by_species

# Load the CSV file into a DataFrame - Task1a
file_path = '/Users/ktcli/VSC/python/MyPetStoreDataAnalysisProject/pets.csv'

#Load and clean data - Task1b
df = load_data(file_path)
df_cleaned = clean_data(df) 

if __name__ == "__main__":
    file_path = '/Users/ktcli/VSC/python/MyPetStoreDataAnalysisProject/pets.csv'
    
    df = load_data(file_path)
    df_cleaned = clean_data(df)

    # Rename and clean columns
    df.columns = ['Name', 'Date_of_Birth', 'Price', 'Type', 'Additional_Info', 'Empty_Column']
    df = df.drop(columns=['Empty_Column'])
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Date_of_Birth'] = pd.to_datetime(df['Date_of_Birth'], errors='coerce')
    current_date = pd.to_datetime('2024-06-15')
    df['Age'] = (current_date - df['Date_of_Birth']).dt.days / 365.25

# Calculate and print the average price for a given species - Task2a 
species = 'Cat'  # Example species, change as needed
average_price = calculate_average_price(df_cleaned, species)
print(f"The average price for {species} is: {average_price:.2f}")

# Find and print the names of pets with a specific feature - Task2b
sample_feature = 'warm'  # Example feature, change as needed
pets_with_sample_feature = find_pets_with_feature(df_cleaned, sample_feature)
print(f"Pets with the feature '{sample_feature}': {pets_with_sample_feature}") 

#Get statistics - Task 3c
species_statistics = get_species_statistics(df_cleaned)
print(species_statistics)  

# Plot price distribution - Task 4ab
plot_price_distribution(df_cleaned) 

#Plot average price by species - Task4cd
plot_average_price_by_species(df_cleaned) 

#Plot price vs age - Task5abc
plot_price_vs_age(df)

# Plot and save the age distribution by species - Task5de
plot_age_distribution_by_species(df_cleaned) 