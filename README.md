# Predicting Home Value
by Deangelo Bowen 
08 Jun 2022

---
# Overview

## Project Description:
   To provide insights and any potential improvements to the Zillow Data Science Team's 2017 Singly Family Property prediction model. 

## Project Goals:
- Construct a ML Regression model that can predict property tax value of single family homes in 2017. 
- Find Key drivers of property tax value for single family homes.
- Make recommendations on what works or what might not work given evaluation in prediction of the homes' values.

---

## Initial Hypothesis/Questions

- Are certain counties more expensive/ have a higher tax value on average than others?
- Why are some properties valued so differently from others when they are located so close to each other?
- Is having 1 Bathroom  worse than have 2 Bathrooms? 
- Is there a relationship between the year a home was built and it's value? 
  
---

## Data Dictionary
|Column | Description | Dtype|
|--------- | --------- | ----------- |
|bathrooms| number of bathrooms| float64|
|bedrooms| number of bedrooms| int64|
|tax_value| final home estimated price| int64|
|tax_amount| amount of taxes| float64|
|fips| county location| String|
|sqft| home sqare feet| int64|
|year_built| home year was built| int64|
    
---
   
### Planning
   - Define goals
   - Determine audience and delivery format
   - Ask questions/formulate hypothesis
   - Determine the MVP

### Acquisition
   - Create a function that establishes connection to zillow_data in CodeUp mySQL
   - Create a function that holds your SQL query and reads results
   - Creating functing for caching data and stores as .csv for ease
   - Create and save in acquire.py so functions can be imported

   ### Preparation
   - Identifiy each of the features data types and manipulated relevant columns to appropriate dtypes.
   - Remove all irrelevant or duplicated columns.
   - Renamed columns to more appropriate and identifiable naming conventions.
   - Repeated these steps on the split data for future modeling.
    
   ### Exploration
   - Use the initial questions to guide the exploration process
   - Create visualizations to help identify drivers
   - Use statistical testing to confirm or deny hypothesis
   - Document answers to questions as takewaways
   - Utilize explore.py as needed for clean final report

 ### Model
   - Train model
   - Make predictions
   - Evaluate model
   - Compute accuracy
   - Utilize model.py as needed for clean final report
--- 

### Key Findings and Takeaway's Summary : 
- Los Angeles has, on average, cheaper total home value than Ventura and Orange County. 
- Ventura and Orange County are closer to one another in terms of average value.
- The more features in, or added to a home, the higher the total home value.
- Homes with 1 bathrooms were worse for square feet, but better for price. 
- There is a linear relationship between the year built and the price of the home.
- So, while majority of homes were built in the 1950s, the newer the home, the higher the tax value.
---
## Results of Obeserving the Primary Goals:

- [x] #### Constructed a ML Regression model that can predict property tax value of single family homes in 2017. 
    - My Polynomial Regression Model beat the baseline model and had outstanding performace over the other models. 
- [x] #### Find Key drivers of property tax value for single family homes.
    - Having more bathrooms increased the value of a property
    - Having more squarefeet increased the value of a property
    - The newer the property, the more the value increases
    - Location is a driver in total property value
- [x] Make recommendations on what works or what might not work given evaluation in prediction of the homes' values.
 
---
### Recommendations : 

- Continue analyzing these key drivers in predicting total home value over time and making improvements to data collection.
- Integrate additional features into the dataset that may help accurately define a feature that influences total home value (i.e. age of home and upgrades). 
---
### Next Steps:
- Evaluate on more unique models
- Investigate the data further-- assuming there is potential data to be collected that can further accurately predict a homes value. 
- Compare this dataset with a more recent housing dataset to see if more features arise that can accurately predict value.
---

### To Recreate this Project:
   - You will need an env file with database credentials saved to your working directory database credentials with CodeUp database (username, password, hostname) 
   - Create a gitignore with env file inside to prevent sharing of credentials
   - Download the acquire.py and prepare.py (model.py and explore.py are optional) files to working directory
   - Create a final notebook to your working directory
   - Review this README.md
   - Libraries used are pandas, matplotlib, Scipy, sklearn, seaborn, and numpy
   - Run predicting_telco_churn.ipynb
   - Create a .csv file with the predictions from your ML model of at risk customers
