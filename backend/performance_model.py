import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class PerformanceModel:

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.model = LinearRegression()

    def train_model(self):
        X = self.data.drop('performance_metric', axis=1)
        y = self.data['performance_metric']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f'Model trained with MSE: {mse}')

    def predict(self, new_data):
        return self.model.predict(new_data)

# Example Usage:
# df = pd.read_csv('athlete_data.csv')
# performance_model = PerformanceModel(df)
# performance_model.train_model()
