# Data Structure Creator for tests on files and folders

This script generates a structured directory and file system based on specified parameters, including year, month, day folders, and various file types.

## Features

- **Create Year/Month/Day Folders:** Generates a nested folder structure for the specified number of months from a start date.
- **Sequential File Creation:** Creates files with specified extensions in each day folder, populated with date and time data.
- **Custom File and Directory Creation:** Allows for the creation of additional specified files and directories.

## Functions

### `create_year_month_day_folders_with_files(start_date, target_directory, month_count)`

- **Parameters:**
  - `start_date`: Starting date in `YYYY-MM-DD` format.
  - `target_directory`: Base directory where folders will be created.
  - `month_count`: Number of months to create folders for.

### `create_sequential_files(start_date, start_time, target_directory, month_count, file_extensions)`

- **Parameters:**
  - `start_date`: Starting date in `YYYY-MM-DD` format.
  - `start_time`: Starting time in `HH:MM:SS.ffffff` format.
  - `target_directory`: Directory where files will be created.
  - `month_count`: Number of months for which files will be generated.
  - `file_extensions`: Comma-separated list of file extensions.

### `create_other_files(other_files, target_directory)`

- **Parameters:**
  - `other_files`: List of additional file names to create.
  - `target_directory`: Directory where these files will be created.

### `create_other_dirs(other_dirs, root_directory)`

- **Parameters:**
  - `other_dirs`: List of additional directory names to create.
  - `root_directory`: Base directory for the new directories.

### `set_file_modification_date(file_path, date)`

- **Parameters:**
  - `file_path`: Path to the file.
  - `date`: Date to set as the file's modification date.

### `set_folder_modification_date(folder_path, date)`

- **Parameters:**
  - `folder_path`: Path to the folder.
  - `date`: Date to set as the folder's modification date.

## Example Usage

```python
first_date = "2023-07-17"
first_time = "12:29:24.195003"
creation_dir = "C:\\teste\\DATA_LAKE\\"
number_of_months = "24"
file_extensions = "TXT,JPG,ETP"
other_files = ["TESTE.WAV"]
other_dirs = ["TESTE1", "TESTE2"]

create_year_month_day_folders_with_files(first_date, creation_dir, number_of_months)
create_sequential_files(first_date, first_time, creation_dir, number_of_months, file_extensions)
create_other_files(other_files, creation_dir)
create_other_dirs(other_dirs, creation_dir)
```

## Logging

The script uses the `logging` module to provide feedback during execution, including directory and file creation notifications.

## Error Handling

Invalid date or time formats will result in error logs, ensuring robustness in input handling.

## Requirements

- Python 3.x
- `os` and `logging` modules (standard in Python)