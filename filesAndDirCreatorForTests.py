import os
import logging
from datetime import datetime, timedelta

first_date = "2021-05-17"
first_time = "12:29:24.195003"
creation_dir = "C:\\teste\\DATA_LAKE\\"
number_of_months = "40"
file_extensions = "TXT,JPG,ETP"
other_files = ["TESTE.WAV"]
other_dirs = ["TESTE1", "TESTE2"]

logging.basicConfig(level=logging.INFO)

def create_year_month_day_folders_with_files(start_date, target_directory, month_count):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        logging.error("Invalid start_date format. Use YYYY-MM-DD.")
        return
    
    current_date = start_date
    for month in range(int(month_count)):
        year = current_date.year
        month_str = current_date.strftime("%m")
        year_folder = os.path.join(target_directory, f'year{year}')
        month_folder = os.path.join(year_folder, f'month{month_str}')
        
        os.makedirs(month_folder, exist_ok=True)
        set_folder_modification_date(month_folder, current_date)

        for day in range(1, 32):
            try:
                day_date = current_date.replace(day=day)
                day_folder = os.path.join(month_folder, f'day{day:02}')
                os.makedirs(day_folder, exist_ok=True)
                set_folder_modification_date(day_folder, day_date)

                file_path = os.path.join(day_folder, f'file_{day:02}.txt')
                with open(file_path, 'w') as file:
                    file.write(f'Data for {day_date.strftime("%Y-%m-%d")}')
                
                set_file_modification_date(file_path, day_date)
            except ValueError:
                break
        
        current_date += timedelta(days=32)
        current_date = current_date.replace(day=1)

def create_sequential_files(start_date, start_time, target_directory, month_count, file_extensions):
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        start_time = datetime.strptime(start_time, "%H:%M:%S.%f")
    except ValueError:
        logging.error("Invalid date or time format.")
        return

    extensions = file_extensions.split(',')
    file_counter = 1
    
    for month in range(int(month_count)):
        for day in range(1, 32):
            try:
                day_date = start_date.replace(day=day)
                base_file_name = f'file{file_counter:02d}'
                
                for ext in extensions:
                    file_name = f'{base_file_name}.{ext}'
                    file_path = os.path.join(target_directory, file_name)
                    
                    with open(file_path, 'w') as file:
                        file.write(f'Data for {day_date.strftime("%Y-%m-%d")} with time {start_time.strftime("%H:%M:%S")}')
                    
                    set_file_modification_date(file_path, day_date)

                file_counter += 1
            except ValueError:
                break
        
        start_date = (start_date + timedelta(days=32)).replace(day=1)

def create_other_files(other_files, target_directory):
    for file_name in other_files:
        file_path = os.path.join(target_directory, file_name)
        with open(file_path, 'w') as file:
            file.write(f'Data for {file_name}')

def create_other_dirs(other_dirs, root_directory):
    for dir_name in other_dirs:
        dir_path = os.path.join(root_directory, dir_name)
        os.makedirs(dir_path, exist_ok=True)
        logging.info(f'Created directory: {dir_path}')
        set_folder_modification_date(dir_path, datetime.now())

def set_file_modification_date(file_path, date):
    timestamp = date.timestamp()
    os.utime(file_path, (timestamp, timestamp))
    logging.info(f'Set modification date for {file_path} to {date.strftime("%Y-%m-%d")}')

def set_folder_modification_date(folder_path, date):
    timestamp = date.timestamp()
    os.utime(folder_path, (timestamp, timestamp))
    logging.info(f'Set modification date for {folder_path} to {date.strftime("%Y-%m-%d")}')

create_year_month_day_folders_with_files(first_date, creation_dir, number_of_months)
create_sequential_files(first_date, first_time, creation_dir, number_of_months, file_extensions)
create_other_files(other_files, creation_dir)
create_other_dirs(other_dirs, creation_dir)
