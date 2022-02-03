# Flights Data Analysis
## by Ahmed Mokhtar
###### this is my final project in Udacity Data Analyst Nanodegree.

## Project detail
This project is based on the flight data of US airplanes between (Jan 2017 -> June 2020), It contains three main features, the delay arraival flights The canceled travels, and some information about the flights as the month, year, airport, carrier,...etc.

The delay of arrival has many reasons, it is is one of the elements of ("NASDelay", "LateAircraftDelay", "CarrierDelay", "WeatherDelay", "SecurityDelay"). 

The delay of arrival has many reasons, it is is one of the elements of ("NASDelay", "LateAircraftDelay", "CarrierDelay", "WeatherDelay", "SecurityDelay"). 
The delay of arrival has many reasons, it is is one of the elements of ('carrier_ct', 'weather_ct', 'nas_ct', 'security_ct', 'late_aircraft_ct', 'arr_cancelled').

#### Submitted files
- flightsdata_explanation.ipynb  
- flightsdata_exploration.html   
- flightsdata_explanation.slides.html   
- output_toggle.tpl   
- readme.md    

   
## Dataset
The data consists of 63290 records about flights in US. This records include date(month,year), Carrier name, Airport, arrival delay time, and the delay_reasons, and other various features such the number of flights, Cancelled flights, and the cancellation_reasons.
The dataset (airline_delay_causes.csv) can be downloaded from ASA Section on Statistical Computing & ASA Section on Statistical Graphics. [here](https://community.amstat.org/jointscsg-section/home).

## Wrangling process
* I excluded Unnamed:21 column that had nan values in all couloms.
* I dropped all rows that had nan values.
* I alos wrangled the city name from the airport name and add a new column to add it there.


## Summary of Findings

> This Delay time per carrier data is normal distibuted as we shuold consider if the flights arrive early, and this make sence as the flight that delayed in a couple of minutes should be much greater than the number of delayed flights in higher range.

> I also saw the total flights per month, and found that the two highest months were Jul and Augast, I can imagine this is because the summer holiday, and Febrauary is the lowest month in the year, I think beacuse it is only 28 day.

> I can see that the carrier air-lines vary from each other very much, as we can see some of them has very thin violin plot as they records were very littel and they have too much delay, other carrier air lines have too much records in the compare of other carrier airline and they have less maen than them, which lead to say there is a relationship between the delay of the carrier flights and the flights number on this air-lines

> At (Nov-2017, Dec-2017, and Jun-2019) there were many flights that cancelled or delayed because security reasons, I think there were some terrorist operations or something like that in this months.


## Key Insights for Presentation
* For the presentation, I focus on the distribution of the variables as they tell us more about the data details, especially the delay and the carrier flights journeys.
* I also focus on the effect of the coronavirus as it made the number of flights decreased very much
* I tried to compare the carrier airlines to show how they vary.
* In my exploration, I found that something interesting in the security issues that affect the delayed or canceled flights, so I want to share this piece of information
