#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
import matplotlib.pyplot as plt


# In[107]:


G_API = ''

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



def generate_csv_data(listings, file_name):
    listings.reset_index(drop=True, inplace=True)
    addresses = []
    for index, row in listings.iterrows():
        print(row['latitude'], row['longitude'])
        address = get_address(row['latitude'], row['longitude'])
        addresses.append(address)
    listings['address'] = pd.Series(addresses)
    listings.to_csv('data/' + file_name)
    return listings

filtered_listings = listings.loc[listings['property_type'].isin(['Condominium','Townhouse'])]
filtered_listings = filter_dataframe(filtered_listings, 'room_type', 'Entire home/apt')

filtered_listings = filtered_listings[["id",
                                       "zipcode",
                                       "bedrooms",
                                       "bathrooms",
                                       "price",
                                       "neighbourhood_cleansed",
                                       "latitude",
                                       "longitude",
                                       "property_type",
                                       "room_type",
                                       "is_location_exact"]]


# In[87]:


filtered_listings.shape


# In[88]:


listings_0719 = pd.read_csv("data/listings_0719.csv")
filtered_listings_0719 = listings_0719.loc[listings_0719['property_type'].isin(['Condominium','Townhouse'])]
filtered_listings_0719 = filter_dataframe(filtered_listings_0719, 'room_type', 'Entire home/apt')

filtered_listings_0719 = filtered_listings_0719[["id",
                                                 "zipcode",
                                                 "bedrooms",
                                                 "bathrooms",
                                                 "price",
                                                 "neighbourhood_cleansed",
                                                 "latitude",
                                                 "longitude",
                                                 "property_type",
                                                 "room_type",
                                                 "is_location_exact"]]
print(filtered_listings_0719.shape)

nonduped_rows = set(filtered_listings_0719.id) - set(filtered_listings.id)
filtered_listings_0719 = filtered_listings_0719[filtered_listings_0719.id.isin(nonduped_rows)]

filtered_listings_0719 = filtered_listings_0719[(filtered_listings_0719.bedrooms <= 3) & (filtered_listings_0719.bathrooms <= 3)]

print(filtered_listings_0719.shape)


# In[89]:


print(len(generate_csv_data(filtered_listings_0719, "augmented_data_sc_0719.csv").address.unique()))

