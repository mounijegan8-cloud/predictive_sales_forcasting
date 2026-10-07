# Predictive Sales Forecasting Using Historical Data

## 📌 Project Overview

This project uses historical sales data to predict future sales trends using **Machine Learning**. The dataset is cleaned and transformed into monthly sales data, followed by a **Linear Regression** model to analyze trends and forecast future sales.

## 🎯 Objectives

* Clean and preprocess historical sales data
* Analyze monthly sales trends
* Build a predictive regression model
* Evaluate model performance using MAE and R² Score
* Forecast sales for future months
* Visualize actual, predicted, and forecasted sales

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Excel

## 📂 Project Structure

```text
Predictive-Sales-Forecasting/
│
├── Sales_Revenue_Analysis_Dataset.xlsx
├── predictive_sales_forecasting.py
├── monthly_sales.csv
├── actual_vs_predicted.csv
├── future_sales_forecast.csv
├── actual_vs_predicted.png
└── future_sales_forecast.png
```

## 🔄 Project Workflow

```text
Historical Sales Data
        ↓
Data Cleaning & Preprocessing
        ↓
Monthly Sales Aggregation
        ↓
Time Index Creation
        ↓
Train-Test Split
        ↓
Linear Regression Model
        ↓
Model Evaluation
        ↓
Future Sales Forecast
        ↓
Visualization
```

## 🤖 Machine Learning Model

A **Linear Regression** model is used to identify the trend in historical monthly sales.

The model uses:

* **Input:** Time Index
* **Output:** Monthly Sales

The dataset is divided chronologically into:

* 80% Training Data
* 20% Testing Data

## 📊 Model Evaluation

The model is evaluated using:

### Mean Absolute Error (MAE)

Measures the average difference between actual and predicted sales values.

### R² Score

Measures how well the model explains the variation in the sales data.

The actual values obtained from the model are available in the project output files.

## 🔮 Future Sales Forecast

The trained model is used to forecast sales for the **next 3 months** based on the historical sales trend.

The forecast results are stored in:

`future_sales_forecast.csv`

## 📈 Visualizations

### Actual vs Predicted Sales

`actual_vs_predicted.png` compares the actual sales values with the model's predictions.

### Future Sales Forecast

`future_sales_forecast.png` shows historical sales along with the forecast for the upcoming months.

## ▶️ How to Run the Project

### 1. Install Python

Make sure Python is installed on your system.

### 2. Install Required Libraries

```bash
pip install pandas openpyxl matplotlib scikit-learn
```

### 3. Place the Dataset

Keep the following file in the same folder as the Python program:

```text
Sales_Revenue_Analysis_Dataset.xlsx
```

### 4. Run the Program

```bash
python predictive_sales_forecasting.py
```

### 5. View the Results

The program generates:

* `monthly_sales.csv`
* `actual_vs_predicted.csv`
* `future_sales_forecast.csv`
* `actual_vs_predicted.png`
* `future_sales_forecast.png`

## ✅ Conclusion

This project demonstrates how historical sales data can be used to build a simple predictive analytics solution. Linear Regression is applied to identify sales trends and generate future sales forecasts, providing a basic data-driven approach to sales prediction.

## 👩‍💻 Author

**MOUNIKA V J**

2nd Year / 3rd Semester
Rathinam Technical Campus
