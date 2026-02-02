import pandas as pd
import matplotlib.pyplot as plt


# Read the data file
import pandas as pd

file_path = 'data/snap-annualsummary-8.csv' #update this line with your file path
data = pd.read_csv(file_path, thousands=',')

print(data.shape)
print(data.columns)
print(data.head(10)) #print the first 10 observations
# Drop rows where *all* columns are NaN
data = data.dropna(how='all')

data['Fiscal Year'] = data['Fiscal Year'].astype(str).str[:4].astype(int) #keep only the first four symbols, which is a year, remove endnotes.

# --- Time Series Plot ---
plt.figure()  # Create a new figure
x_var = 'Fiscal Year'
y_var = 'Total Costs (Millions of Dollars)'


plt.plot(data[x_var], data[y_var], marker='.', linestyle='-', color='purple')


plt.xlabel(x_var)
plt.ylabel(y_var)
plt.title('Total Costs Over Years')

# --- Scatter Plot ---
plt.figure()  # Create another new figure

x2_var = 'Average Participation (Thousands)'
plt.scatter(data[x2_var], data[y_var],alpha=0.3, color='purple')

plt.xlabel(x2_var)
plt.ylabel(y_var)
plt.title('Relationship between Average Participation and Total Costs')

plt.show()