import numpy as np
import joblib


def preprocessdata(Gender, Married, Dependents, Education, SelfEmployed, ApplicantIncome,
                   CoapplicantIncome, DebtConsolidationAmount, Tenor, CreditHistory,
                   PropertyArea):
    test_data = [[Gender, Married, Dependents, Education, SelfEmployed, ApplicantIncome,
                  CoapplicantIncome, DebtConsolidationAmount, Tenor, CreditHistory,
                  PropertyArea]]
    trained_model = joblib.load("model.pkl")
    prediction = trained_model.predict(test_data)

    return prediction
