import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained pipeline and feature names
pipeline = joblib.load('har_best_pipeline.joblib')
feature_names = list(pipeline.named_steps['scaler'].feature_names_in_)

# Mapping of numeric labels to HAR activity names
activity_labels = {
    1: "WALKING",
    2: "WALKING_UPSTAIRS",
    3: "WALKING_DOWNSTAIRS",
    4: "SITTING",
    5: "STANDING",
    6: "LAYING",
}

# User-friendly labels for top features (customize as needed)
feature_labels = {
    "tBodyAcc-mean()-X": "Mean Body Acceleration X (m/s²)",
    "tBodyAcc-mean()-Y": "Mean Body Acceleration Y (m/s²)",
    "tBodyAcc-mean()-Z": "Mean Body Acceleration Z (m/s²)",
    "tGravityAcc-mean()-X": "Mean Gravity Acceleration X (m/s²)",
    "tGravityAcc-mean()-Y": "Mean Gravity Acceleration Y (m/s²)",
    "tGravityAcc-mean()-Z": "Mean Gravity Acceleration Z (m/s²)",
    "tBodyGyro-mean()-X": "Mean Body Gyroscope X (rad/s)",
    "tBodyGyro-mean()-Y": "Mean Body Gyroscope Y (rad/s)",
    "tBodyGyro-mean()-Z": "Mean Body Gyroscope Z (rad/s)",
    "angle(tBodyAccMean,gravity)": "Angle Between Acceleration Mean & Gravity (deg)",
}

mode = st.sidebar.radio(
    "Choose input type:",
    ["Manual Input (Sliders)", "CSV File Upload", "Random Sensor Sample"]
)

st.title("Human Activity Recognition (HAR) Predictor")

# --- Manual sliders ---
if mode == "Manual Input (Sliders)":
    st.header("Input Features Manually")
    input_row = {fname: 0.0 for fname in feature_names}
    for fname, nice_label in feature_labels.items():
        if fname in input_row:
            input_row[fname] = st.slider(nice_label, -1.0, 1.0, 0.0)
    if st.button("Predict Activity"):
        x_df = pd.DataFrame([input_row], columns=feature_names)
        pred = pipeline.predict(x_df)[0]
        pred_name = activity_labels.get(int(pred), str(pred))
        st.success(f"Predicted Activity: {pred_name} (label {pred})")

# --- CSV Upload ---
elif mode == "CSV File Upload":
    st.header("Upload Sensor Features CSV/TXT")
    uploaded_file = st.file_uploader(
        "Upload CSV or TXT file with features (columns must match model)", type=["txt", "csv"]
    )
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception:
            df = pd.read_csv(uploaded_file, sep=r"\s+", header=None)
            df.columns = feature_names  # fallback for raw txt

        missing = set(feature_names) - set(df.columns)
        extra = set(df.columns) - set(feature_names)
        if missing:
            st.warning(f"Missing columns in uploaded file: {missing}")
        if extra:
            st.info(f"Ignoring extra columns: {extra}")

        if not missing:
            if st.button("Predict Activities"):
                preds = pipeline.predict(df[feature_names])
                pred_classes = [activity_labels.get(int(p), str(p)) for p in preds]
                df = df.reset_index().rename(columns={'index': 'ID'})
                df['Predicted Activity'] = pred_classes
                st.write(df)

# --- Random Sensor Sample ---
elif mode == "Random Sensor Sample":
    st.header("Generate & Predict Random Sensor Data")
    if st.button("Generate Random Sensor Data"):
        random_sample = {
            "tBodyAcc-mean()-X": np.random.normal(0, 0.4),
            "tBodyAcc-mean()-Y": np.random.normal(0, 0.4),
            "tBodyAcc-mean()-Z": np.random.normal(0, 0.4),
            "tGravityAcc-mean()-X": np.random.normal(0, 0.7),
            "tGravityAcc-mean()-Y": np.random.normal(0, 0.6),
            "tGravityAcc-mean()-Z": np.random.normal(9.8, 0.3),
            "tBodyGyro-mean()-X": np.random.normal(0, 0.2),
            "tBodyGyro-mean()-Y": np.random.normal(0, 0.2),
            "tBodyGyro-mean()-Z": np.random.normal(0, 0.2),
            "angle(tBodyAccMean,gravity)": np.random.normal(0, 0.05),
        }
        full_sample = {fname: 0.0 for fname in feature_names}
        for k, v in random_sample.items():
            if k in full_sample:
                full_sample[k] = v
        x_df = pd.DataFrame([full_sample], columns=feature_names)
        pred = pipeline.predict(x_df)[0]
        pred_name = activity_labels.get(int(pred), str(pred))
        st.write("Random Sensor Sample (Key Features):", pd.DataFrame([random_sample]))
        st.success(f"Predicted Activity: {pred_name} (label {pred})")

