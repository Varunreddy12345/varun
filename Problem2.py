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
applications = df_filtered.groupby('Term')['Applications'].sum()
admitted = df_filtered.groupby('Term')['Admitted'].sum()
enrolled = df_filtered.groupby('Term')['Enrolled'].sum()

# Plotting the data using Streamlit line chart
st.line_chart(df_filtered[['Applications', 'Admitted', 'Enrolled']].groupby(df_filtered['Term']).sum())

# Retention and Satisfaction Trends
st.subheader("Retention Rate and Student Satisfaction")
retention_rate = df_filtered.groupby('Term')['Retention Rate (%)'].mean()
satisfaction_scores = df_filtered.groupby('Term')['Student Satisfaction (%)'].mean()

# Plotting the data using Streamlit line chart
st.line_chart(pd.DataFrame({
    'Retention Rate': retention_rate,
    'Satisfaction': satisfaction_scores
}))

# Enrollment Breakdown by Department
st.subheader("Enrollment Breakdown by Department")
departments = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
department_counts = df_filtered[departments].sum()

# Plotting the data using Streamlit bar chart
st.bar_chart(department_counts)

# Insights and Summary
st.subheader("Key Insights")
insights = """
- **Admissions Trends**: Applications and enrollments fluctuate across terms, with a notable difference between Spring and Fall.
- **Retention & Satisfaction**: Retention and satisfaction trends indicate overall stability but show variations by year.
- **Department Analysis**: Engineering and Business typically see the highest enrollments, while Arts and Science have steadier numbers.
- **Spring vs. Fall**: Comparing across terms reveals key differences in admission rates and student preferences.
"""
st.markdown(insights)
