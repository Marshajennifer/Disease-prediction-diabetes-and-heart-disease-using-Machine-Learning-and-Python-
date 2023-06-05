import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('C:/Users/HP/hackathon/diabetes_model.sav','rb'))
heart_disease_model=pickle.load(open('C:/Users/HP/hackathon/heart_disease_model.sav','rb'))


with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0)
    
    

if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    original_title = '<p style="font-family:Courier; color:Red; font-weight:bold; font-size: 20px;">***All fields are mandatory***</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    
    
    col1, col2, col3 = st.columns((5,5,5))
#     st.markdown("""
#     <style>
#     [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
#         gap: 0rem;
#     }
#     </style>
#     """,unsafe_allow_html=True)
# with st.container():
#     col1, col2 = st.columns(2)
#     with col1:
#         st.write('Caption for first chart')
#     with col2:
#         st.line_chart((0,1), height=100)
    
    with col1:
        gender = st.text_input('Gender(Enter 0 for Female, 1 for Male)')
        st.markdown("")
        st.markdown("")
#         st.text("")
        
    with col2:
        age = st.text_input('Age of Person')
#         st.markdown("")
    
    with col3:
        hypertension = st.text_input('Hypertension(Blood Pressure)')
        st.markdown("")
        st.markdown("")
        st.markdown("")
    
    with col1:
        heart_disease = st.text_input('Heart disease history(If Yes enter 1, If No enter 0)')
        st.markdown("")
    
    with col2:
        smoking_history = st.text_input('Smoking history(Enter correct digits; No_info:0, Current:1, Ever:2, Former:3, Never:4)')
        st.markdown("")
        st.markdown("")
        st.markdown("")
    
    with col3:
        bmi = st.text_input('BMI value(Body mass index)')
        st.markdown("")
    
    with col1:
        HbA1c_level = st.text_input('HbA1c level (Avg blood glucose level of past 3 months)')
        st.markdown("")
    
    with col2:
        blood_glucose_level = st.text_input('Blood glucose level')
        st.markdown("")
    
    
   
    diab_diagnosis = ''
    
    

    try:
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]])
            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
        st.success(diab_diagnosis)
    except ValueError:
        st.error("Please enter a valid input. All fields are mandatory")
     


    st.write(f'''
    <a target="_self" href="http://localhost/find/">
        <button>
            Find Hospitals
        </button>
    </a>
    ''',
    unsafe_allow_html=True
    )




if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    original_title = '<p style="font-family:Courier; color:Red; font-weight:bold; font-size: 20px;">***All fields are mandatory***</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        age = st.text_input('Age')
        
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        sex = st.text_input('Sex(Enter 0 for Female, 1 for Male)')
        
    with col3:
        cp = st.text_input('Chest Pain types(Enter correct digits; 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic)')
        
    with col1:
        st.markdown("")
        trestbps = st.text_input('Resting Blood Pressure(in mm Hg)')
        
    with col2:
        chol = st.text_input('Cholestoral (cholestoral in mg/dl fetched via BMI sensor)')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl(1 = true; 0 = false)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (Enter correct digits; 0: normal, 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), 2: showing probable or definite left ventricular hypertrophy by Estes criteria)')
        
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        exang = st.text_input('Exercise Induced Angina(1 = yes; 0 = no)')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Number of major vessels (0-3)')
        
    with col1:
        thal = st.text_input('maximum heart rate achieved(0 = normal; 1 = fixed defect; 2 = reversable defect)')
        
        
     
     
    
    heart_diagnosis = ''
    
  
    try:
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)
    except ValueError:
        st.error("Please enter a valid input. All fields are mandatory")
        
    st.write(f'''
    <a target="_self" href="http://localhost/find/">
        <button>
            Find Hospitals
        </button>
    </a>
    ''',
    unsafe_allow_html=True
    )
        
    
    




