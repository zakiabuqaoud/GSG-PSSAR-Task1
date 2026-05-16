
import pandas as pd
import os

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

# check Is parquet exists
if not os.path.exists("raw_data/employee.parquet"):
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

# print data
print("%" * 20)
print(emp_data_frame_csv.head(3)) # print first 3 row
print("%" * 20)
print(emp_data_frame_csv.sample(3)) # print random 3 row
print("%" * 20)
print(emp_data_frame_csv.tail(3)) # print last 3 row





