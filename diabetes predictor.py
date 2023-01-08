import pandas as pd

df = pd.read_excel("sugar.xlsx")
sugar = df.copy()

# Finding if 0 values exist
sugar1 = sugar[sugar['Glucose'] == 0]
sugar1

# Removing those 0 values
sugar = sugar[sugar['Glucose'] != 0]
sugar

X = sugar.iloc[:, [1,2,4,5,6,7]]      #Feature (Dependent variables)
X

y = sugar.iloc[:, [9]]                 # Outcomes / Classes
y

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier

# Create a KNN classifier with 3 neighbors
knn = KNeighborsClassifier(n_neighbors=11)

# Train the classifier using the training data
knn.fit(X_train, y_train)

# Test the classifier on the testing data
accuracy = knn.score(X_test, y_test)

print("Accuracy: {:.2f} %".format(accuracy *100))
