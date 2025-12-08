import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample training dataset
data = {
    "area": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 4],
    "age": [10, 5, 8, 4, 2],
    "price": [50, 65, 80, 90, 110]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
