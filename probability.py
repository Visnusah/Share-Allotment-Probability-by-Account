import pandas as pd
import matplotlib.pyplot as plt 
import io

# Sample data
data = """Name,Total Applied Share,Alloted Share
Tamanna,38,7
Bimal,22,3
Kamlesh,62,15
Priya,21,3
Dipendra,12,2"""

# Create DataFrame
df = pd.read_csv(io.StringIO(data))

# Calculate Allotment Probability
df['Allotment Probability'] = df['Alloted Share'] / df['Total Applied Share']

# Sort by probability for better visualization and to find the max
df_sorted = df.sort_values(by='Allotment Probability', ascending=False)

# Display the dataframe to the user (via text response later) and identify the top one
print(df_sorted)

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(df_sorted['Name'], df_sorted['Allotment Probability'], color='skyblue')
plt.xlabel('Account Name')
plt.ylabel('Allotment Probability')
plt.title('Share Allotment Probability by Account')
plt.ylim(0, max(df_sorted['Allotment Probability']) * 1.2) # Add some headroom

# Add value labels on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2%}', ha='center', va='bottom')

plt.savefig('allotment_probability_chart.png')