# 4. Data Wrangling

This chapter was a deep dive into the data wrangling part of the data analysis process. I learned about the difference between messy and dirty data, how tidy data should look like, about the assessing, defining, cleaning and testing process, etc. Moreover, I talked about many different file types and different methods of gathering data.

In this project I had to deal with the reality of dirty and messy data (again). We gathered data from different sources (for example the Twitter API), identified issues with the dataset in terms of tidiness and quality. Afterwards I had to solve these problems while documenting each step. The end of the project was then focused on the exploration of the data.

## Introduction 

Using Python and its libraries, I will gather data from some sources and formats, assess its quality and tidiness, then clean it. All the process will be documented in here and plus showcase them through analyses and visualizations using Python (and its libraries) and/or SQL.

The dataset that will be gathered and anlyzed is the tweet archive of Twitter user [@dog_rates](https://twitter.com/dog_rates), also known as [WeRateDogs](https://en.wikipedia.org/wiki/WeRateDogs). WeRateDogs is a Twitter account that rates people's dogs with a humorous comment about the dog.

WeRateDogs downloaded their Twitter archive and sent it to Udacity via email exclusively for us, students, to use in this project. This archive contains basic tweet data (tweet ID, timestamp, text, etc.) for all 5000+ of their tweets as they stood on August 1, 2017. More on this soon.

### The Goal

Wrangle WeRateDogs Twitter data to create interesting and trustworthy analyses and visualizations

### The Data

In this projetct, I will work with three datasets:

1. <b>Enhanced Twitter Archive:</b> 
    - The WeRateDogs Twitter archive contains basic tweet data for all 5000+ of their tweets, but not everything. One column the archive does contain though: each tweet's text.
2. <b>Additional Data via the Twitter API: **</b>
    - Back to the basic-ness of Twitter archives: retweet count and favorite count are two of the notable column omissions. Fortunately, this additional data can be gathered by anyone from Twitter's API. Well, "anyone" who has access to data for the 3000 most recent tweets, at least. But with the WeRateDogs Twitter archive and specifically the tweet IDs within it, it's possible to gather this data for all 5000+.
    - <b>_** With the recent changes on Twitter API, for the fisrt submission of this project, I will follow the [Udacity Recomendations](https://knowledge.udacity.com/questions/855395) and use the JSON provided by Udacity. After the submit, I intend to try develop the same or better results following the extraction with the API._</b>
3. <b>Image Predictions File</b>:
    -  table full of image predictions (the top three only) alongside each tweet ID, image URL, and the image number that corresponded to the most confident prediction (numbered 1 to 4 since tweets can have up to four images).