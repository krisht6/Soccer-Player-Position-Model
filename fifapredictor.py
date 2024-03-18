import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('players_20.csv')
# reading the excel file using panda's read function
df = df[df['player_positions'] != 'GK'] 
# removing the gks from the dataFrame

df['position'] = df['player_positions'].apply(lambda x: 'defense' if 'B' in x else 'midfield')
# only using defensive players and midfielders. B is in all defensive postions (RB, RWB, CB, LWB, LB)


df = df[['position', 'shooting','passing','dribbling','defending']]
# using the 4 most important stats with position

X  = df.drop('position', axis=1).values 
# converting features into Numpy array by calling .value on the dataFrame
y  = df['position'].values 
# taking the label/category into a Numpy array

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, stratify=y) 
# features and labels are defined, pass them into training function


knn = KNeighborsClassifier(n_neighbors=10)
knn.fit(X_train, y_train)
print(knn.score(X_test, y_test)) 

# tests with different k-neighbor cluster sizes
# 1 = 83.05%
# 3 = 85.64%
# 5 = 85.90%
# 10 = 86.79%
# 15 = 87.50%
# 30 = 87.61%
# 100 = 87.61%

# based on just the selected categories of shooting, passing, dribbling, defending:
# the max accuracy for predicting postions was ~87%

# predict new players
n_vidic = np.array([[39,55,51,84]])
s_gerrard= np.array([[83,85,75,70]])
# importing the stats for new players Vidic and Gerrard (4 stats in order)
print(knn.predict(s_gerrard))
print(knn.predict(n_vidic))
# correctly printed midfield for Gerrard and defense for Vidic

grealish = np.array([[76,81,89,58]])
print(knn.predict(grealish))
# correctly predicted jack grealish as a midfielder 

cash = np.array([[66,71,75,77]])
print(knn.predict(cash))
# correctly predicted matty cash as a midfielder 
