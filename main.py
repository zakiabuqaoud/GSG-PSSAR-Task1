
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

# comma
print("///" * 50)

#dealing with parquet files

# create my  data frame
my_data = {
    "names" : ["Zaki", "Omar", "Ahmed"],
    "ages": [26,28,30]
}
my_data_frame = pd.DataFrame(my_data)

# create parquet file
my_data_frame.to_parquet("raw_data/employee.parquet")

#read and print parquet file
emp_data_frame_parquet = pd.read_parquet("raw_data/employee.parquet")
print(emp_data_frame_parquet)





