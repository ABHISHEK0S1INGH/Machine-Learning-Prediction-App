# Machine Learning Prediction App

This **Machine Learning Prediction App** built with Streamlit allows users to upload a CSV file, make predictions using a pre-trained model, and visualize the results interactively. 

## Key Features

1. **File Upload & Model Prediction**:
   - Upload a CSV file containing the data for which predictions are to be made.
   - The app loads a pre-trained model (`dataXL.joblib`) and generates predictions based on the uploaded data.
   - The predicted values are appended to the original data and displayed in a table.

2. **Interactive Visualizations**:
   - **Prediction Distribution (Pie Chart)**: Displays a pie chart of prediction proportions if predictions are categorical (with limited unique values).
   - **Prediction Counts (Bar Chart)**: 
     - For **categorical data**: Shows a bar chart displaying the count of each category.
     - For **continuous data**: Displays a bar chart of predictions grouped into frequency bins.

3. **Downloadable Results**:
   - Users can download the updated dataset (including predictions) as a CSV file directly from the app.

4. **Error Handling & Flexibility**:
   - Comprehensive error handling ensures smooth operation across different types of data (categorical or continuous).
   - Step-by-step messages guide users through the process, from uploading data to visualizing predictions.

## Purpose and Benefits

This app is designed for data scientists, analysts, or anyone needing a quick and easy way to apply a machine learning model to new data, visualize predictions, and explore their distribution. The ability to download the results makes it easy to export the predictions for further analysis.

## Running the App Locally

### Prerequisites

- **Python**: Version 3.6 or higher.
- **Model File**: Ensure the pre-trained model file (`dataXL.joblib`) is placed in the same directory as your app script.
- **Required Libraries**: The app requires the following libraries:
  - `joblib`
  - `pandas`
  - `streamlit`
  - `matplotlib`
  - `seaborn`
  - `numpy`

### Steps to Run

1. **Create a Project Folder**:
   - Create a folder for your app files, including the `dataXL.joblib` model file.

2. **Save the App Script**:
   - Inside the folder, create a Python file (e.g., `app.py`) and paste the Streamlit app code into it.

3. **Install Required Libraries**:
   - Open a terminal or command prompt, navigate to your project folder, and install the necessary libraries by running:
     ```bash
     pip install joblib pandas streamlit matplotlib seaborn numpy
     ```

4. **Run the Streamlit App**:
   - In the terminal, navigate to your project directory and run:
     ```bash
     streamlit run app.py
     ```
   - This will start a local web server and provide a URL (usually `http://localhost:8501`). Open the link in your web browser to access the app.

### Using the App

1. Upload a CSV file containing the data that is compatible with the pre-trained model.
2. Click the **Predict** button to generate predictions for the uploaded data.
3. Visualize the predictions in graphical formats (pie chart for categorical data, bar chart for counts or ranges).
4. Optionally, download the dataset with predictions as a new CSV file.

### Stopping the App![Uploading Screenshot 2024-11-12 173724.png…]()


- To stop the app, press `Ctrl + C` in the terminal where Streamlit is running.

## Screenshots

Here are some screenshots of the app in action:

![App Screenshot](https://github.com/user-attachments/assets/ada9d344-ea09-4362-99ca-ad444c3afaeb)
![App Screenshot](https://github.com/ABHISHEK0S1INGH/Machine-Learning-Prediction-App/blob/c9e8ffa6581dfd572f34aa81a8100e7ed9ca3fbe/App_ScreenShot/Screenshot%202024-11-12%20173741.png)
![App Screenshot](https://github.com/ABHISHEK0S1INGH/Machine-Learning-Prediction-App/blob/c9e8ffa6581dfd572f34aa81a8100e7ed9ca3fbe/App_ScreenShot/Screenshot%202024-11-12%20173753.png)
![App Screenshot](https://github.com/ABHISHEK0S1INGH/Machine-Learning-Prediction-App/blob/c9e8ffa6581dfd572f34aa81a8100e7ed9ca3fbe/App_ScreenShot/Screenshot%202024-11-12%20173802.png)











