import pandas as pd
import matplotlib.pyplot as plt

# Data provided: This is the CSV output from query 1
data = {
    "job_id": [226942, 547382, 552322, 99305, 1021647, 168310, 731368, 310660, 1749593, 387860],
    "job_title": ["Data Analyst", "Director of Analytics", "Associate Director- Data Insights", "Data Analyst, Marketing",
                  "Data Analyst (Hybrid/Remote)", "Principal Data Analyst (Remote)", "Director, Data Analyst - HYBRID",
                  "Principal Data Analyst, AV Performance Analysis", "Principal Data Analyst", "ERM Data Analyst"],
    "job_location": ["Anywhere"] * 10,
    "job_schedule_type": ["Full-time"] * 10,
    "salary_year_avg": [650000.0, 336500.0, 255829.5, 232423.0, 217000.0, 205000.0, 189309.0, 189000.0, 186000.0, 184000.0],
    "job_posted_date": ["2023-02-20 15:13:33", "2023-08-23 12:04:42", "2023-06-18 16:03:12", "2023-12-05 20:00:40",
                        "2023-01-17 00:17:23", "2023-08-09 11:00:01", "2023-12-07 15:00:13", "2023-01-05 00:00:25",
                        "2023-07-11 16:00:05", "2023-06-09 08:01:04"],
    "company_name": ["Mantys", "Meta", "AT&T", "Pinterest Job Advertisements", "Uclahealthcareers", "SmartAsset",
                     "Inclusively", "Motional", "SmartAsset", "Get It Recruit - Information Technology"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert job_posted_date to datetime
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])

# Plotting
plt.figure(figsize=(10, 6))
plt.barh(df['job_title'], df['salary_year_avg'], color='teal')
plt.xlabel('Yearly Salary ($)')
plt.ylabel('Job Title')
plt.title('Top 10 Salaries for Data Analysts')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

