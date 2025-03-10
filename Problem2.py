import streamlit as st
import pandas as pd

# Load data
def load_data():
    file_path = "university_student_dashboard_data.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Streamlit app
st.title("University Admissions and Student Satisfaction Dashboard")

# Filters
years = df['Year'].unique()
selected_year = st.selectbox("Select Year", years)

df_filtered = df[df['Year'] == selected_year]

# Applications, Admissions, and Enrollments over time
st.subheader("Applications, Admissions, and Enrollments")
applications = df_filtered['Applications']
admitted = df_filtered['Admitted']
enrolled = df_filtered['Enrolled']
df_filtered['Applications'] = applications
df_filtered['Admitted'] = admitted
df_filtered['Enrolled'] = enrolled

st.line_chart(df_filtered[['Applications', 'Admitted', 'Enrolled']], use_container_width=True)

# Retention and Satisfaction Trends
st.subheader("Retention Rate and Student Satisfaction")
retention_rate = df_filtered['Retention Rate (%)']
student_satisfaction = df_filtered['Student Satisfaction (%)']
df_filtered['Retention Rate (%)'] = retention_rate
df_filtered['Student Satisfaction (%)'] = student_satisfaction

st.line_chart(df_filtered[['Retention Rate (%)', 'Student Satisfaction (%)']], use_container_width=True)

# Enrollment Breakdown by Department
st.subheader("Enrollment Breakdown by Department")
departments = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
department_counts = df_filtered[departments].sum()

st.bar_chart(department_counts, use_container_width=True)

# Insights and Summary
st.subheader("Key Insights")
insights = """
- **Admissions Trends**: Applications and enrollments fluctuate across terms, with a notable difference between Spring and Fall.
- **Retention & Satisfaction**: Retention and satisfaction trends indicate overall stability but show variations by year.
- **Department Analysis**: Engineering and Business typically see the highest enrollments, while Arts and Science have steadier numbers.
- **Spring vs. Fall**: Comparing across terms reveals key differences in admission rates and student preferences.
"""
st.markdown(insights)
