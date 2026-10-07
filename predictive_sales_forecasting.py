import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ============================================
# PREDICTIVE SALES FORECASTING
# ============================================

# 1. Load dataset
file_name = "Sales_Revenue_Analysis_Dataset.xlsx"

df = pd.read_excel(file_name)

print("============================================")
print("PREDICTIVE SALES FORECASTING")
print("============================================")

# ============================================
# 2. DATA CLEANING
# ============================================

# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Remove rows with missing dates or sales
df = df.dropna(subset=["Order_Date", "Sales"])

# Sort by date
df = df.sort_values("Order_Date")

print("\nDataset loaded successfully!")
print("Number of records:", len(df))

# ============================================
# 3. CREATE MONTHLY SALES DATA
# ============================================

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

# Convert Month to datetime
monthly_sales["Month"] = monthly_sales["Month"].dt.to_timestamp()

print("\n============================================")
print("MONTHLY SALES")
print("============================================")

print(monthly_sales)

# Save monthly sales
monthly_sales.to_csv("monthly_sales.csv", index=False)

# ============================================
# 4. CREATE TIME FEATURE
# ============================================

# Create a numerical time index
monthly_sales["Time_Index"] = range(len(monthly_sales))

# Independent variable
X = monthly_sales[["Time_Index"]]

# Dependent variable
y = monthly_sales["Sales"]

# ============================================
# 5. SPLIT DATA INTO TRAINING AND TESTING
# ============================================

# Use 80% for training
train_size = int(len(monthly_sales) * 0.8)

X_train = X.iloc[:train_size]
X_test = X.iloc[train_size:]

y_train = y.iloc[:train_size]
y_test = y.iloc[train_size:]

print("\n============================================")
print("TRAINING AND TESTING DATA")
print("============================================")

print("Training records:", len(X_train))
print("Testing records:", len(X_test))

# ============================================
# 6. TRAIN LINEAR REGRESSION MODEL
# ============================================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully!")

# ============================================
# 7. PREDICT TEST DATA
# ============================================

y_pred = model.predict(X_test)

# ============================================
# 8. MODEL EVALUATION
# ============================================

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n============================================")
print("MODEL EVALUATION")
print("============================================")

print("Mean Absolute Error (MAE):", round(mae, 2))
print("R² Score:", round(r2, 4))

# ============================================
# 9. CREATE ACTUAL VS PREDICTED DATA
# ============================================

results = pd.DataFrame({
    "Month": monthly_sales["Month"].iloc[train_size:].values,
    "Actual_Sales": y_test.values,
    "Predicted_Sales": y_pred
})

print("\n============================================")
print("ACTUAL VS PREDICTED SALES")
print("============================================")

print(results)

# Save prediction results
results.to_csv("actual_vs_predicted.csv", index=False)

# ============================================
# 10. PLOT ACTUAL VS PREDICTED SALES
# ============================================

plt.figure(figsize=(12, 6))

plt.plot(
    results["Month"],
    results["Actual_Sales"],
    marker="o",
    label="Actual Sales"
)

plt.plot(
    results["Month"],
    results["Predicted_Sales"],
    marker="o",
    label="Predicted Sales"
)

plt.title("Actual vs Predicted Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("actual_vs_predicted.png")

plt.show()

# ============================================
# 11. FORECAST FUTURE SALES
# ============================================

# Number of future months
future_months = 3

last_index = monthly_sales["Time_Index"].max()

future_indices = []

for i in range(1, future_months + 1):
    future_indices.append(last_index + i)

future_X = pd.DataFrame({
    "Time_Index": future_indices
})

future_predictions = model.predict(future_X)

# ============================================
# 12. CREATE FUTURE MONTH DATES
# ============================================

last_month = monthly_sales["Month"].max()

future_dates = []

for i in range(1, future_months + 1):
    future_dates.append(
        last_month + pd.DateOffset(months=i)
    )

forecast = pd.DataFrame({
    "Month": future_dates,
    "Forecasted_Sales": future_predictions
})

print("\n============================================")
print("FUTURE SALES FORECAST")
print("============================================")

print(forecast)

# Save forecast
forecast.to_csv("future_sales_forecast.csv", index=False)

# ============================================
# 13. PLOT FUTURE FORECAST
# ============================================

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["Month"],
    monthly_sales["Sales"],
    marker="o",
    label="Historical Sales"
)

plt.plot(
    forecast["Month"],
    forecast["Forecasted_Sales"],
    marker="o",
    linestyle="--",
    label="Future Forecast"
)

plt.title("Sales Forecast Using Linear Regression")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()
plt.grid(True)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("future_sales_forecast.png")

plt.show()

# ============================================
# 14. FINAL OUTPUT
# ============================================

print("\n============================================")
print("PROJECT COMPLETED")
print("============================================")

print("\nFiles created:")

print("1. monthly_sales.csv")
print("2. actual_vs_predicted.csv")
print("3. future_sales_forecast.csv")
print("4. actual_vs_predicted.png")
print("5. future_sales_forecast.png")

print("\nPrediction model: Linear Regression")

print("\nFuture Sales:")
print(forecast)