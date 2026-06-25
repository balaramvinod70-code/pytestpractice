import pandas as pd

# Reading an Excel file
df = pd.read_excel("hr_payroll.xlsx")
fd=pd.read_excel("acc.xlsx")

print(df)
print(fd)# shows fi
merged = pd.merge(df, fd, on="EmployeeID", suffixes=("_DF", "_FD"))
print(merged)
mismatches = merged[
    (merged["HoursWorked_DF"] != merged["HoursWorked_FD"]) |
    (merged["Rate_DF"] != merged["Rate_FD"])
]
print("Mismatched Records:\n", mismatches)

# rst 5 rows
