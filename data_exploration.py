import pandas as pd
import requests
import matplotlib.pyplot as plt
G_API = 'AIzaSyDPvnBQie8O8ujlU_BTGVQKMihXOQ8Ycvs'

# reading csv file
listings = pd.read_csv("data/listings_sc.csv")



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
        print(row['latitude'], row['longitude'])
        address = get_address(row['latitude'], row['longitude'])
        addresses.append(address)
    listings['address'] = pd.Series(addresses)
    listings.to_csv('data/augmented_data_sc.csv')
    return listings


print(list(listings.columns.values))
print('######################################')
print(listings.is_location_exact.unique())
print(listings.room_type.unique())




filtered_listings = listings.loc[listings['property_type'].isin(['Condominium','Townhouse'])]
filtered_listings = filter_dataframe(filtered_listings, 'room_type', 'Entire home/apt')

filtered_listings = filtered_listings[["zipcode",
                 "bedrooms",
                 "bathrooms",
                 "price",
                 "neighbourhood_cleansed",
                 "latitude",
                 "longitude",
                "property_type",
                "room_type",
                "is_location_exact"]].copy()
print(filtered_listings)

#print(filtered_listings.neighbourhood_cleansed.unique())

print(len(generate_csv_data(filtered_listings).address.unique()))
