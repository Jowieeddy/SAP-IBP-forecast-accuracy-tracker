# SAP IBP Forecast Accuracy Tracker (Python Simulation)

This project simulates forecast performance across three SKUs using 24 months of demand data. It replicates KPI tracking from SAP IBP and visualizes:

- Mean Absolute Percentage Error (MAPE)
- Forecast Bias
- Forecast Accuracy
- Carbon emissions and cost from over-forecasting

## 📊 Charts Included
- Forecast Accuracy by SKU (bar chart)
- Forecast-Driven Carbon Cost by SKU (bar chart)

## 🧪 Scenario Design
- Base simulation with noise-added forecast vs actuals
- Carbon exposure modeled using 0.5 kg CO₂/unit × $50/ton tax rate

## 🛠 Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn

## 🔁 Usage
Clone this repo and run:
```bash
python forecast_analysis.py
