
# Data Analyst Job Postings Analysis 

# Synopsis
**Problem**: Identify trends in the data job market for targeted job applications.

**Solution**: Queried 1,500+ job listings using PostgreSQL, extracting top in-demand skills and industry trends. Visualized insights in Python.

**Insights**: SQL is the most in demand job for data analytics. 

**Recommendation**: Built a SQL-focused portfolio project, showcasing real-world data analysis & visualization skills to align with industry demands.

# Introduction
Welcome to my SQL project. In this project I will look at the US data job market with a focus on data analytics roles. This project will explore top paying jobs, in demand tools, and where high demand meets high salaries for data analytics.

See the SQL queries here: [queries folder](/queries/)

# Background
At the time of this project I was in the market for a data analytics position and I wanted to understand the data analyst job market better. 

In order to make my job search more targeted and more effected. I intended to discover which skills are paid the most, what analysis and visualation tools are in demand. 

The data for this analysis is from Luke Barousse’s SQL Course (https://www.lukebarousse.com/sql) and the data was provided by his web scraper. The data includes details on job titles, salaries, locations, and required skills. 

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
- **ChatGPT**: Used for routine formating tasks to be more efficient.

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

![Top Paying Roles](https://github.com/HarvestMondello/SQL_Project_Data_Job_Analysis/blob/main/assets/viz-1.png)
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

![Top Skills](https://github.com/HarvestMondello/SQL_Project_Data_Job_Analysis/blob/main/assets/viz-2.png)
*bar graph visualizing the top 10 skills for data analysts. This result was generated using Python. 

### 3. In-Demand Skills for Data Analysts
This query identifies the skills most frequently requested in job postings, directing focus to areas with high demand.

```sql
-- Identifies the top 5 most demanded skills for Data Analyst job postings
SELECT
  skills_dim.skills,
  COUNT(skills_job_dim.job_id) AS demand_count
FROM
  job_postings_fact
  INNER JOIN
    skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
  INNER JOIN
    skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
  -- Filters job titles for 'Data Analyst' roles
  job_postings_fact.job_title_short = 'Data Analyst'
	-- AND job_work_from_home = True -- optional to filter for remote jobs
GROUP BY
  skills_dim.skills
ORDER BY
  demand_count DESC
LIMIT 5;
```
| Skills    | Demand Count |
|-----------|--------------|
| SQL       | 92,628       |
| Excel     | 67,031       |
| Python    | 57,326       |
| Tableau   | 46,554       |
| Power BI  | 39,468       |

*Table of the demand for the top 5 skills in data analyst job postings. Markdown formated in ChatGPT to save time on routine tasks.

### 4. Skills Based on Salary
Exploring the average salaries associated with different skills to see which skills are the highest paying.

```sql
-- Calculates the average salary for job postings by individual skill 
  SELECT 
    skills,
    ROUND(AVG(salary_year_avg), 0) AS avg_salary
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
    job_title_short = 'Data Analyst'
    AND salary_year_avg IS NOT NULL
    AND job_work_from_home = True 
GROUP BY
    skills
ORDER BY
    avg_salary DESC
LIMIT 10;
```
  
A breakdown of the results for top paying skills for Data Analysts:

**High Demand for Big Data & Machine Learning Skills:** Top salaries are for data analysts skilled in big data technologies (PySpark, Couchbase), machine learning tools (DataRobot, Jupyter, Watson), and Python libraries (Pandas), reflecting the industry's high valuation of data processing and predictive modeling capabilities.
**Software Development & Deployment Proficiency:** Knowledge in development and deployment tools (GitLab, Bitbucket) indicates a lucrative crossover between data analysis and engineering, with a premium on skills that facilitate automation and efficient data pipeline management.
**Cloud Computing Expertise:** Familiarity with cloud and data engineering tools (Elasticsearch) underscores the growing importance of cloud-based analytics environments, suggesting that cloud proficiency significantly boosts earning potential in data analytics.


| Skills       | Average Salary ($) |
|--------------|--------------------|
| Pyspark      | 208,172            |
| Bitbucket    | 189,155            |
| Couchbase    | 160,515            |
| Watson       | 160,515            |
| Datarobot    | 155,486            |
| Gitlab       | 154,500            |
| Swift        | 153,750            |
| Jupyter      | 152,777            |
| Pandas       | 151,821            |
| Elasticsearch| 145,000            |

*Table of the average salary for the top 10 paying skills for data analysts. Markdown formated in ChatGPT to save time on routine tasks.

### 5. Highest Demand Skills
Combining insights from demand and salary data, this query aimed to pinpoint skills that are both in high demand and have high salaries, offering a strategic focus for skill development.

```sql
SELECT 
    skills_dim.skill_id,
    skills_dim.skills,
    COUNT(skills_job_dim.job_id) AS demand_count,
    ROUND(AVG(job_postings_fact.salary_year_avg), 0) AS avg_salary
FROM job_postings_fact
INNER JOIN skills_job_dim ON job_postings_fact.job_id = skills_job_dim.job_id
INNER JOIN skills_dim ON skills_job_dim.skill_id = skills_dim.skill_id
WHERE
    job_title_short = 'Data Analyst'
    AND salary_year_avg IS NOT NULL
    AND job_work_from_home = True 
GROUP BY
    skills_dim.skill_id
HAVING
    COUNT(skills_job_dim.job_id) > 10
ORDER BY
    avg_salary DESC,
    demand_count DESC
LIMIT 25;
```


Here's a breakdown of the top 25 skills paying the highest average salaries:

| Skills       | Demand Count | Average Salary ($) |
|--------------|--------------|--------------------|
| Go           | 27           | 115,320            |
| Confluence   | 11           | 114,210            |
| Hadoop       | 22           | 113,193            |
| Snowflake    | 37           | 112,948            |
| Azure        | 34           | 111,225            |
| BigQuery     | 13           | 109,654            |
| AWS          | 32           | 108,317            |
| Java         | 17           | 106,906            |
| SSIS         | 12           | 106,683            |
| Jira         | 20           | 104,918            |
| Oracle       | 37           | 104,534            |
| Looker       | 49           | 103,795            |
| NoSQL        | 13           | 101,414            |
| Python       | 236          | 101,397            |
| R            | 148          | 100,499            |
| Redshift     | 16           | 99,936             |
| Qlik         | 13           | 99,631             |
| Tableau      | 230          | 99,288             |
| SSRS         | 14           | 99,171             |
| Spark        | 13           | 99,077             |
| C++          | 11           | 98,958             |
| SAS          | 63           | 98,902             |
| SQL Server   | 35           | 97,786             |
| JavaScript   | 20           | 97,587             |


*Table of the demand for the top 5 skills in data analyst job postings. Markdown formated in ChatGPT to save time on routine tasks.

**Cloud Tools and Technologies:** Skills in specialized technologies such as Snowflake, Azure, AWS, and BigQuery show significant demand with relatively high average salaries, showing the trending importance of cloud platforms and big data technologies in data analysis. With salaries of Hadoop $113,193, Snowflake $112,948, Azure $111,225, AWS $108,317 and BigQuery $109,654. Non of these have triple digit demand count showing us that this is a more specialized field of data analytics. 
**Programming Languages:** Python and R stand out for their high demand, with demand counts of 236 and 148 respectively. Despite their high demand, their average salaries are around $101,397 for Python and $100,499 for R, indicating that proficiency in these languages is highly valued but also widely available. Languages such as Go are less in demand but pay more awith a demand of 27 and $115,320 avarage salary.
**Business Intelligence and Visualization Tools:** Tableau and Looker, with demand counts of 230 and 49 respectively, and average salaries around $99,288 and $103,795, highlight the critical role of data visualization and business intelligence in deriving actionable insights from data.
**Database Technologies:** The demand for skills in traditional and NoSQL databases (Oracle, SQL Server, NoSQL) with average salaries ranging from $97,786 to $104,534, reflects the enduring need for data storage, retrieval and management. 


# Conclusion

### The Problem
In order to make my Data Analyst job search more targeted and more effected, I wanted to discover which skills are paid the most, what analysis and visualation tools are in demand.

### How I Solved the Problem
I designed five SQL queries to answer sub questions related to my overall question:
1. What are the top paying data analyst jobs?
2. What skills do these top paying jobs require?
3. What skills are most demanded by the market?
4. Which skills bring in the highest salaries?
5. Which skills have both a high demand and high salary?

### Insights
The completed analysis shows five insights:
1. **Top Paying Data Analyst Jobs:** The highest paying jobs have a very large range topping out at $650,000.
2. **Skills for Top Paying Jobs:** SQL is a skill that all the highest paying data analysts need.
3. **Most Demanded Skills**: Again, SQL is the overall most demanded skill in the data analyst job market.
4. **Skills with the Highest Pay**: Include niche skills including cloud computing skills.
5. **Optimal Skill for the Job Market**: SQL is the most in demand skill and offers a high average salary, making it a very important skill to have.

### Closing Thoughts and Actionable Recommendation
&ensp;&ensp;&ensp;&ensp;Both junior and senior data analysts can better position themeselves in the job my by focusing on high demand skills. Through this project I increased my hands on SQL skills and came to see valuable insights into the data analyst job market. This will help me focus my skill development and job searches in a more targeted way. Additionally, showcaseing the project on Github increased my knowledge of Github, Git and allowed me to showcase a professional README file to integrate into my personal portfolio. 


### License

Created by Harvest Mondello. You're welcome to use this project for **personal** or **educational** purposes! Feel free to explore, adapt, and learn from the code and visuals. Just note that **commercial use isn’t permitted** without permission. See [LICENSE.md](https://github.com/HarvestMondello/data-analyst-job-postings-analysis/blob/main/LICENSE.MD) for full details and contact info.
