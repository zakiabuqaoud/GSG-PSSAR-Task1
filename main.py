
import pandas as pd

#read and print CSV file
emp_data_frame_csv = pd.read_csv("raw_data/employee.csv")
print("This is dataset in CSV File:")
print(emp_data_frame_csv)


# comma
print("///" * 50)

#read and print excel file
emp_data_frame_excel = pd.read_excel("raw_data/employee.xlsx")
print("This is dataset in Excel File:")
print(emp_data_frame_excel)