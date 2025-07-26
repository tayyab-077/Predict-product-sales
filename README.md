Sales Prediction Using Linear Regression with Gradient Descent
🎯 Purpose / Motive

The objective of this project is to predict product sales based on the amount spent on advertisements across three major media channels:
- 📺 TV
- 📻 Radio
- 📰 Newspaper

By analyzing the historical dataset and using a machine learning algorithm (Linear Regression with Gradient Descent), we aim to forecast how changes in advertising spend affect sales.

🧠 What the Code Does

1. Data Loading:
   - Reads a dataset (CSV) containing columns: 'TV', 'Radio', 'Newspaper', and 'Sales'.

2. Data Normalization:
   - Normalizes the feature values to bring them to the same scale, which improves gradient descent performance.

3. Gradient Descent Training:
   - Uses manual implementation of gradient descent to optimize the model parameters (weights and bias).

4. Model Saving:
   - Saves the trained weights (w), bias (b), mean, and standard deviation using `joblib` so they can be used later for predictions.

5. Prediction Interface (Flask Web App):
   - Users can input ad spend manually or upload a CSV file.
   - The model returns predicted sales based on learned parameters.

🌍 Real-World Applications

- Marketing Strategy: Companies can estimate how changes in ad budgets affect product sales.
- Sales Forecasting: Sales teams can predict future demand based on planned advertising efforts.
- ROI Optimization: Helps determine which advertising channel yields the best returns.

🧪 Example Use Case

A marketing team plans to spend:
- ₹200,000 on TV
- ₹50,000 on Radio
- ₹30,000 on Newspaper

By entering these values into the web app, the model predicts expected sales — allowing the team to better allocate resources.

📁 Summary Table
Component	Description
Data	Advertising spend vs actual sales
Model	Linear Regression via Gradient Descent
Input	TV, Radio, Newspaper ad spend
Output	Predicted Sales
Interface	Flask + HTML (manual input & file upload)
Use Case	Forecasting, marketing strategy, ROI estimation

Additional:
Here’s a concise one-line project description perfect for your portfolio or resume:
Built a Flask web app to predict product sales using custom Linear Regression with Gradient Descent based on multi-channel advertising data.

