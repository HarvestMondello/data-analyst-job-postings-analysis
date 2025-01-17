
# Introduction
Welcome to my SQL project. In this project I will look at the US data job market with a focus on data analytics roles. This project will explore top paying jobs, in demand tools, and where high demand meets high salaries for data analytics.

See the SQL queries here: [queries folder](/queries/)

# Background
At the time of this project I was in the market for a data analytics position and I wanted to understand the data analyst job market better. 

In order to make my job search more targeted and more effected. I intended to discover which skills are paid the most, what analysis and visualation tools arein demand., 

The data for this analysis is from Luke Barousse’s SQL Course (https://www.lukebarousse.com/sql). The data includes details on job titles, salaries, locations, and required skills. 

The questions I wanted to answer through my SQL queries were:

1. What are the top-paying data analyst jobs?
2. What skills are required for these top-paying jobs?
3. What skills are most in demand for data analysts?
4. Which skills are associated with higher salaries?
5. What are the most optimal skills to learn for a data analyst looking to maximize job market value?

# Tools I used
In this project, I utilized a variety of tools to conduct my analysis:

- **SQL** (Structured Query Language): Enabled me to interact with the database, extract insights, and answer my key questions through queries.
- **PostgreSQL**: As the database management system, PostgreSQL allowed me to store, query, and manipulate the job posting data.
- **Visual Studio Code** (VS Code): This open-source administration and development platform helped me manage the database and execute SQL queries.
- **Python** In VS Code: Enabled me to visualize the query output which I had saved as csv (comma seperated value) files after running each SQL query. 
- **Gitub and Git**: To share my analysis, visualizations and code

# The Analysis
Each query for this project aimed at investigating specific aspects of the data analyst job market. Here’s how I approached each question:

### 1. Top Paying Data Analyst Jobs
To identify the highest-paying roles, I filtered data analyst positions by average yearly salary and location, focusing on remote jobs. This query highlights the high paying opportunities in the field.

```sql
SELECT	
	job_id,
	job_title,
	job_location,
	job_schedule_type,
	salary_year_avg,
	job_posted_date,
    name AS company_name
FROM
    job_postings_fact
LEFT JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
WHERE
    job_title_short = 'Data Analyst' AND 
    job_location = 'Anywhere' AND 
    salary_year_avg IS NOT NULL
ORDER BY
    salary_year_avg DESC
LIMIT 10;
```
Here's three takeways for the top 10 data analyst jobs:

**Wide Salary Range** 
The top 10 paying data analyst roles have a range from $184,000 to $650,000 indicating a very wide range of potential for the job titles. 
**Diverse Employers**
Companies like Meta, and AT & T are among those offering high salaries, showing analyst positions in different industries.
**Job Title Variety**: There's a large diversity in job titles, from Data Analyst to Director of Analytics, showing varied roles and specializations within data analytics.

![Top Paying Roles](https://github.com/HarvestMondello/SQL_Project_Data_Job_Analysis/blob/main/assets/1_viz.png)
*bar graph visualizing the top 10 data analyst salaries for data analysts. This result was generated using Python. 

### 2. Skills for Top Paying Jobs
To understand what skills are required for the top-paying jobs, I joined the job postings with the skills data, providing insights into what employers value for high-compensation roles.

```sql
-- Gets the top 10 paying Data Analyst jobs 
WITH top_paying_jobs AS (
    SELECT
        job_id,
        job_title,
        salary_year_avg
        -- name AS company_name
    FROM
        job_postings_fact
    -- LEFT JOIN company_dim ON job_postings_fact.company_id = company_dim.company_id
    WHERE
        job_title_short = 'Data Analyst'
				AND salary_year_avg IS NOT NULL
        AND job_location = 'Anywhere'
    ORDER BY
        salary_year_avg DESC
    LIMIT 10
)
-- Skills required for data analyst jobs
SELECT
    top_paying_jobs.job_id,
    job_title,
    salary_year_avg,
    skills
FROM
    top_paying_jobs
	INNER JOIN
    skills_job_dim ON top_paying_jobs.job_id = skills_job_dim.job_id
	INNER JOIN
    skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
ORDER BY
    salary_year_avg DESC

```
Here's the breakdown of the most demanded skills for the top 10 highest paying data analyst jobs:

**SQL** is leading with a count of 8.
**Python** is second most in demand with a count of 7.
**Tableau** is also highly sought after, with a count of 6. Other skills like R, Snowflake, Pandas, and Excel show varying demand.

![Top Skills](https://github.com/HarvestMondello/SQL_Project_Data_Job_Analysis/blob/main/assets/2_viz.png)
*bar graph visualizing the top 10 skills for data analysts. This result was generated using Python. 

# What I Learned
# Conclusion

