# Merge Student Data Utility

This Python script merges data from `studentlist.csv` and `studentdata.csv` into a new file `finallist.csv`.

## Functionality

The script performs the following tasks:
- Reads `studentdata.csv` to create a dictionary based on the 'name' field.
- Reads `studentlist.csv` to retrieve 'id', 'regdno', and 'name'.
- Matches 'name' from `studentlist.csv` with the dictionary created from `studentdata.csv`.
- Creates a new CSV file `finallist.csv` containing merged data.

## Requirements

- Python 3.x
- CSV files: `studentlist.csv`, `studentdata.csv`

## Usage

1. **Clone Repository:**
git clone https://github.com/ramabhadrarao/Merge-Student-Data-Utility
cd merge-student-data

2. **Install Dependencies (if needed):**
This script uses only built-in Python libraries. No additional dependencies are required.

3. **Run the Script:**
- Ensure `studentlist.csv` and `studentdata.csv` are in the root directory.
- Execute the script using Python:
  ```
  python merge_data.py
  ```

4. **Output:**
After execution, a new file named `finallist.csv` will be created in the same directory.

## File Structure

- `merge_data.py`: Python script to merge data.
- `studentlist.csv`: Contains student details with 'id', 'regdno', and 'name'.
- `studentdata.csv`: Contains additional data based on 'name'.

## Contribution

Feel free to contribute to enhance the functionality or optimize the code. Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-idea`).
3. Make modifications and commit changes (`git commit -am 'Add awesome feature'`).
4. Push the changes to your branch (`git push origin feature/awesome-idea`).
5. Create a pull request.

## License

This project is licensed under the [MIT License].

---
Author: Rama Bhadra Rao Maddu
