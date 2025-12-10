from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mathematical Credit Risk Calculator (Indian Standards)
def calculate_credit_risk(input_data):
    """
    Calculate credit risk using mathematical formulas based on Indian banking standards.
    Uses RBI guidelines and common Indian credit scoring metrics.
    """
    
    # Extract data
    age = input_data.get('age', 0)
    income = input_data.get('income', 0)
    credit_rating = input_data.get('creditRating', 'Average')  # Changed from creditScore
    debt_to_income = input_data.get('debtToIncomeRatio', 0)
    employment_years = input_data.get('employmentLength', 0)
    num_accounts = input_data.get('numAccounts', 0)
    late_payments = input_data.get('latePayments', 0)
    loan_amount = input_data.get('loanAmount', 0)
    interest_rate = input_data.get('interestRate', 0)
    savings_balance = input_data.get('savingsBalance', 0)
    
    # Initialize risk score (0 to 100, higher = more risk)
    risk_score = 0
    
    # 1. Age Factor (25-40 is ideal for Indians, age risk: 10 points)
    if age < 25 or age > 60:
        risk_score += 10
    elif age < 30 or age > 55:
        risk_score += 5
    
    # 2. Income Stability (Based on Indian income levels)
    # Minimum income threshold for loan eligibility in India: ~₹150,000/year
    if income < 150000:
        risk_score += 25  # Very high risk
    elif income < 300000:
        risk_score += 15  # High risk
    elif income < 500000:
        risk_score += 8   # Medium risk
    elif income < 1000000:
        risk_score += 3   # Low risk
    # Above 1000000 - minimal risk (0 points)
    
    # 3. Credit Rating (Indian-specific categories)
    credit_rating_weight = {
        'Excellent': 0,      # CIBIL 750-900
        'Good': 5,           # CIBIL 700-749
        'Average': 15,       # CIBIL 650-699
        'Fair': 25,          # CIBIL 600-649
        'Poor': 40,          # CIBIL <600
        'No History': 30     # First-time borrower
    }
    risk_score += credit_rating_weight.get(credit_rating, 15)
    
    # 4. Debt-to-Income Ratio (Critical in India)
    # RBI guideline: Should be <50% for most lenders
    if debt_to_income > 0.70:
        risk_score += 25
    elif debt_to_income > 0.50:
        risk_score += 20
    elif debt_to_income > 0.35:
        risk_score += 10
    elif debt_to_income > 0.20:
        risk_score += 3
    # Below 0.20 is excellent (0 points)
    
    # 5. Employment Stability (Indian employment patterns)
    if employment_years < 1:
        risk_score += 15  # Unstable/new employment
    elif employment_years < 2:
        risk_score += 10
    elif employment_years < 5:
        risk_score += 5
    # 5+ years = minimal risk (0 points)
    
    # 6. Payment History (Late Payments - Critical)
    # Each late payment adds significant risk in India
    if late_payments == 0:
        payment_penalty = 0
    elif late_payments <= 2:
        payment_penalty = 10
    elif late_payments <= 5:
        payment_penalty = 20
    else:
        payment_penalty = 35
    risk_score += payment_penalty
    
    # 7. Number of Active Accounts (Too many = higher risk in India)
    if num_accounts > 10:
        risk_score += 12
    elif num_accounts > 7:
        risk_score += 8
    elif num_accounts > 4:
        risk_score += 3
    # Less than 4 accounts = 0 points
    
    # 8. Savings Buffer (Emergency fund)
    savings_to_monthly_income = (savings_balance / (income / 12)) if income > 0 else 0
    if savings_to_monthly_income < 1:  # Less than 1 month salary
        risk_score += 10
    elif savings_to_monthly_income < 3:  # Less than 3 months
        risk_score += 5
    elif savings_to_monthly_income < 6:  # 6 months
        risk_score += 2
    # 6+ months savings = 0 points
    
    # 9. Loan-to-Value Ratio (Loan amount vs income)
    ltv = (loan_amount / income * 100) if income > 0 else 0
    if ltv > 500:  # Loan > 5x annual income
        risk_score += 20
    elif ltv > 350:  # Loan > 3.5x annual income
        risk_score += 15
    elif ltv > 200:  # Loan > 2x annual income
        risk_score += 8
    elif ltv > 100:  # Loan > 1x annual income
        risk_score += 3
    # Less than 1x annual income = 0 points
    
    # 10. Interest Rate Acceptance (Higher rate = higher risk perception)
    if interest_rate > 15:
        risk_score += 8
    elif interest_rate > 12:
        risk_score += 4
    elif interest_rate > 9:
        risk_score += 1
    # Below 9% = 0 points
    
    # Cap the risk score at 100
    risk_score = min(risk_score, 100)
    
    return risk_score

def get_indian_credit_assessment(risk_score):
    """Convert risk score to Indian credit assessment"""
    if risk_score < 20:
        return {
            'rating': 'Excellent',
            'risk_level': 'EXCELLENT',
            'color': '#27ae60',
            'description': '✅ आपका क्रेडिट प्रोफाइल उत्कृष्ट है। आप सभी बैंकों से सर्वोत्तम दरों पर ऋण प्राप्त कर सकते हैं।',
            'english_desc': '✅ Your credit profile is excellent. You can get loans from all banks at the best rates.'
        }
    elif risk_score < 35:
        return {
            'rating': 'Good',
            'risk_level': 'GOOD',
            'color': '#2ecc71',
            'description': '👍 आपका क्रेडिट प्रोफाइल अच्छा है। आप आसानी से ऋण अनुमोदन प्राप्त कर सकते हैं।',
            'english_desc': '👍 Your credit profile is good. You can easily get loan approval.'
        }
    elif risk_score < 50:
        return {
            'rating': 'Average',
            'risk_level': 'AVERAGE',
            'color': '#f39c12',
            'description': '⚠️ आपका क्रेडिट प्रोफाइल औसत है। आपको उच्च ब्याज दर पर ऋण मिल सकता है।',
            'english_desc': '⚠️ Your credit profile is average. You may get loans at higher interest rates.'
        }
    elif risk_score < 70:
        return {
            'rating': 'Fair',
            'risk_level': 'FAIR',
            'color': '#e67e22',
            'description': '⚠️ आपका क्रेडिट प्रोफाइल कमजोर है। आपको अधिक ब्याज दर और सख्त शर्तें मिल सकती हैं।',
            'english_desc': '⚠️ Your credit profile is weak. You may get higher rates and stricter conditions.'
        }
    else:
        return {
            'rating': 'Poor',
            'risk_level': 'POOR',
            'color': '#e74c3c',
            'description': '❌ आपका क्रेडिट प्रोफाइल खराब है। आपको ऋण मिलना मुश्किल हो सकता है। अपने क्रेडिट प्रोफाइल में सुधार करें।',
            'english_desc': '❌ Your credit profile is poor. You may face difficulty getting loans. Improve your profile.'
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        data = request.json
        
        # Extract input data
        input_data = {
            'age': float(data.get('age', 0)),
            'income': float(data.get('income', 0)),
            'creditRating': data.get('creditRating', 'Average'),
            'debtToIncomeRatio': float(data.get('debtToIncomeRatio', 0)),
            'employmentLength': float(data.get('employmentLength', 0)),
            'numAccounts': float(data.get('numAccounts', 0)),
            'latePayments': float(data.get('latePayments', 0)),
            'loanAmount': float(data.get('loanAmount', 0)),
            'interestRate': float(data.get('interestRate', 0)),
            'savingsBalance': float(data.get('savingsBalance', 0))
        }
        
        # Calculate risk using mathematical formula
        risk_score = calculate_credit_risk(input_data)
        assessment = get_indian_credit_assessment(risk_score)
        
        return jsonify({
            'risk_score': round(risk_score, 1),
            'rating': assessment['rating'],
            'risk_level': assessment['risk_level'],
            'risk_color': assessment['color'],
            'description_hindi': assessment['description'],
            'description_english': assessment['english_desc']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/formula', methods=['GET'])
def api_formula():
    """Return the formula breakdown for transparency"""
    return jsonify({
        'formula': [
            'Age Factor: 10 points if <25 or >60',
            'Income: Up to 25 points based on annual income',
            'Credit Rating: 0-40 points (CIBIL score based)',
            'Debt-to-Income: Up to 25 points (RBI guideline <50%)',
            'Employment: Up to 15 points (Stability)',
            'Payment History: Up to 35 points (Late payments)',
            'Active Accounts: Up to 12 points (Fewer is better)',
            'Savings Buffer: Up to 10 points (Emergency fund)',
            'Loan-to-Value: Up to 20 points (Loan vs Income)',
            'Interest Rate: Up to 8 points (Rate acceptance)'
        ],
        'total': 'Risk Score out of 100',
        'methodology': 'Mathematical formula based on RBI guidelines and Indian banking standards'
    })

if __name__ == '__main__':
    print("Starting Flask app on http://localhost:8501")
    app.run(debug=False, host='0.0.0.0', port=8501, threaded=True)
