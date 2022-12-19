# 5. Data Visualizations

The final chapter was focused on proper visualization of data. We learned about chart junk, uni-, bi- and multivariate visualization, use of color, data/ink ratio, the lief factor, other encodings, [...].

The task of the final project was to analyze and visualize real-world data. I chose the Ford GoBike dataset.

## Ford GoBike Data Visualization


### Dataset

This data set includes information about individual rides made in a bike-sharing system covering the greater San Francisco Bay area. This project will analyze the data collected from users of the GoBike program for February 2019. 

The original dataset has 183,412 rows and 16 features of some rides for February 2019 as:
- Duration of the rides in seconds;
- Start and Ent Time of the ride;
- Station Information as the id, the name and the location in coordinates;
- The user information as year of birth, gennder and subscription type (Customer or Subscription)
- The bike id

During the wrangling process, was necessary correct some quality and tidiness issues. For this, I dropped missing values, corrected columns type, created new columns with the information of the dataset and removed some outliers.

After all this process, there was left 174,759 rides with 7 features.


### Summary of Findings

- Almost 30% of data has the distance lower than 1%.
- 96% of the data has the distance of stations between 4km.
- 96% of the data it's under 2,000 seconds (under 30 minutes).
- Some people that rent the bike for just one minute.
- Almost 80% of the users are between 20 and 40 years old.
- There is a linear relation between the duration of the rent and the distance between the stations where the bike was got and left
- People looks get the bike during more time on the weekends.


### Key Insights for Presentation

I foccused on find relations between the stations that people get and leave the bicycles. Including in this relation the duration of time that people rent the bike, the day of the week and the hour of the day.