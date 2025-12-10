import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Indian Credit Risk Assessment",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for dark/light mode
st.markdown("""
    <style>
    .main {
        max-width: 800px;
        margin: 0 auto;
    }
    .header {
        text-align: center;
        padding: 20px 0;
        border-bottom: 2px solid rgba(0, 0, 0, 0.1);
        margin-bottom: 30px;
    }
    .result-card {
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        color: white;
        text-align: center;
    }
    .excellent { background-color: #27ae60; }
    .good { background-color: #2ecc71; }
    .average { background-color: #f39c12; }
    .fair { background-color: #e67e22; }
    .poor { background-color: #e74c3c; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div class="header">
        <h1>Credit Risk Assessment</h1>
        <p style="color: #666; margin-top: 10px;">
            Mathematical formula-based credit evaluation system for Indian banking standards
        </p>
    </div>
""", unsafe_allow_html=True)

# Mathematical Credit Risk Calculator
def calculate_credit_risk(input_data):
    """Calculate credit risk using mathematical formulas based on Indian banking standards."""
    
    age = input_data['age']
    income = input_data['income']
    credit_rating = input_data['creditRating']
    debt_to_income = input_data['debtToIncomeRatio']
    employment_years = input_data['employmentLength']
    num_accounts = input_data['numAccounts']
    late_payments = input_data['latePayments']
    loan_amount = input_data['loanAmount']
    interest_rate = input_data['interestRate']
    savings_balance = input_data['savingsBalance']
    
    risk_score = 0
    
    # 1. Age Factor
    if age < 25 or age > 60:
        risk_score += 10
    elif age < 30 or age > 55:
        risk_score += 5
    
    # 2. Income Stability
    if income < 150000:
        risk_score += 25
    elif income < 300000:
        risk_score += 15
    elif income < 500000:
        risk_score += 8
    elif income < 1000000:
        risk_score += 3
    
    # 3. Credit Rating
    credit_rating_weight = {
        'Excellent': 0,
        'Good': 5,
        'Average': 15,
        'Fair': 25,
        'Poor': 40,
        'No History': 30
    }
    risk_score += credit_rating_weight.get(credit_rating, 15)
    
    # 4. Debt-to-Income Ratio
    if debt_to_income > 0.70:
        risk_score += 25
    elif debt_to_income > 0.50:
        risk_score += 20
    elif debt_to_income > 0.35:
        risk_score += 10
    elif debt_to_income > 0.20:
        risk_score += 3
    
    # 5. Employment Stability
    if employment_years < 1:
        risk_score += 15
    elif employment_years < 2:
        risk_score += 10
    elif employment_years < 5:
        risk_score += 5
    
    # 6. Payment History
    if late_payments == 0:
        payment_penalty = 0
    elif late_payments <= 2:
        payment_penalty = 10
    elif late_payments <= 5:
        payment_penalty = 20
    else:
        payment_penalty = 35
    risk_score += payment_penalty
    
    # 7. Number of Active Accounts
    if num_accounts > 10:
        risk_score += 12
    elif num_accounts > 7:
        risk_score += 8
    elif num_accounts > 4:
        risk_score += 3
    
    # 8. Savings Buffer
    savings_to_monthly_income = (savings_balance / (income / 12)) if income > 0 else 0
    if savings_to_monthly_income < 1:
        risk_score += 10
    elif savings_to_monthly_income < 3:
        risk_score += 5
    elif savings_to_monthly_income < 6:
        risk_score += 2
    
    # 9. Loan-to-Value Ratio
    ltv = (loan_amount / income * 100) if income > 0 else 0
    if ltv > 500:
        risk_score += 20
    elif ltv > 350:
        risk_score += 15
    elif ltv > 200:
        risk_score += 8
    elif ltv > 100:
        risk_score += 3
    
    # 10. Interest Rate Acceptance
    if interest_rate > 15:
        risk_score += 8
    elif interest_rate > 12:
        risk_score += 4
    elif interest_rate > 9:
        risk_score += 1
    
    risk_score = min(risk_score, 100)
    return risk_score

def get_indian_credit_assessment(risk_score):
    """Convert risk score to Indian credit assessment."""
    if risk_score < 20:
        return {
            'rating': 'Excellent',
            'risk_level': 'EXCELLENT',
            'color': 'excellent',
            'description': 'Your credit profile is excellent. You can get loans from all banks at the best rates.'
        }
    elif risk_score < 35:
        return {
            'rating': 'Good',
            'risk_level': 'GOOD',
            'color': 'good',
            'description': 'Your credit profile is good. You can easily get loan approval.'
        }
    elif risk_score < 50:
        return {
            'rating': 'Average',
            'risk_level': 'AVERAGE',
            'color': 'average',
            'description': 'Your credit profile is average. You may get loans at higher interest rates.'
        }
    elif risk_score < 70:
        return {
            'rating': 'Fair',
            'risk_level': 'FAIR',
            'color': 'fair',
            'description': 'Your credit profile is weak. You may get higher rates and stricter conditions.'
        }
    else:
        return {
            'rating': 'Poor',
            'risk_level': 'POOR',
            'color': 'poor',
            'description': 'Your credit profile is poor. You may face difficulty getting loans.'
        }

# Input form
st.subheader("Enter Your Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age (Years)", min_value=18, max_value=100, value=35)
    income = st.number_input("Annual Income (₹)", min_value=0, value=500000)
    credit_rating = st.selectbox(
        "CIBIL Credit Rating",
        ["Excellent (750-900)", "Good (700-749)", "Average (650-699)", "Fair (600-649)", "Poor (Below 600)", "No History"]
    )
    dti_ratio = st.number_input("Debt-to-Income Ratio", min_value=0.0, max_value=1.0, value=0.35, step=0.01)
    employment_length = st.number_input("Employment Length (Years)", min_value=0, max_value=50, value=5)

with col2:
    num_accounts = st.number_input("Number of Active Accounts", min_value=0, max_value=20, value=4)
    late_payments = st.number_input("Late Payments (Count)", min_value=0, max_value=20, value=2)
    loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=1000000)
    interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, max_value=30.0, value=8.5)
    savings_balance = st.number_input("Savings Balance (₹)", min_value=0, value=100000)

# Auto-calculate DTI
st.markdown("---")
st.subheader("Debt-to-Income Ratio Calculation")

monthly_income = income / 12
monthly_loan = loan_amount / 12
calculated_dti = (monthly_loan / monthly_income) if monthly_income > 0 else 0

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Monthly Income", f"₹{monthly_income:,.0f}")
with col2:
    st.metric("Monthly Loan Payment", f"₹{monthly_loan:,.0f}")
with col3:
    st.metric("Calculated DTI", f"{calculated_dti:.2f}")

st.info(f"Formula: ₹{monthly_loan:,.0f} ÷ ₹{monthly_income:,.0f} = {calculated_dti:.2f}")

# Assess button
st.markdown("---")

if st.button("Assess Credit Risk", key="predict", use_container_width=True):
    # Map credit rating to value
    rating_map = {
        "Excellent (750-900)": "Excellent",
        "Good (700-749)": "Good",
        "Average (650-699)": "Average",
        "Fair (600-649)": "Fair",
        "Poor (Below 600)": "Poor",
        "No History": "No History"
    }
    
    input_data = {
        'age': age,
        'income': income,
        'creditRating': rating_map[credit_rating],
        'debtToIncomeRatio': dti_ratio,
        'employmentLength': employment_length,
        'numAccounts': num_accounts,
        'latePayments': late_payments,
        'loanAmount': loan_amount,
        'interestRate': interest_rate,
        'savingsBalance': savings_balance
    }
    
    risk_score = calculate_credit_risk(input_data)
    assessment = get_indian_credit_assessment(risk_score)
    
    # Display result
    st.markdown("---")
    st.subheader("Assessment Result")
    
    result_html = f"""
    <div class="result-card {assessment['color']}">
        <h2>{assessment['rating']}</h2>
        <h3>Risk Score: {risk_score:.1f}/100</h3>
        <p style="font-size: 16px; margin-top: 15px;">{assessment['description']}</p>
    </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)
    
    # Detailed breakdown
    st.subheader("Score Breakdown")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Key Factors:**")
        st.write(f"• Age: {age} years")
        st.write(f"• Annual Income: ₹{income:,}")
        st.write(f"• CIBIL Rating: {rating_map[credit_rating]}")
        st.write(f"• DTI Ratio: {dti_ratio:.2f}")
        st.write(f"• Employment: {employment_length} years")
    
    with col2:
        st.write("**Risk Factors:**")
        st.write(f"• Late Payments: {late_payments}")
        st.write(f"• Active Accounts: {num_accounts}")
        st.write(f"• Loan Amount: ₹{loan_amount:,}")
        st.write(f"• Interest Rate: {interest_rate}%")
        st.write(f"• Savings: ₹{savings_balance:,}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px; padding: 20px;">
    <p><strong>Assessment Methodology:</strong> This calculator uses mathematical formulas based on Reserve Bank of India guidelines 
    to evaluate 10 key financial metrics for credit risk assessment.</p>
    <p>Version 1.0 | Last Updated: December 2025</p>
</div>
""", unsafe_allow_html=True)
