import joblib
from sklearn.pipeline import Pipeline


polynomial_features = joblib.load('utils/polynomial_features.pkl')
linear_regression = joblib.load('utils/best_regressor.pkl')
#tree_regressor = joblib.load('utils/flow-rod_regressor.pkl')

modelo_rod = Pipeline([
    ('poly', polynomial_features),
    ('regression', linear_regression)
])

def predict_rod(x1, x2, x3):
    prediction = modelo_rod.predict([[x1, x2, x3]]) 
    return prediction[0]

def predict_rod_batch(df):
    predictions = modelo_rod.predict(df)
    return predictions

"""def predict_flow(rod):
    flow = tree_regressor.predict([[rod, rod**2]])
    return flow[0]"""