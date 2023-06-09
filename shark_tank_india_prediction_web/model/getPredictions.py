import pickle

model = pickle.load(open('shark_tank_india_prediction_web/model/shark_tank_india_model.sav', 'rb'))

def getPredictions(industry, y_rev, m_rev, g_margin, n_margin, og_ask, og_equity, og_value, patents):
    return model.predict([[industry, y_rev, m_rev, g_margin, n_margin, og_ask, og_equity, og_value, patents]])