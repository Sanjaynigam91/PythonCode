import pandas as pd
csv_file = pd.read_csv("C:\\Users\\Sanjay\\PycharmProjects\\PythonCode\\Empdata.csv")
#print(csv_file)
#Replace 1 as 100
#res=csv_file["EmployeeID"]
#csv_file.loc[csv_file["EmployeeID"] <= 10, "EmployeeID"] = 100
#print(csv_file)

#Replace By Using Dictionary and regex
csv_file = csv_file.replace(
    to_replace={"Name": r"^[A-Za-z\s\.]+$"},
    value="Welcome",
    regex=True
)

print(csv_file)
