# CSV -> Comma Seprated Value

import csv

# WRITER
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
    # writer.writerow(["transaction_id", "product_id", "price"])
    # writer.writerow([1000, 1, 5])
    # writer.writerow([1001, 2, 15])


# READER
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)