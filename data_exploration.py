import pandas as pd
import requests
import matplotlib.pyplot as plt
G_API = 'YOUR API KEY'

# reading csv file
listings = pd.read_csv("data/listings.csv")



def filter_dataframe(df, column_name, value):
    return df.loc[df[column_name] == value]

def get_address(lat, long):
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + str(lat) + ',' + str(long) + '&key=' + G_API
    r = requests.get(URL)
    data = r.json()
    address = data['results'][0]['formatted_address']
    return address



def generate_csv_data(listings):
    listings.reset_index(drop=True, inplace=True)
    addresses = []
    for index, row in listings.iterrows():
        address = get_address(row['latitude'], row['longitude'])
        addresses.append(address)
    listings['address'] = pd.Series(addresses, index=filtered_listings.index)
    listings.to_csv('data/augmented_data.csv')


print(list(listings.columns.values))
print('######################################')


filtered_listings = filter_dataframe(listings, 'room_type', "Entire home/apt")

filtered_listings = filtered_listings.loc[filtered_listings['calculated_host_listings_count'] > 8]

filtered_listings = filtered_listings[["zipcode",
                 "bedrooms",
                 "bathrooms",
                 "price",
                 "neighbourhood_cleansed",
                 "latitude",
                 "longitude"]].copy()
print(filtered_listings)

print(filtered_listings.neighbourhood_cleansed.unique())
generate_csv_data(filtered_listings)


