import pandas as pd
import os

df = pd.DataFrame({
    "Name" : ["Purush","Sudha","Madhu","Hema"],
    "Age" : [27,30,26,25],
    "Profession" : ["DataScientist","Operator","Incharge","Soilder"]
    })

new_df = {"Name": "Naveen", "Age": 24,"Profession" : "Engineer"}
df.loc[len(df.index)] = new_df

new_df_1 = {"Name": "Srinu", "Age": 23,"Profession" : "CivilEngineer"}
df.loc[len(df.index)] = new_df_1

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including column names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")