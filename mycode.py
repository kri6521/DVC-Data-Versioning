import pandas as pd
import os

# sample dataframe
data = {
    "Name": ["alice", "bob", "charlie"],
    "Age": [25, 30, 35],
    "City": ["new york", "los angeles", "chicago"],
}

df = pd.DataFrame(data)

# adding new row
new_row_loc = {"Name": "GF1", "Age": 20, "City": "City1"}
df.loc[len(df.index)] = new_row_loc

# adding new row
new_row_loc2 = {"Name": "GF2", "Age": 30, "City": "City2"}
df.loc[len(df.index)] = new_row_loc2

# ensure "data" directory exists at root level
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)  # data name folder will be created

file_path = os.path.join(data_dir, "sample_data.csv")

df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
