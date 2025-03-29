import os
import streamlit as st
import pandas as pd
import pickle as pk
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression

def check_cibil():
    cibil = st.slider('Choose Cibil Score', 0, 1000)
    if cibil >= 800:
        st.markdown("You will get the loan with minimum interest rate")
    elif 800 > cibil >= 700:
        st.markdown("You will get the loan with average interest rate")
    elif 700 > cibil >= 550:
        st.markdown("You will get the loan with above average interest rate")
    else:
        st.markdown("You will get the loan with maximum interest rate")

def Loan_Approval():
    model_path = os.path.join(os.getcwd(), 'model.pkl')  
    scaler_path = os.path.join(os.getcwd(), 'scaler.pkl') 

    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            model = pk.load(f)  
    
    if os.path.exists(scaler_path):
        with open(scaler_path, 'rb') as f1:
            scaler = pk.load(f1)  
    else:
        st.error("Scaler file not found! Please train and save the scaler first.")
        return

    no_of_dep = st.slider('Choose No of dependents', 0, 5)
    grad = st.selectbox('Choose Education', ['Graduated', 'Not Graduated'])
    self_emp = st.selectbox('Self Employed?', ['Yes', 'No'])
    Annual_Income = st.slider('Choose Annual Income', 0, 10000000)
    Loan_Amount = st.slider('Choose Loan Amount', 0, 10000000)
    Loan_Dur = st.slider('Choose Loan Duration (in years)', 0, 20)
    check_cibil()
    Assets = st.slider('Choose Assets Value', 0, 10000000)

    grad_s = 0 if grad == 'Graduated' else 1
    emp_s = 0 if self_emp == 'No' else 1

    pred_data = pd.DataFrame([[no_of_dep, grad_s, emp_s, Annual_Income, Loan_Amount, Loan_Dur, Assets]],
                            columns=['no_of_dependents', 'education', 'self_employed', 'income_annum', 'loan_amount', 'loan_term', 'Assets'])

    pred_data_scaled = scaler.transform(pred_data)

    poly = PolynomialFeatures(degree=2)  
    pred_data_poly = poly.fit_transform(pred_data_scaled)

    predict = model.predict(pred_data_poly)

    if st.button("Predict"):
        if predict[0] >= 0.5:  
            st.snow()
            st.markdown('✅ Loan Is Approved')
        else:
            st.markdown('❌ Loan Is Rejected')

st.set_page_config(
    page_title="Loan Navigator", 
    page_icon="🏦"
)
st.sidebar.title('Loan Approval Prediction System')

app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Personal Loan', 'Education Loan', 'Home Loan', 'Medical Loan', 'Vehicle Loan'])

if app_mode == 'Home':
    st.title("🏦 Loan Approval Prediction System")

    from PIL import Image
    img_path = "path/to/image.png"  
    if os.path.exists(img_path):
        st.image(img_path)

    st.header('Loan Navigator')
    st.write(
        "Welcome to the Loan Approval Prediction System! Our platform helps you determine the likelihood of your loan approval "
        "based on key financial and personal details. Using machine learning, we analyze your information and provide "
        "an instant prediction."
    )
    
    st.write("\n This is a group project created by Hari Milan Arora, Himanshu Singh Bisht, Gulshan Singh, and Yukta Kakkar")
    st.write("\n Select the type of loan from the dropdown to apply")
    st.write("---")

elif app_mode in ["Personal Loan", "Education Loan", "Home Loan", "Medical Loan", "Vehicle Loan"]:
    Loan_Approval()
