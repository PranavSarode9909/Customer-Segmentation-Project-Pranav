# 📊 Customer Segmentation Project

<p align="center">

<a href="https://customer-segmentation-project-cvkkhnzjfard4hihqm4rgb.streamlit.app/" target="_blank">
<img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-STREAMLIT-red?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo">
</a>

<a href="https://customer-segmentation-project-cvkkhnzjfard4hihqm4rgb.streamlit.app/" target="_blank">
<img src="https://img.shields.io/badge/STREAMLIT-APP-red?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit App">
</a>

<a href="https://github.com/atharva123-buddy/Customer-Segmentation-Project" target="_blank">
<img src="https://img.shields.io/badge/💻%20GITHUB-SOURCE%20CODE-black?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Source Code">
</a>

</p>

<p align="center">
<strong>Customer Segmentation using K-Means Clustering and Interactive Streamlit Dashboard</strong>
</p>

---


# 📊 Customer Segmentation Project

An end-to-end customer segmentation project using **Python, Exploratory Data Analysis, K-Means Clustering, and Streamlit** to identify customer groups based on demographics, income, and spending behavior.

## 📌 Project Overview

Customer segmentation is the process of dividing customers into groups based on similar characteristics and behaviors.

This project analyzes the **Mall Customers dataset** and applies **K-Means Clustering** to identify meaningful customer segments based on:

- Age
- Annual Income
- Spending Score

The project also includes an interactive **Streamlit dashboard** that allows users to explore the identified customer segments and their characteristics.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Understand customer demographics and purchasing behavior
- Perform data cleaning and preprocessing
- Conduct Exploratory Data Analysis (EDA)
- Identify important patterns in customer data
- Apply K-Means clustering for customer segmentation
- Determine the optimal number of clusters
- Analyze the characteristics of each customer segment
- Develop business insights and marketing recommendations
- Build an interactive Streamlit dashboard
- Deploy the dashboard as a live web application

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming and analysis |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Machine Learning and K-Means clustering |
| Plotly | Interactive visualizations |
| Streamlit | Interactive dashboard |
| Jupyter Notebook | Data analysis and experimentation |
| Git & GitHub | Version control and project hosting |

---

## 📂 Dataset

The project uses the **Mall Customers dataset**.

### Dataset Features

| Column | Description |
|---|---|
| CustomerID | Unique customer identifier |
| Gender | Customer gender |
| Age | Customer age |
| Annual_Income | Annual income in thousands of dollars |
| Spending_Score | Customer spending score from 1 to 100 |

The original dataset contains **200 customers**.

---

# 🔍 Project Methodology

The project follows an end-to-end data analytics and machine learning workflow.

### 1. Dataset Loading

The Mall Customers dataset is loaded into a Pandas DataFrame for analysis.

### 2. Data Understanding

The dataset is examined using:

- Dataset dimensions
- Column names
- Data types
- Statistical summary
- Unique values
- Dataset information

### 3. Data Cleaning

The dataset is checked for:

- Missing values
- Duplicate records
- Unique customer IDs

Column names are also simplified for easier analysis.

For example:

```text
Annual Income (k$) → Annual_Income
Spending Score (1-100) → Spending_Score