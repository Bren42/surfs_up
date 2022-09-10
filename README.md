# surfs_up

## Analysis Overview

The purpose of this analysis was to determine whether or not the temperatures in Oahu Hawaii were practical to sustain keeping the surfs up ice cream and surf shop open year round.
  As we had earlier prepared data that we had collected from weather stations around the island into useful datapoints we would begin with that data again. This time however we were going to look at two points in time 6 months appart from each other, we would first review temperatures in June, during the summer months, and then follow those up with a similar analysis on the month of December. We would need to look at all data that we had collected for a multi-year analysis of the average, median, minimum, and maximum temperatures in that region. As this would be multiple years of data it should give us a really good statistical outcome to base our decisions off of.
  
  ## June Results
  To start we formatted all of the collected June data into a list to make it easier for us to view.
  
  ![This is an image](https://github.com/Bren42/surfs_up/blob/main/resources/challenge_june_list.png)
  
  As you can see the data was properly formatted and more clean to use and read as a list, however we had seven years of June dates collected. To make this easier to read we converted the data into a DataFrame to make it even easier to work the data into a more useful format. After completion of the dataframe we queried the data to find the Max temperature, Min temperature, the average (Mean) and the median temperatures. 
  
  ![This is an Image](https://github.com/Bren42/surfs_up/blob/main/resources/challenge_june_tobs.png)
  
  As we can see from the image above we had 1700 unique data items to work with, the average and the median are between 74 and 75 degrees, so very stable with little variation. As well our max and min temperatures, between 85 and 64 respectively are very moderate deviations.
  
  ## December Results
  
  Now that we had the June results we need to see how the month of December would compare to the opposite end of the year in June. As we were looking for the same data outputs with only a change in the data we were able to effectively re-factor some of our previous query code with only changes to the month we wanted to see. So as before we convereted the data into a list and then converted that into a dataframe.
  
  
  ![This is an image](https://github.com/Bren42/surfs_up/blob/main/resources/challenge_dec_list.png)
  
  As before the list was too coumbersome to work with independently as it had over 1500 unique items, as mentioned above we converted this to a data frame and again asked the dataframe for summary statistics of the collected weather.
  
  ![This is an image](https://github.com/Bren42/surfs_up/blob/main/resources/challenge_dec_tobs.png)
  
  Looking at the December data we see a slight change in the max temp, June is 85, December is 83 degrees. Our min temps swung a bit more with a 8 degree difference between the June low and the December low. Again the mean and the median are nearly identical. Decembers median temp is 71 degrees, whereas Junes was 75, only a 4 degree differences.
  
  - December and June had only a 4 degree difference in their Median temperature.
  - The highest temp in December was 83, whereas in June it was 85. Again a very small variance.
  - The lowest temp in December was 56, June recorded a low of 64. This is by far the biggest variance.


## Summmary
Looking at our data it seems to be telling us that the median temperatures in this area are very stable with very little deviation from the median. It is true that there will be rare occasions in December where the low may impact business, but overall the median temperatures are so similar between June and December that it stands to reason that this location is a ideal spot to open the business all your round, as all businesses that have weather considerations experience some outliers, this location is ideal for its low outliers.
