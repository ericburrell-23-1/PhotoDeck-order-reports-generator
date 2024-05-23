# Order Reports Generator

## Description

This Python application processes order and customer information from two CSV files, combines the data, and generates new CSV files with formatted order reports. The reports are saved in a `reports` subdirectory within the specified folder.

It is intended for use with the job reports generated and downloaded from PhotoDeck.

## Usage

To run this application, use the following syntax from the command line:

```sh
python app.py <path_to_folder>
```

Replace `<path_to_folder>` with the path to the folder containing the .csv files to analyze.

## Prerequisites

- Python 3.x
- Ensure you have `os`, `re`, `csv`, and `sys` modules available (these are standard with Python).

## Files

- `orders_Report*.csv`: CSV file containing customer information.
- `orders_items*.csv`: CSV file containing order details.

_Note_ - The application expects the names of the customer info file and the orders/items file to start with `"orders_Report"` and `"orders_items"`, respetively. **DO NOT CHANGE THE NAMES OF THE FILES AFTER DOWNLOADING FROM PHOTODECK**. They _should_ already be named appropriately.

## Output

- The application will create a `reports` subdirectory inside the specified folder.
- It will generate new CSV files named `<photo_name>_orders_report.csv` in the `reports` directory, where `<photo_name>` is derived from the `media file name` field in the `orders_items*.csv` file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For any issues or contributions, please contact Eric Burrell at ericburrell231@gmail.com.
