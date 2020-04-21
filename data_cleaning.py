import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data/CS7290_listings_sc_0719 - augmented_data_sc_0719.csv")
data = data.loc[~data['zestimate'].isna()]
data['zestimate'] = data['zestimate'].str.replace(',', '')
data['zestimate'] = data['zestimate'].str.replace('$', '')
data['zestimate'] = data['zestimate'].astype(float)

data.reset_index(drop=True, inplace=True)
print(data.columns.values)


# data['zipcode'][75] = 94043
# print(data.zipcode.unique())

print(data.loc[data['neighbourhood_cleansed'] == 'Unincorporated Areas'])
data['neighbourhood_cleansed'][2] = 'San Jose'
print(data.neighbourhood_cleansed.unique())

data = data.loc[data['bedrooms'] < 4]
data['bedrooms'] = data['bedrooms'].astype(str)

print(data.bedrooms.unique())
data['bathrooms'] = round(data['bathrooms']).astype(int)
data = data.loc[data['bathrooms'] < 4]
data['bathrooms'] = data['bathrooms'].astype(str)
print(data.bathrooms.unique())

data['price'] = data['price'].str.replace('$', '')
data['price'] = data['price'].str.replace(',', '')
data['price'] = data['price'].astype(float)
#data = data.loc[data['price'] < 1000]
data.reset_index(drop=True, inplace=True)
print(data.price.unique())

data = data.drop(columns=['Unnamed: 0', 'zipcode', 'latitude', 'longitude', 'room_type', 'is_location_exact', 'address'])


def calculate_monthly(P, mortgage_rate, num_years):
    n = num_years * 12
    monthly_i = mortgage_rate / 12
    numerator = monthly_i * (1 + monthly_i) ** n
    denominator = ((1 + monthly_i) ** n) - 1
    return P * numerator / denominator


def airbnb_income(price, inflation_rate, num_years):
    total = 0
    for year_number in range(num_years):
        curr_inflation = (1 + inflation_rate) ** year_number
        total += (price * curr_inflation) * 12
    return total


# %%

def roi(zestimate, inflation_rate, mortgage_rate, num_years, rental_price, down_payment_percent):
    down_payment = zestimate * down_payment_percent
    P = zestimate * (1 - down_payment_percent)

    incurred_cost = calculate_monthly(P, mortgage_rate, num_years) * 12 * num_years + down_payment

    income = airbnb_income(price=rental_price,
                           inflation_rate=inflation_rate,
                           num_years=num_years)

    return (income - incurred_cost) / incurred_cost


INFLATION_RATE = 0.028
MORTGAGE_RATE = 0.036
NUM_YEARS = 30
DOWN_PAYMENT = 0.20
data['ROI'] = roi(zestimate=data['zestimate'],
    rental_price=data['price'],
    inflation_rate=INFLATION_RATE,
    mortgage_rate=MORTGAGE_RATE,
    num_years=NUM_YEARS,
    down_payment_percent=DOWN_PAYMENT
   )
print(min(data.ROI.unique()), max(data.ROI.unique()))
print(data.columns.values)
data = data.drop(columns=['Unnamed: 14', 'Unnamed: 15', 'id'])

data.columns = ['Beds', 'Baths', 'Rent', 'Neigh', 'Type', 'Zest', 'ROI']
print(data.columns.values)

for index, row in data.iterrows():
     if row['Neigh'] in ['Palo Alto', 'Mountain View', 'Los Altos', 'Milpitas', 'Sunnyvale', 'Santa Clara']:
         data['Neigh'][index] = 'Neigh_North'
     if row['Neigh'] in ['Campbell', 'Cupertino', 'Saratoga', 'San Jose']:
         data['Neigh'][index] = 'Neigh_South'

print(data['Neigh'])
data['BPB'] = (data['Beds'].astype(int) + data['Baths'].astype(int)).astype(str)
data = data.drop(columns=['Beds', 'Baths'])
data.to_csv("data/cleansed_data_2.csv",index=False)

