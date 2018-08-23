#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# create a DataFrame from the .csv file:
df = pd.read_csv('../Data/iris.csv')


# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
setosa = df[df['class']=='Iris-setosa']['petal_length']
versic = df[df['class']=='Iris-versicolor']['petal_length']
virgin = df[df['class']=='Iris-virginica']['petal_length']

# Define a data variable
hist_data = [setosa,versic,virgin]
group_labels = ['setosa','versicolor','virginica']

# Create a fig from data and layout, and plot the fig
fig = ff.create_distplot(hist_data,group_labels)

pyo.plot(fig)
