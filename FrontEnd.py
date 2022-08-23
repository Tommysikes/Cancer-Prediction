import numpy as np
import pandas as pd
import joblib 
import streamlit as st

model=joblib.load('c:/Users/ACER/Documents/databases/Cancer_Prediction_Model.pkl')

def Cancer_prediction(input_data):
    
    np_array = np.asarray(input_data)
    array_reshaped = np_array.reshape(1,-1)
    prediction=model.predict(array_reshaped)
    print(prediction)
    if (prediction[0] == 0) :
        return 'Cancer is Benign'
    else:
        return 'Cancer is Malignant'
def main():
    st.title('Breast Cancer Prediction Webapp')
    
    st.markdown("""
    This application performs wheather the cancer is **malignant** or **benign**""")
    radius = st.text_input("Enter The Radius")
    texture = st.text_input("Enter The texture")
    perimeter = st.text_input("Enter The perimeter")
    area = st.text_input("Enter The area")
    smoothness = st.text_input("Enter The smoothness")
    compactness = st.text_input("Enter The compactness")
    concavity = st.text_input("Enter The concavity")
    concave_points = st.text_input("Enter The concave points")
    symmetry = st.text_input("Enter The symmetry")
    fractal_dimension = st.text_input("Enter The Fractal Dimension")
    
    diagnosis = ''
    if st.button("Cancer Prediction"):
        diagnosis = Cancer_prediction([radius,texture,perimeter,area,smoothness,compactness,concavity,concave_points,
                                   symmetry,fractal_dimension])
    st.success(diagnosis)
    
    with st.container():
        st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

if __name__=='__main__':
    main()