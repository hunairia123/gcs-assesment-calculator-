import streamlit as st

st.set_page_config(
    page_title="GCS Calculator",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Glasgow Coma Scale (GCS) Calculator")
st.write("Select the patient's best responses below to calculate the GCS score.")

st.divider()

# Eye Opening
st.subheader("1. Eye Opening (E)")

eye = st.radio(
    "Select the best eye-opening response:",
    [
        "4 - Spontaneous",
        "3 - To speech",
        "2 - To pain",
        "1 - No eye opening"
    ]
)

# Verbal Response
st.subheader("2. Verbal Response (V)")

verbal = st.radio(
    "Select the best verbal response:",
    [
        "5 - Oriented",
        "4 - Confused conversation",
        "3 - Inappropriate words",
        "2 - Incomprehensible sounds",
        "1 - No verbal response"
    ]
)

# Motor Response
st.subheader("3. Motor Response (M)")

motor = st.radio(
    "Select the best motor response:",
    [
        "6 - Obeys commands",
        "5 - Localizes pain",
        "4 - Withdraws from pain",
        "3 - Abnormal flexion",
        "2 - Abnormal extension",
        "1 - No motor response"
    ]
)

# Extract scores
eye_score = int(eye.split(" ")[0])
verbal_score = int(verbal.split(" ")[0])
motor_score = int(motor.split(" ")[0])

total_score = eye_score + verbal_score + motor_score

st.divider()

st.header("GCS Result")

st.metric(
    label="Total GCS Score",
    value=f"{total_score}/15"
)

st.write(
    f"**E{eye_score} + V{verbal_score} + M{motor_score} = {total_score}/15**"
)

# Interpretation
if total_score >= 13:
    st.success("Mild impairment: GCS 13–15")
elif total_score >= 9:
    st.warning("Moderate impairment: GCS 9–12")
else:
    st.error("Severe impairment: GCS 3–8")

st.divider()

st.info(
    "⚠️ This calculator is for educational and clinical-support purposes only. "
    "It should not replace assessment by a qualified healthcare professional."
)

st.caption("Glasgow Coma Scale Calculator")
