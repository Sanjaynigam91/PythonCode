import pandas as pd
csv_file = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\employee_dump_50_records_missing_data.csv")
print(csv_file)
numeric_data = csv_file.select_dtypes(include='number')

res = numeric_data.interpolate()

print(res)