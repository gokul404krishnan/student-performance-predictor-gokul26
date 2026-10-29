
import streamlit as st

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Predictor")
st.write("Predict student academic performance")

st.sidebar.header("Student Details")

name = st.sidebar.text_input("Student Name")

attendance = st.sidebar.slider(
    "Attendance (%)", 0, 100, 75
)

study_hours = st.sidebar.slider(
    "Daily Study Hours", 0, 12, 3
)

previous_marks = st.sidebar.slider(
    "Previous Exam Marks", 0, 100, 60
)

internal_marks = st.sidebar.slider(
    "Internal Marks", 0, 100, 60
)

assignments = st.sidebar.slider(
    "Assignment Score", 0, 100, 70
)

st.subheader("📊 Student Performance Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Attendance", f"{attendance}%")
col2.metric("Study Hours", f"{study_hours} hrs/day")
col3.metric("Previous Marks", f"{previous_marks}/100")

if st.button("Predict Performance"):
    predicted_marks = (
        previous_marks * 0.35
        + internal_marks * 0.25
        + assignments * 0.15
        + attendance * 0.15
        + min(study_hours / 12, 1) * 100 * 0.10
    )

    st.subheader("Prediction Result")

    st.metric(
        "Estimated Marks",
        f"{predicted_marks:.1f}/100"
    )

    if predicted_marks >= 75:
        st.success("Good Performance 🌟")
    elif predicted_marks >= 50:
        st.warning("Average Performance 📚")
    else:
        st.error("Needs Improvement 💪")

    if attendance < 75:
        st.info("Suggestion: Improve your attendance.")

    if study_hours < 2:
        st.info("Suggestion: Increase daily study time.")

    if not name.strip():
        st.info("Enter the student's name for identification.")
