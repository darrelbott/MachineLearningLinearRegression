import tensorflow
import keras
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

########################################################################################################################
# Data from: https://archive.ics.uci.edu/ml/datasets/Student+Performance
# Citation: P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. In A. Brito and
#           J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) pp. 5-12, Porto,
#           Portugal, April, 2008, EUROSIS, ISBN 978-9077381-39-7.
# Data Set Information:
# This data approach student achievement in secondary education of two Portuguese schools. The data attributes include
# student grades, demographic, social and school related features) and it was collected by using school reports and
# questionnaires. Two datasets are provided regarding the performance in two distinct subjects: Mathematics (mat) and
# Portuguese language (por). In [Cortez and Silva, 2008], the two datasets were modeled under binary/five-level
# classification and regression tasks. Important note: the target attribute G3 has a strong correlation with attributes
# G2 and G1. This occurs because G3 is the final year grade (issued at the 3rd period), while G1 and G2 correspond to
# the 1st and 2nd period grades. It is more difficult to predict G3 without G2 and G1, but such prediction is much more
# useful (see paper source for more details).
#
# Attribute Information:
#
# 1 school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
# 2 sex - student's sex (binary: 'F' - female or 'M' - male)
# 3 age - student's age (numeric: from 15 to 22)
# 4 address - student's home address type (binary: 'U' - urban or 'R' - rural)
# 5 famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
# 6 Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
# 7 Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
# 8 Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 â€“ 5th to 9th grade, 3 â€“ secondary education or 4 â€“ higher education)
# 9 Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
# 10 Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other')
# 11 reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')
# 12 guardian - student's guardian (nominal: 'mother', 'father' or 'other')
# 13 traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
# 14 studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
# 15 failures - number of past class failures (numeric: n if 1<=n<3, else 4)
# 16 schoolsup - extra educational support (binary: yes or no)
# 17 famsup - family educational support (binary: yes or no)
# 18 paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
# 19 activities - extra-curricular activities (binary: yes or no)
# 20 nursery - attended nursery school (binary: yes or no)
# 21 higher - wants to take higher education (binary: yes or no)
# 22 internet - Internet access at home (binary: yes or no)
# 23 romantic - with a romantic relationship (binary: yes or no)
# 24 famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
# 25 freetime - free time after school (numeric: from 1 - very low to 5 - very high)
# 26 goout - going out with friends (numeric: from 1 - very low to 5 - very high)
# 27 Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
# 28 Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
# 29 health - current health status (numeric: from 1 - very bad to 5 - very good)
# 30 absences - number of school absences (numeric: from 0 to 93)
#
# These grades are related with the course subject, Math or Portuguese:
# 31 G1 - first period grade (numeric: from 0 to 20)
# 31 G2 - second period grade (numeric: from 0 to 20)
# 32 G3 - final grade (numeric: from 0 to 20, output target)
#
# This project was to demonstrate how to predict student performance in secondary education (high school)
# final grade (G3) based on some given variables
########################################################################################################################

data = pd.read_csv("student-mat.csv", sep=";") #read data seperated by semi-colon
print(data.head()) #check

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]] #declare what ATTRIBUTES to use
print(data.head()) #check

predict = "G3" #LABEL \\|// what are we looking for

X = np.array(data.drop([predict], 1)) #all training data into X, minus PREDICT variable
y = np.array(data[predict]) #put LABEL into y variable

#take ATTRIBUTES into x_train and LABELS into y_train
#splitting 10% of data into test samples (0.1)
x_train, x_test,y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

'''
#find the best accurate model given the above ATTRIBUTES
best = 0
#run 30 times
for _ in range(30):
    x_train, x_test,y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)
    #training model
    linear = linear_model.LinearRegression()
    linear.fit(x_train, y_train) #fit data to get line (y=mx+b)
    accuracy = linear.score(x_test, y_test) #see how well model works
    print(accuracy) #see how accurate the variables

    #if accuracy of ran training model is better than any previous accuracy, use that model
    if (accuracy > best):
        print("added")
        best = accuracy
        #save model with pickle
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)
'''

#open model using pickle
pickle_in = open("studentmodel.pickle", "rb") #open model
linear = pickle.load(pickle_in) #load model into linear

print("Coefficent: \n", linear.coef_) #variable m in y=mx+b
print("Intercept: \n", linear.intercept_) #variable b in y=mx+b

#predict using model
predictions = linear.predict(x_test)

#print out predictions based on input
# print template:
# PREDICTION [G1 G2 studytime failures absences] actualgrade
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

p = 'G1' #can use different variables to see correlation between different points
#scatter plot
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade")
pyplot.show()