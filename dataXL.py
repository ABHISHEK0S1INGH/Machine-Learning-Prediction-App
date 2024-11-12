from joblib import load
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the trained model
model = load('dataXL.joblib')

# Set up the Streamlit app title and description
st.title("Machine Learning Prediction App")
st.markdown("### Upload your CSV file for predictions and see the results instantly with summary visualizations.")

# Use a form to keep the file uploader and button aligned in a single row
with st.form(key="upload_form"):
    st.write("### Step 1: Upload your CSV file")

    col1, col2 = st.columns([5, 1])

    # Place the file uploader in the first column and the submit button in the second
    with col1:
        uploaded_file = st.file_uploader("Choose a CSV file for prediction", type="csv")

    with col2:
        submit = st.form_submit_button("Predict")

# Check if file is uploaded and submit button is clicked
if uploaded_file is not None and submit:
    try:
        # Read the CSV file
        data = pd.read_csv(uploaded_file)

        # Display an initial message about the file upload success
        st.success("File uploaded successfully!")
        st.write("### Step 2: Review Your Data and Predictions")

        # Make predictions
        predictions = model.predict(data)  # Assuming data is in the correct format

        # Append predictions as a new column to the DataFrame
        data['Prediction'] = predictions

        # Display the data with predictions in an expanded view
        st.dataframe(data)

        # Visualization 1: Prediction Distribution (Pie Chart)
        st.write("### Prediction Category Distribution (Pie Chart)")
        if len(np.unique(predictions)) <= 10:  # For categorical or limited unique values
            prediction_counts = pd.Series(predictions).value_counts()
            fig, ax = plt.subplots()
            ax.pie(prediction_counts, labels=prediction_counts.index, autopct='%1.1f%%', startangle=90)
            ax.set_title("Distribution of Prediction Categories")
            st.pyplot(fig)
        else:
            st.write("Pie chart is only available for categorical predictions with limited unique values.")

        # Visualization 2: Prediction Counts (Bar Chart)
        st.write("### Prediction Counts (Bar Chart)")
        if len(np.unique(predictions)) <= 10:  # For categorical predictions
            fig, ax = plt.subplots()
            sns.countplot(x=predictions, ax=ax)
            ax.set_title("Prediction Counts by Category")
            ax.set_xlabel("Prediction")
            ax.set_ylabel("Count")
            st.pyplot(fig)
        else:
            # For continuous predictions, create bins and show a bar chart of counts
            bins = np.linspace(predictions.min(), predictions.max(), 10)  # 10 bins
            binned_predictions = pd.cut(predictions, bins=bins)
            binned_counts = pd.value_counts(binned_predictions).sort_index()

            fig, ax = plt.subplots()
            binned_counts.plot(kind="bar", ax=ax)
            ax.set_title("Prediction Counts by Range")
            ax.set_xlabel("Prediction Range")
            ax.set_ylabel("Count")
            st.pyplot(fig)

        # Add option to download results
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Predictions as CSV",
            data=csv,
            file_name="predictions.csv",
            mime="text/csv"
        )

    except ValueError as e:
        st.error(f"Error in input data: {e}")
else:
    st.info("Please upload a CSV file to start the prediction process.")
