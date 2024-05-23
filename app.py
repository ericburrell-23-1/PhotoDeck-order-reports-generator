import os
import re
import csv
import sys


def main():
    # ENSURE PROPER USAGE SYNTAX AND DEFINE rootdir VARIABLE
    if len(sys.argv) != 2:
        print('\nSYNTAX ERROR! Please execute this app with the following syntax: python app.py <path_to_folder>\n\
Replace <path_to_folder> with the path to the folder containing the .csv files to analyze.\n\n\
If this application and the folder are both on the Desktop, and the folder is called "order_docs", you can use the following: \n\n\
\tpython app.py ./order_docs\n\n')
        sys.exit(1)

    rootdir = sys.argv[1]

    if not os.path.isdir(rootdir):
        print(f"The path {rootdir} is not a directory or does not exist.")
        sys.exit(1)

    combined_data = {}
    photo_orders = {}

    # GET THE NAMES OF THE CSV FILES TO BE PARSED
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if re.match("orders_items", file):
                orders_file = os.path.join(rootdir, file)
            if re.match("orders_Report", file):
                customer_info_file = os.path.join(rootdir, file)

    # CHECK THAT BOTH FILES WERE FOUND
    if ("orders_file" not in locals()) or ("customer_info_file" not in locals()):
        return print("A file is missing")

    # READ DATA FROM ORDERS FILE
    with open(orders_file, 'r', newline='') as orders_csv:
        csv_reader = csv.DictReader(orders_csv, delimiter=";")

        for line in csv_reader:
            important_line_info = {
                "photo_ordered": line["media file name"], "product_ordered": line["description"], "quantity": line["quantity"]}
            combined_data[line["order id"]] = important_line_info

    # READ DATA FROM CUSTOMER INFO FILE
    with open(customer_info_file, 'r', newline='') as customer_info_csv:
        csv_reader = csv.DictReader(customer_info_csv, delimiter=";")

        for line in csv_reader:
            customer = line["client"]
            payment_state = line["payment state"]
            customer_name = re.split("\n", customer)[0]
            combined_data[line["id"]]["customer"] = customer_name
            combined_data[line["id"]]["payment_state"] = payment_state

    # PARSE COMBINED DATA BY PHOTO NAME
    for id in combined_data:
        order_data = combined_data[id]
        photo_name = order_data["photo_ordered"]
        if photo_orders.get(photo_name) == None:
            photo_orders[photo_name] = [order_data]
        else:
            photo_orders[photo_name].append(order_data)

    # WRITE THE PHOTO ORDERS TO A NEW FILE
    reports_dir = os.path.join(rootdir, "reports")
    os.makedirs(reports_dir, exist_ok=True)

    for photo in photo_orders:
        orders_data = photo_orders[photo]
        photo_name = re.split('\.', photo)[0]
        report_file_path = os.path.join(
            reports_dir, f"{photo_name}_orders_report.csv")

        with open(report_file_path, 'w', newline='') as new_file:
            field_names = ["photo_ordered",
                           "product_ordered", "quantity", "customer"]
            csv_writer = csv.DictWriter(new_file, fieldnames=field_names)

            csv_writer.writeheader()

            for order in orders_data:
                if order["payment_state"] == "paid":
                    del order["payment_state"]
                    csv_writer.writerow(order)

    return print("CSV file(s) created\n\nLocation: " + reports_dir)


if __name__ == "__main__":
    main()
