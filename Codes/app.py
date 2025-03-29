import os
import streamlit as st
import pandas as pd
import pickle as pk


def Loan_Approval():
    no_of_dep = st.slider('Choose No of dependents', 0, 5)
    grad = st.selectbox('Choose Education',['Graduated','Not Graduated'])
    self_emp = st.selectbox('Self Emoployed ?',['Yes','No'])
    Annual_Income = st.slider('Choose Annual Income', 0, 10000000)
    Loan_Amount = st.slider('Choose Loan Amount', 0, 10000000)
    Loan_Dur = st.slider('Choose Loan Duration', 0, 20)
    Cibil = st.slider('Choose Cibil Score', 0, 1000)
    Assets = st.slider('Choose Assets', 0, 10000000)


    
    if grad =='Graduated':
        grad_s =0
    else:
        grad_s = 1

    if self_emp =='No':
        emp_s =0
    else:
        emp_s = 1


    if st.button("Predict"):
        pred_data = pd.DataFrame([[no_of_dep,grad_s,emp_s,Annual_Income,Loan_Amount,Loan_Dur,Cibil,Assets]],
                            columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Assets'])
        pred_data = scaler.transform(pred_data)
        predict = model.predict(pred_data)
        if predict[0] == 1:
            st.snow()
            st.markdown('Loan Is Approved')
        else:
            st.markdown('Loan Is Rejected')
            
def check_cibil():
    cibil = st.slider(0,1000)
    if cibil >=800:
        st.write("You will get the loan with minimum interest rate")



model_path = os.path.join(os.getcwd(), 'model.pkl')  
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pk.load(f)

model_path = os.path.join(os.getcwd(), 'scaler.pkl') 
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pk.load(f)

st.set_page_config(
    page_title="Loan Navigator", 
    page_icon="🏦"
    )
st.sidebar.title('Loan Approval Prediction System')
app_mode = st.sidebar.selectbox('select page',['Home','Personal Loan','Education Loan','Home Loan','Medical Loan','Vehicle Loan'])


if(app_mode=='Home'):
    st.title("🏦 Loan Approval Prediction System")

    from PIL import Image
    img_path = "path/to/image.png"  
    if os.path.exists(img_path):
        st.image(img_path)

    st.header('Loan Navigator')


    st.write(
        "Welcome to the Loan Approval Prediction System! Our platform helps you determine the likelihood of your loan approval "
        "based on key financial and personal details. Using machine learning, we analyze your information and provide "
        "an instant prediction. This tool is designed to assist individuals and financial institutions in making informed "
        "loan decisions quickly and efficiently. Simply enter your details, and let our AI-powered model do the rest!"
    )
    
    st.write(
        "\n This is a group project created by Hari Milan Arora, Himanshu Singh Bisht, Gulshan Singh and Yukta Kakkar"
    )
    
    st.write(
        "\n Select the type of loan from the dropdown to apply"
    )
    st.write("---")
    
    
elif(app_mode == "Personal Loan"):
    Loan_Approval()
    check_cibil()
elif(app_mode == "Education Loan"):
    Loan_Approval()
    check_cibil()
elif(app_mode == "Home Loan"):
    Loan_Approval()
    check_cibil()
elif(app_mode == "Medical Loan"):
    Loan_Approval()
    check_cibil()
elif(app_mode == "Vehicle Loan"):
    Loan_Approval()
    check_cibil()
