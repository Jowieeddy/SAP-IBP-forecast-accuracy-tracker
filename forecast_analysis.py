import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore

print("Libraries loaded successfully.")

# Load forecast dataset
df = pd.read_csv("Forecast_Accuracy_Simulation_With_Carbon.csv")

# Preview the first few rows
print(df.head())

# Calculate KPI Summary
kpi_summary = df.groupby('SKU').agg({
    'APE': 'mean',          # MAPE
    'Error': 'mean',        # Bias
}).reset_index()

kpi_summary['Forecast Accuracy (%)'] = (1 - kpi_summary['APE']) * 100
kpi_summary['MAPE (%)'] = kpi_summary['APE'] * 100

# Optional: round for clarity
kpi_summary = kpi_summary[['SKU', 'MAPE (%)', 'Error', 'Forecast Accuracy (%)']]
kpi_summary.rename(columns={'Error': 'Bias'}, inplace=True)

print("\nKPI Summary:\n", kpi_summary)

# Summarize Carbon Impact by SKU
carbon_summary = df.groupby('SKU').agg({
    'Emissions (kg)': 'sum',
    'Carbon Cost ($)': 'sum'
}).reset_index()

# Optional: round for cleaner visuals
carbon_summary['Carbon Cost ($)'] = carbon_summary['Carbon Cost ($)'].round(2)

# Plot Carbon Cost by SKU
plt.figure(figsize=(6, 4))
sns.barplot(data=carbon_summary, x='SKU', y='Carbon Cost ($)', palette='Reds')

plt.title('Forecast-Driven Carbon Cost by SKU')
plt.ylabel('Cost ($)')
plt.tight_layout()
plt.show()

# Plot Forecast Accuracy by SKU
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

plt.figure(figsize=(6, 4))
sns.barplot(data=kpi_summary, x='SKU', y='Forecast Accuracy (%)', palette='Blues_d')

plt.title('Forecast Accuracy by SKU')
plt.ylabel('Accuracy (%)')
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
