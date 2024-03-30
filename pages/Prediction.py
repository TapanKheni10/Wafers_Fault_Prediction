import streamlit as st
import numpy as np
import os, sys
from WafersFault.pipeline import prediction

st.set_page_config(
    page_title="Prediction",
    layout="wide"
)

st.header("Wafers Defect Predictor", divider="rainbow")

st.write("""
    Please enter the requested sensor data into a comma-separated values (CSV) file, and the
    model will predict whether the wafer is faulty or not.
""")

uploaded_file = st.file_uploader(label="**Upload the File**", type=['.csv'], 
                                 help="upload the file of data over here for which you want to make prediction", 
                                )

if uploaded_file is not None:
    pred_file_dir = "artifacts/prediction"
    os.makedirs(pred_file_dir, exist_ok=True)
    pred_file_path = os.path.join(pred_file_dir, "prediction_data.csv")

    with open(pred_file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())

    obj = prediction.PredictionPipeline(pred_file_path)
    prediction_result = obj.predict()

    st.subheader("Prediction Results:")
    st.dataframe(prediction_result)

else:
    st.warning("Please upload a CSV file to make the predictions.")