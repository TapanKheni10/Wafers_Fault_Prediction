import streamlit as st
from PIL import Image

## set the streamlit page configuration
st.set_page_config(
    page_title="Home_Page",
    layout="wide"
)

st.title("Wafers Fault Prediction", help="predicting whether a wafer is faulty or not")

logo = Image.open('static/logo.png')
left_col, center_col, right_col = st.columns(3)

with center_col:
    st.write("\n")
    st.image(logo)

st.header("Precision at the Nanoscale: Machine Learning for Flawless Chips", divider="rainbow")

st.write("""
    In the semiconductor industry, ensuring the quality of wafers is crucial for maintaining high product standards and minimizing defects. 
    This project aims to develop a machine learning-based system for predicting whether a particular wafer is faulty or not based on data collected 
    from numerous sensors placed on the wafer during the manufacturing process.
""")

st.header("How it works?", divider="rainbow")

st.write("""
    The system utilizes advanced machine learning algorithms to analyze and learn from the complex patterns present in the sensor data, 
    which includes readings from approximately 500 sensors monitoring various parameters. By leveraging this vast amount of data, 
    the model can accurately classify wafers as faulty or non-faulty, enabling early detection and prevention of defective products.
""")

st.write("""
    Key Features:
    - Comprehensive data preprocessing and feature engineering techniques to ensure optimal model performance.
    - Application of state-of-the-art machine learning algorithms, such as Random Forests, Gradient Boosting Machines, or Deep Neural Networks, for accurate fault prediction.
    - Robust model evaluation and validation strategies, including cross-validation and ensembling, to enhance prediction accuracy.
    - User-friendly interface for easy integration with existing wafer production systems.
         
    The successful implementation of this project will not only improve the overall quality of wafer production but also contribute to cost savings 
    by reducing the wastage of resources on defective products. Additionally, it will provide valuable insights into the manufacturing process, 
    enabling further optimization and process improvements.
         
    Stay tuned for updates as we continue to refine and enhance this innovative machine learning solution for wafer fault detection.
""")

