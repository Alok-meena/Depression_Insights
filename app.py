import streamlit as st
import pandas as pd
import joblib

# Load pre-trained model
model_pipeline = joblib.load('model_pipeline.pkl')

# Set up the Streamlit app
st.set_page_config(page_title="Child Depression Monitoring Tool", page_icon="🧠", layout="centered")

# Add custom CSS to style the result boxes
st.markdown("""
    <style>
        .result-box {
            padding: 20px;
            margin: 20px 0;
            background-color: red;
            border-radius: 10px;
            text-align: center;
            transition: transform 0.3s ease;  
        }

        .result-box:hover {
            transform: scale(1.1);  /* Increases the size when hovered */
        }

        .result-box h3 {
            margin-bottom: 10px;
        }
        .result-box .metric {
            font-size: 24px;
            font-weight: bold;
        }
        .success {
            color: green;
        }
        .warning {
            color: orange;
        }
        .error {
            color: red;
        }

        h1, h2, h3 {
            font-family: 'Open Sans', sans-serif;
        }

        .stButton {
            background-color: #5fa8d3;  /* Soft blue button color */
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            transition: background-color 0.3s ease;
        }

        .stButton:hover {
            background-color: #3f8a99;  /* Slightly darker shade for hover effect */
        }

        .result-box {
            padding: 20px;
            margin: 20px 0;
            background-color:red;  /* Soft Yellow background for results */
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Soft shadow effect */
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .result-box:hover {
            transform: scale(1.05);  /* Smooth scaling effect */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);  /* Enhance shadow on hover */
        }

        .stMetric {
            background-color: #fff;  /* White background for metrics */
            padding: 10px;
            margin: 10px;
            border-radius: 8px;
            border: 1px solid #ccc;  /* Light gray border for a neat appearance */
        }

        .stSelectbox, .stNumberInput {
            background-color: #ffffff;  /* White background for inputs */
            border-radius: 8px;
            border: 1px solid #ddd;  /* Light gray border */
            padding: 10px;
        }

        .stSelectbox:hover, .stNumberInput:hover {
            border-color: #5fa8d3;  /* Highlight input field border on hover */
        }

    </style>
""", unsafe_allow_html=True)

# Main header and description for parents
st.title("🧠 Child Depression Monitoring Tool for Parents")
st.write("""
This tool is designed to help parents monitor their child's mental well-being.
Please complete the form below, and answer the questionnaires for anxiety, sleepiness, and depression assessments.
The scores will be automatically calculated, and you'll receive a depression probability assessment based on the data.
""")

phq_score, gad_7_score, epworth_score = 0, 0, 0

# Form for child’s details
with st.form("Student_INFO_Form"):
    st.header("Student's Details")
    age = st.number_input("Age", min_value=10, max_value=25, value=16, step=1)
    gender = st.selectbox("Gender", options=["Male", "Female"])
    study_year = st.selectbox("Year of Study", options=["1st Year", "2nd Year", "3rd Year", "4th Year"])
    bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=22.0, step=0.1)

    # Section for PHQ-9 Score
    st.subheader("PHQ-9 Depression Severity")
    phq_responses = [
        st.radio("Little interest or pleasure in doing things?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Feeling down, depressed, or hopeless?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Trouble falling or staying asleep, or sleeping too much?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Feeling tired or having little energy?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Poor appetite or overeating?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Feeling bad about yourself—or that you are a failure?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Trouble concentrating on things, such as reading?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Moving or speaking slowly or being fidgety/restless?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Thoughts that you would be better off dead or hurting yourself?", ["Not at all", "Several days", "More than half the days", "Nearly every day"])
    ]
    
    # Section for GAD-7 Score
    st.subheader("GAD-7 Anxiety Assessment")
    gad_responses = [
        st.radio("Feeling nervous, anxious, or on edge?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Not being able to stop or control worrying?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Worrying too much about different things?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Trouble relaxing?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Being so restless that it's hard to sit still?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Becoming easily annoyed or irritable?", ["Not at all", "Several days", "More than half the days", "Nearly every day"]),
        st.radio("Feeling afraid as if something awful might happen?", ["Not at all", "Several days", "More than half the days", "Nearly every day"])
    ]
    
    # Section for Epworth Sleepiness Score
    st.subheader("Epworth Sleepiness Scale")
    epworth_responses = [
        st.radio("Sitting and reading?", ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"]),
        st.radio("Watching TV?", ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"]),
        st.radio("Sitting inactive in a public place?", ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"]),
        st.radio("As a passenger in a car for an hour?", ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"]),
        st.radio("Lying down in the afternoon?", ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"]),
        st.radio("Sitting and talking with someone?", ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"]),
        st.radio("Sitting quietly after a lunch without alcohol?", ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"]),
        st.radio("In a car while stopped in traffic?", ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"])
    ]
    
    # Calculate Scores (Added this to ensure the form submit button is processed once)
    def calculate_score(responses, labels):
        return sum([labels.index(ans) for ans in responses])

    # Submit button for the form
    submitted = st.form_submit_button("Predict Depression")

    if submitted:
        # Calculate all scores
        phq_score = calculate_score(phq_responses, ["Not at all", "Several days", "More than half the days", "Nearly every day"])
        gad_7_score = calculate_score(gad_responses, ["Not at all", "Several days", "More than half the days", "Nearly every day"])
        epworth_score = calculate_score(epworth_responses, ["Would never doze", "Slight chance of dozing", "Moderate chance of dozing", "High chance of dozing"])

        # Display calculated scores
        st.write(f"PHQ-9 Score: {phq_score}")
        st.write(f"GAD-7 Score: {gad_7_score}")
        st.write(f"Epworth Sleepiness Score: {epworth_score}")

        # Model prediction
        gender_num = 0 if gender == "Male" else 1
        study_year_map = {"1st Year": 1, "2nd Year": 2, "3rd Year": 3, "4th Year": 4}
        study_year_num = study_year_map[study_year]

        # Create DataFrame for model input
        input_data = pd.DataFrame({
            'age': [age],
            'gender': [gender_num],
            'study_year': [study_year_num],
            'bmi': [bmi],
            'phq_score': [phq_score],
            'gad_7_score': [gad_7_score],
            'epworth_score': [epworth_score]
        })

        # Make prediction
        prediction_proba = model_pipeline.predict_proba(input_data)[0, 1]
        depression_score = round(prediction_proba * 10, 1)

        # Display prediction results with styled boxes
        st.subheader("Depression Prediction Results")
        st.write(f"Based on the inputs provided, here is the analysis for your child:")

        # Display results in yellow boxes
        st.markdown(f"""
            <div class="result-box">
                <h3>Depression Probability</h3>
                <p class="metric">{prediction_proba * 100:.2f} %</p>
            </div>
            <div class="result-box">
                <h3>Depression Score (0-10 Scale)</h3>
                <p class="metric">{depression_score}</p>
            </div>
        """, unsafe_allow_html=True)

        if depression_score < 3:
            st.markdown('<p class="success">Child is likely to be mentally healthy.</p>', unsafe_allow_html=True)
        elif depression_score < 7:
            st.markdown('<p class="warning">Child is showing moderate signs of depression.</p>', unsafe_allow_html=True)
        else:
            st.markdown('<p class="error">Child is showing high signs of depression. Immediate attention is recommended.</p>', unsafe_allow_html=True)
