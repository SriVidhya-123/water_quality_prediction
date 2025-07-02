# Import all the necessary libraries
import pandas as pd
import numpy as np
import joblib
import streamlit as st

# Load the model and columns
#model = joblib.load("C:/Users/vidhaya/Downloads/pollution_model.pkl")
#model_cols = joblib.load("C:/Users/vidhaya/Downloads/model_columns.pkl")
model = joblib.load("pollution_model.pkl")
model_cols = joblib.load("model_columns.pkl")

# Streamlit UI
st.title("💧 Water Quality Predictor")
st.write("Predict the water pollutants based on Year and Station ID")

# User inputs
year_input = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
station_id = st.text_input("Enter Station ID", value='1')

# On Predict button click
if st.button('Predict'):
    if not station_id:
        st.warning('Please enter the station ID')
    else:
        # Prepare input
        input_df = pd.DataFrame({'year': [year_input], 'id': [station_id]})
        input_encoded = pd.get_dummies(input_df, columns=['id'])

        # Align input with model columns
        for col in model_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[model_cols]

        # Predict
        predicted_pollutants = model.predict(input_encoded)[0]
        pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']
        predicted_values = {p: round(val, 2) for p, val in zip(pollutants, predicted_pollutants)}

        # Define safety thresholds
        safe_limits = {
            'O2': 6.0,
            'NO3': 0.7,
            'NO2': 0.2,
            'SO4': 250,
            'PO4': 0.1,
            'CL': 250
        }

        # Show predictions with status
        st.subheader(f"📊 Predicted pollutant levels for Station '{station_id}' in {year_input}")
        status_data = []
        for pollutant, value in predicted_values.items():
            safe_value = safe_limits[pollutant]
            status = "✅ Safe" if value <= safe_value else "⚠️ Unsafe"
            st.write(f"{pollutant}: {value:.2f} — {status}")
            status_data.append((pollutant, value, status))

        # Create DataFrame for chart and CSV
        chart_df = pd.DataFrame(status_data, columns=["Pollutant", "Level", "Status"])
        chart_df.set_index("Pollutant", inplace=True)

        # Show bar chart
        st.bar_chart(chart_df["Level"])

        # Allow CSV download
        st.write("### 📥 Download Results as CSV")
        csv = chart_df.reset_index().to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"pollution_prediction_{station_id}_{year_input}.csv",
            mime='text/csv'
        )
