# causal_ml_airbnb
Building a causal model from Airbnb listing data to be able to understand what factors impact ROI for different properties

[Airbnb data](http://insideairbnb.com/get-the-data.html)


# Causal Model of Santa Clara County Airbnb Data

## Authors 

Shashank Viswanadha, Alexander Gomez

## Abstract

We used Airbnb listing rental data to build a causal model of ROI. We started by pulling the data from Airbnb and then manually labeling property price estimates. We used this data to test multiple DAG architectures and then used the best DAG architecture to build a statistical model in Pyro. We then used the statstical model to learn about the causal effects of different settings in our data.

[See video abstract](https://youtu.be/adiQcwsGX2Y)

## How to explore this project

### Data Cleaning

We considered Airbnb data for Santa Clara county taken form [Inside Airbnb](http://insideairbnb.com/get-the-data.html) for this project. We considered data from July 2019 [listings_0719.csv](data/listings_0719.csv) and March 2020 [listings_0320.csv](data/listings_0320.csv) for our analysis. 

#### Step 1: 
We filtered out data based on the property type and considered only Condominiums, Townhouses for this project. Additionally we only considered only the properties which were available to rent as a whole on Airbnb. The reason we decided to do this was to get an accurate estimate of Return on Investment which partially rented properties would not give us.
#### Step 2:
We used Google's [geo-coding API](https://developers.google.com/maps/documentation/geocoding/start?utm_source=google&utm_medium=cpc&utm_campaign=FY18-Q2-global-demandgen-paidsearchonnetworkhouseads-cs-maps_contactsal_saf&utm_content=text-ad-none-none-DEV_c-CRE_315916117595-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+Google+Maps+Geocoding+API-KWID_43700039136946117-kwd-300650646186-userloc_9004054&utm_term=KW_google%20geocoding%20api-ST_google+geocoding+api&gclid=CjwKCAjwnIr1BRAWEiwA6GpwNYs9HqeKeAm07opBtifC1HqKtl2GTBfPIQz2365hvhJp4v2jhtcbxhoCVbIQAvD_BwE)
to get the addresses for the properties using their latitude and longitude. The data after applying steps 1 and 2 is stored in [augmented_data_0719](data/augmented_data_0719.csv) and [augmented_data_0320](data/augmented_data_0320.csv). The code for this is in [pull_addresses.py](pull_addresses.py).
#### Step3:
We used [Zillow](https://www.zillow.com) to get the Zestimates (current estimated market price) for each of these properties using their addresses. This data is stored in [data_with_estimates_0719.csv](data/data_with_estimates_0719.csv) and [data_with_estimates_0320.csv](data/data_with_estimates_0320.csv).
#### Step4:
The data from these two files were combined into [cleansed_data.csv](data/cleansed_data.csv) after cleaning up all the properties for which we could not find estimates for and adding the calculated ROI for each property. The code for this is in [data_cleaning.py](data_cleaning.py). The data from [cleansed_data.csv](data/cleansed_data.csv) was used for all our analysis.

### Causal DAG exploration and evaluation

In the file `dag_analysis.rmd` we explore various DAG structures and evaluate each based on Global Markov and faithfulness properties, which can be found at the end of the file.

### Model Building using Pyro

In the file `model.ipynb` we build our causal models in pyro, analyze the results from them, and provide some next steps for improving them.

### Project Libraries

Libraries that need to be installed:

Python:
- Pandas
- Numpy
- Pyro
- Statsmodels
- Torch
- Statistics

R:
- bnlearn
- Rgraphviz
