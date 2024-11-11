## Page View Time Series Visualizer

This project is about visualizing time series data using a line chart, bar chart, and box plots.

**Dataset Source**
[https://www.freecodecamp.org/](FreeCodeCamp.org) forum page views.

The dataset contains the number of page views each day on the FreeCodeCamp.org forum 2016-05-09 to 2019-12-03


#### Goal 
understand the patterns in visits and identify yearly and monthly growth.


#### project content:
* Using Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the __date__ column.
* Cleaning the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
* Creating a __draw_line_plot__ function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". The title should be __Daily freeCodeCamp Forum Page Views 5/2016-12/2019__. The label on the x axis should be Date and the label on the y axis should be Page Views.
* Creating a __draw_bar_plot__ function that draws a bar chart similar to "examples/Figure_2.png". It should show average daily page views for each month grouped by year. The legend should show month labels and have a title of __Months__. On the chart, the label on the x axis should be __Years__ and the label on the y axis should be __Average Page Views__.
* Creating a __draw_box_plot__ function that uses Seaborn to draw two adjacent box plots similar to "examples/Figure_3.png". These box plots should show how the values are distributed within a given year or month and how it compares over time. The title of the first chart should be __Year-wise Box Plot (Trend)__ and the title of the second chart should be __Month-wise Box Plot (Seasonality)__. Make sure the month labels on bottom start at __Jan__ and the x and y axis are labeled correctly. The boilerplate includes commands to prepare the data.

