💧 Water Quality Prediction - RMS
This project is focused on predicting multiple water quality parameters using advanced machine learning techniques. It was developed during a one-month AICTE Virtual Internship sponsored by Shell in June 2025.

🌍 Project Overview
Access to clean and safe water is a growing global concern. Early and accurate prediction of key water quality metrics can support environmental monitoring and policy enforcement.

This project aims to:

Preprocess and analyze real-world water quality datasets.

Build a multi-output regression model to simultaneously predict various pollutant concentrations.

Provide a user-friendly Streamlit web app to visualize predictions and assess safety status.

🔧 Technologies Used
Python 3.12

Pandas, NumPy – Data manipulation and preprocessing

Scikit-learn – Model building with MultiOutputRegressor and RandomForestRegressor

Matplotlib, Seaborn – Data visualization

Streamlit – Web app interface for predictions

Jupyter Notebook – Exploratory analysis and experimentation

🔬 Predicted Water Quality Parameters
The model predicts the concentration levels of the following pollutants:

NH₄ – Ammonium

BOD₅ (BSK5) – Biochemical Oxygen Demand

Colloids

O₂ – Dissolved Oxygen

NO₃ – Nitrate

NO₂ – Nitrite

SO₄ – Sulfate

PO₄ – Phosphate

CL – Chloride

Each predicted value is compared against a safety threshold to determine if the level is safe or unsafe.

📊 Model Performance
Model evaluation metrics include:

R² Score – Measures prediction accuracy

Mean Squared Error (MSE) – Quantifies error in predictions

The model showed consistent and acceptable performance across all predicted parameters.

🚀 Try the App
Use the deployed Streamlit app to:

Enter a Year and Station ID

View predicted pollutant levels

Download the results as a CSV file

Instantly see whether each pollutant is Safe ✅ or Unsafe ⚠️

📁 Model Files
You can download the trained model and column encoder files here:

🔗 Download pollution_model.pkl and model_columns.pkl

These are required to run the Streamlit app.

🎓 Internship Information
Program: AICTE Virtual Internship

Sponsor: Shell

Duration: June 2025 (1 Month)

Focus: Applied Machine Learning for Environmental Sustainability


