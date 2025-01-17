import pandas as pd
import matplotlib.pyplot as plt

# Data provided: This is the CSV output from query 2
data = {
    "job_id": [552322, 552322, 552322, 552322, 552322, 552322, 552322, 552322, 552322, 552322, 552322, 552322, 552322, 99305, 99305, 99305, 99305, 99305, 1021647, 1021647, 1021647, 1021647, 1021647, 168310, 168310, 168310, 168310, 168310, 168310, 168310, 168310, 168310, 731368, 731368, 731368, 731368, 731368, 731368, 731368, 731368, 731368, 731368, 731368, 731368, 731368, 731368, 310660, 310660, 310660, 310660, 310660, 310660, 310660, 310660, 1749593, 1749593, 1749593, 1749593, 1749593, 1749593, 1749593, 1749593, 1749593, 387860, 387860, 387860],
    "job_title": ["Associate Director- Data Insights"]*13 + ["Data Analyst, Marketing"]*5 + ["Data Analyst (Hybrid/Remote)"]*5 + ["Principal Data Analyst (Remote)"]*9 + ["Director, Data Analyst - HYBRID"]*14 + ["Principal Data Analyst, AV Performance Analysis"]*8 + ["Principal Data Analyst"]*9 + ["ERM Data Analyst"]*3,
    "salary_year_avg": [255829.5]*13 + [232423.0]*5 + [217000.0]*5 + [205000.0]*9 + [189309.0]*14 + [189000.0]*8 + [186000.0]*9 + [184000.0]*3,
    "skills": ["sql", "python", "r", "azure", "databricks", "aws", "pandas", "pyspark", "jupyter", "excel", "tableau", "power bi", "powerpoint",
               "sql", "python", "r", "hadoop", "tableau",
               "sql", "crystal", "oracle", "tableau", "flow",
               "sql", "python", "go", "snowflake", "pandas", "numpy", "excel", "tableau", "gitlab",
               "sql", "python", "azure", "aws", "oracle", "snowflake", "tableau", "power bi", "sap", "jenkins", "bitbucket", "atlassian", "jira", "confluence",
               "sql", "python", "r", "git", "bitbucket", "atlassian", "jira", "confluence",
               "sql", "python", "go", "snowflake", "pandas", "numpy", "excel", "tableau", "gitlab",
               "sql", "python", "r"]
}
# Create DataFrame
df = pd.DataFrame(data)

# Limiting the data to the top most frequent skills
top_skills = skill_counts.head(10)

# Plotting
plt.figure(figsize=(10, 6))
top_skills.plot(kind='barh', color='teal')
plt.xlabel('Frequency')
plt.ylabel('Skills')
plt.title('Skill Count for Top 10 Paying Data Analyst Jobs')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()



