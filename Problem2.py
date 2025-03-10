import streamlit as st
import pandas as pd

# Load the data
def load_data():
    file_path = "university_student_dashboard_data.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Streamlit app
st.title("University Admissions and Student Satisfaction Dashboard")

# Filter by year
years = df['Year'].unique()
selected_year = st.selectbox("Select Year", years)

# Filtered data for the selected year
df_filtered = df[df['Year'] == selected_year]

# 1. Total applications, admissions, and enrollments per term
st.subheader("Total Applications, Admissions, and Enrollments per Term")
st.line_chart(df_filtered[['Term', 'Applications', 'Admitted', 'Enrolled']].set_index('Term'))

# 2. Retention Rate Trends Over Time
st.subheader("Retention Rate Trends Over Time")
st.line_chart(df_filtered[['Term', 'Retention Rate (%)']].set_index('Term'))

# 3. Student Satisfaction Scores Over Time
st.subheader("Student Satisfaction Scores Over Time")
st.line_chart(df_filtered[['Term', 'Student Satisfaction (%)']].set_index('Term'))

# 4. Enrollment Breakdown by Department
st.subheader("Enrollment Breakdown by Department")
departments = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
department_counts = df_filtered[departments].sum()

st.bar_chart(department_counts)

# 5. Comparison Between Spring and Fall Term Trends
st.subheader("Comparison Between Spring and Fall Term Trends")
df_spring = df_filtered[df_filtered['Term'] == 'Spring']
df_fall = df_filtered[df_filtered['Term'] == 'Fall']

# Applications, Admissions, and Enrollments Comparison
spring_fall_data = pd.DataFrame({
    'Spring Applications': df_spring['Applications'].reset_index(drop=True),
    'Fall Applications': df_fall['Applications'].reset_index(drop=True),
}, index=df_spring['Year'])

st.line_chart(spring_fall_data)

# 6. Insights and Key Findings
st.subheader("Key Insights and Actionable Findings")

insights = """
- **Applications, Admissions, and Enrollments**: The data shows trends in terms of applications, admissions, and enrollments.
- **Retention Rate Trends**: Some years show higher retention, possibly indicating improved student services or programs.
- **Satisfaction Trends**: Student satisfaction tends to fluctuate, and may align with retention trends.
- **Department Analysis**: Engineering and Business have higher enrollments, while Arts and Science show steadier growth.
- **Seasonal Trends (Spring vs. Fall)**: Comparing Spring and Fall terms reveals key differences in student interest and enrollment numbers.
"""
st.markdown(insights)
