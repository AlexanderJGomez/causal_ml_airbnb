
### TODO

- [ ] Figuring out important features from data for each listing
    1. \# of beds
    2. sqft 
    3. etc.
- [ ] Getting data for 1 City
    1. lat, long
    2. airbnb price
    3. important features we chose
- [ ] Port the data into R
- [ ] Create an ROI metric
- [ ] Build the DAGS in bnlearn based on our assumptions
- [ ] Test the DAGS for faithfulness and global markov property
    1. tests of conditional independence

Goal: build causal generative model that allows you to identify the causal effect of various factors on Airbnb income relative to the market price of the unit

### Meeting Notes
1. use google maps api to convert lat long to rough address
2. use Zillow API to get Zestimate of listing
3. most people originally intended to rent out or live in property
4. if i want to buy property with airbnb as source of revenue
    1. what factors have the highest impact on ROI?
    2. predictive model of airbnb ROI
        1. function of cost of property
        2. cost of borrowing
        3. income from airbnb
        4. 
    3. problem is you are making interventions to specifically choose property
5. Needs to be causal because
    1. choosing each property is an intervention
6. To get started
    1. script to combine zestimate(sale price)
    2. build causal model in R
        1. fit a dag
        2. think about what dag looks like
        3. do d separations match up to conditional independence
            1. testing markov assumption and faitfulness proprty
        4. As simple as possible but no simpler
    3. bnlearn will force the data to be palatable because of strict assumptions
    4. bnlearn gets shape of model
    5. Then port to Pyro, reprogram, train, get param estimates, relax assumptions and get more flexible model, optimize GOF
    6. net present value(?) for ROI
    7. how to quantify ROI for rental property
7. Market price vs airbnb price
    1. school location
    2. close to MBTA?
    3. Close to venues?
8. What new features might be useful to add?
    1. distance to MBTA?

### Data Summary

1. listings.csv.gz = Detailed listings data
    1. lat and long
2. calendar.csv.gz = detailed calendar data (was unable to open)
3. listings.csv = summarized listing data
    1. name
    2. host name and id
    3. location
    4. room type
    5. price
    6. number of reviews
    7. last review data
    8. reviews per month
    9. calculated host listings count(?)
    10. availabilty / 365 days
4. reviews.csv (good for time based analytics)
    1. listing id
    2. date
5. neighborhoods.csv
    1. neighborhood group
    2. neighborhood name

