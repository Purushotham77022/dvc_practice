import pandas as pd
import os

df = pd.DataFrame({
    "Name" : ["Purush","Sudha","Madhu","Hema"],
    "Age" : [27,30,26,25],
    "Profession" : ["DataScientist","Operator","Incharge","Soilder"]
    })


data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")