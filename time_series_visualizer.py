import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Importing data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df = df.set_index("date")

# Cleaning data
top_threshold = df["value"].quantile(0.975)
bottom_threshold = df["value"].quantile(0.025)

df = df[(df["value"] <= top_threshold) & (df["value"] >= bottom_threshold)]


def draw_line_plot():
    # Drawing line plot
    df.index = pd.to_datetime(df.index)

    fig, axes = plt.subplots(figsize = (15, 5))
    axes.plot(df.index, df["value"], color = "red")
    axes.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    axes.set_xlabel("Date")
    axes.set_ylabel("Page Views")

    # Saving image and returning fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copying and modifying data for monthly bar plot
    df_bar = df.copy()
    df_bar['Year'] = df.index.year
    df_bar['Month'] = df.index.month_name()

    # Drawing bar plot
    df_bar = df_bar.groupby(['Year', 'Month'])['value'].mean()
    df_bar = df_bar.unstack(level = 'Month')
    df_bar = df_bar[["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]]

    fig = df_bar.plot.bar(figsize=(9, 7)).figure

    plt.xlabel('Years');
    plt.ylabel('Average Page Views');
    plt.legend(title = 'Months');

    # Saving image and returning fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Preparing data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Drawing box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize = (20, 5))
    axes[0] = sns.boxplot(data = df_box, x = 'year', y = 'value', ax = axes[0])
    axes[0].set_ylabel('Page Views')
    axes[0].set_xlabel('Year')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    axes[1] = sns.boxplot(data = df_box, x = 'month', y = 'value', ax = axes[1], order = month_names)
    axes[1].set_ylabel('Page Views')
    axes[1].set_xlabel('Month')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Saving image and returning fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
