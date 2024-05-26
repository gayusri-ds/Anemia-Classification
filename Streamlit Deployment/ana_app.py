import streamlit as st
import pandas as pd
import joblib

# Load preprocessing pipeline and label encoder
preprocessing_pipeline = joblib.load(r'C:/Users/DELL/Desktop/My Projects/ANEMIA CLASSIFICATION/Preprocess pipeline/preprocessing_pipeline.pkl')
label_encoder = joblib.load(r'C:/Users/DELL/Desktop/My Projects/ANEMIA CLASSIFICATION/label encoder/label_encoder.pkl')
model = joblib.load(r'C:/Users/DELL/Desktop/My Projects/ANEMIA CLASSIFICATION/saved models/best_ensemble.pkl')



st.title("Anemia Classification")

st.write("""
This app classifies anemia based on the input data.
""")

# Define dictionary mapping numerical labels to categorical labels
label_mapping = {
    0: 'Healthy',
    1: 'Normocytic hypochromic anemia',
    2: 'Normocytic normochromic anemia',
    3: 'Iron deficiency anemia',
    4: 'Thrombocytopenia',
    5: 'Other microcytic anemia',
    6: 'Leukemia',
    7: 'Macrocytic anemia',
    8: 'Leukemia with thrombocytopenia'
}

# File upload
uploaded_file = st.file_uploader("Upload your dataset (CSV file)", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded dataset
    data = pd.read_csv(uploaded_file)
    
    st.write("Uploaded Data:")
    st.write(data)

    # Preprocess the data using the saved preprocessing pipeline
    preprocessed_data = preprocessing_pipeline.transform(data)

    # Make predictions using the loaded model
    predictions = model.predict(preprocessed_data)

    # Decode the predictions using the label mapping
    predicted_classes = [label_mapping[label] for label in predictions]

    # Add predicted classes to the dataframe
    data['Predicted Class'] = predicted_classes

    st.write("Data with Predictions:")
    st.write(data)