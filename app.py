from logging import debug
from flask import Flask, render_template, request
import utils
from utils import preprocessdata

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form.get('Gender')
        Married = request.form.get('Married')
        Dependents = request.form.get('Dependents')
        Education = request.form.get('Education')
        Self_Employed = request.form.get('SelfEmployed')
        ApplicantIncome = request.form.get('ApplicantIncome')
        CoapplicantIncome = request.form.get('CoapplicantIncome')
        DebtConsolidationAmount = request.form.get('DebtConsolidationAmount')
        Tenor = request.form.get('Tenor')
        CreditHistory = request.form.get('CreditHistory')
        PropertyArea = request.form.get('PropertyArea')

        if not Gender or not Married or not Dependents or not Education or not Self_Employed or not ApplicantIncome or not CoapplicantIncome or not DebtConsolidationAmount or not Tenor or not CreditHistory or not PropertyArea:
            missing_fields = True
            return render_template('predict.html', missing_fields=missing_fields)

    prediction = utils.preprocessdata(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome,
                                      CoapplicantIncome, DebtConsolidationAmount, Tenor, CreditHistory,
                                      PropertyArea)
    missing_fields = False
    return render_template('predict.html', prediction=prediction, missing_fields=missing_fields)


if __name__ == '__main__':
    app.run(debug=True)
