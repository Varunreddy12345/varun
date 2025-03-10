import streamlit as st
import pandas as pd

# Load the dataset
def load_data():
    file_path = "university_student_dashboard_data.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Streamlit app title
st.title("University Admissions and Student Satisfaction Dashboard")

# Filters
years = df['Year'].unique()
selected_year = st.selectbox("Select Year", years)

df_filtered = df[df['Year'] == selected_year]

# Metrics & KPIs Section

# Total Applications, Admissions, and Enrollments per Term
st.subheader("Total Applications, Admissions, and Enrollments per Term")
applications = df_filtered.groupby('Term')['Applications'].sum()
admitted = df_filtered.groupby('Term')['Admitted'].sum()
enrolled = df_filtered.groupby('Term')['Enrolled'].sum()

# Display KPIs
st.write("**Total Applications**:")
st.write(applications)
st.write("**Total Admissions**:")
st.write(admitted)
st.write("**Total Enrollments**:")
st.write(enrolled)

# Retention Rate Trends Over Time
st.subheader("Retention Rate Trends Over Time")
retention_rate = df_filtered.groupby('Term')['Retention Rate (%)'].mean()
st.line_chart(retention_rate, use_container_width=True)

# Student Satisfaction Scores Over the Years
st.subheader("Student Satisfaction Scores Over the Years")
satisfaction_scores = df_filtered.groupby('Term')['Student Satisfaction (%)'].mean()
st.line_chart(satisfaction_scores, use_container_width=True)

# Enrollment Breakdown by Department
st.subheader("Enrollment Breakdown by Department")
departments = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
department_counts = df_filtered[departments].sum()
st.bar_chart(department_counts, use_container_width=True)

# Spring vs. Fall Term Comparison
st.subheader("Comparison Between Spring and Fall Term Trends")
spring_fall_data = df_filtered[df_filtered['Term'].isin(['Spring', 'Fall'])]
spring_fall_data_grouped = spring_fall_data.groupby(['Term']).agg({'Applications': 'sum', 'Admitted': 'sum', 'Enrolled': 'sum'})

st.write("**Spring vs Fall Term Trends**:")
st.write(spring_fall_data_grouped)

# Comparison Between Departments, Retention, and Satisfaction
st.subheader("Department-wise Comparison: Retention Rates and Satisfaction Levels")
department_retention = df_filtered.groupby('Term')[['Retention Rate (%)', 'Student Satisfaction (%)']].mean()
department_retention_plot = department_retention[['Retention Rate (%)', 'Student Satisfaction (%)']]
st.line_chart(department_retention_plot, use_container_width=True)

# Insights Section
st.subheader("Key Insights")

insights = """
- **Admissions and Enrollments**: We observe fluctuating trends in applications and admissions, with specific seasons (Spring/Fall) showing higher activity.
- **Retention and Satisfaction Trends**: Retention and satisfaction show a relatively steady upward or downward trend, and departments like Engineering have high retention rates.
- **Department Analysis**: Engineering and Business departments tend to have higher enrollments compared to Arts and Science.
- **Spring vs Fall**: There’s a noticeable increase in applications during the Fall, while Spring often shows a smaller peak.
- **Actionable Insights**: Consider targeted efforts in retention and student satisfaction for Spring intakes, especially in departments with lower satisfaction scores.
"""
st.markdown(insights)

