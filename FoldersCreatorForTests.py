import time
import os
import datetime

user_profile = os.environ['USERPROFILE']
#Change month and year
num_months = 12
year = 2024
num_month_days = 30
month_test = 7
severalext = [".TRN",".TRT",".ETP"]
severalDir = ["TESTE","EXEPT","JEW"]

def month():

    def change_modification_date(folder_name, mod_time):
        mod_timestamp = mod_time.timestamp()
        os.utime(folder_name, (mod_timestamp, mod_timestamp))
    
    def change_modification_date_file(file_name, mod_time):
        mod_timestamp = mod_time.timestamp()
        os.utime(file_name, (mod_timestamp, mod_timestamp))

    for i in range(1, num_months + 1):
        folder_name = f'C:\\teste\\DATA_LAKE\\month{i:02}'
        os.makedirs(folder_name, exist_ok=True)
        print(f'Directory "{folder_name}" created sucessfully.')
        
        file_name = os.path.join(folder_name, f'File{i:02}.txt')
        with open(file_name, 'w') as file:
            file.write(f'This is the file {i:02} on dir {folder_name}.')
        print(f'File "{file_name}" created sucessfully.')
        
        mod_time = datetime.datetime(year, i, 1)
        change_modification_date(folder_name, mod_time)
        change_modification_date_file(file_name, mod_time)
        print(f'Modification date of "{folder_name}" changed to {mod_time}.')

    print('All folders were created and their modification dates changed.')

def days():

    def change_modification_date(folder_name, mod_time):
        mod_timestamp = mod_time.timestamp()
        os.utime(folder_name, (mod_timestamp, mod_timestamp))

    for day in range(1, num_month_days + 1):
        folder_name = f'C:\\teste\\DATA_LAKE\\month{month_test:02}\\day_{day:02}'
        os.makedirs(folder_name, exist_ok=True)
        print(f'Directory "{folder_name}" created sucessfully.')
        
        file_name = os.path.join(folder_name, f'file_day_{day:02}.txt')
        with open(file_name, 'w') as file:
            file.write(f'This is the file {day:02} on directory {folder_name}.')
        print(f'File "{file_name}" created sucessfully.')
        
        mod_time = datetime.datetime(year, month_test, day)
        change_modification_date(folder_name, mod_time)
        print(f'Modification date of "{folder_name}" changed to {mod_time}.')

    print('All folders were created and their modification dates changed.')

def severalFiles(severalext):
    try:

        def change_modification_date(folder_name, mod_time):
            mod_timestamp = mod_time.timestamp()
            os.utime(folder_name, (mod_timestamp, mod_timestamp))

        for day in range(1, num_month_days + 1):
            for i in severalext:
                    
                folder_name = f'C:\\teste\\DATA_LAKE\\'
                file_name = os.path.join(folder_name, f'file_day_{day:02}.{i}')
                with open(file_name, 'w') as file:
                    file.write(f'This is the file {day:02} on directory {folder_name}.')
                print(f'File "{file_name}" created sucessfully.')
                
                mod_time = datetime.datetime(year, month_test, day)
                change_modification_date(folder_name, mod_time)
                print(f'Modification date of "{folder_name}" changed to {mod_time}.')

            print('All folders were created and their modification dates changed.')
    except:
        pass

def severalDirs(severalDir):
    try:

        def change_modification_date(folder_name, mod_time):
            mod_timestamp = mod_time.timestamp()
            os.utime(folder_name, (mod_timestamp, mod_timestamp))

        for day in range(1, num_month_days + 1):
            for i in severalDir:
                    
                folder_name = f'C:\\teste\\DATA_LAKE\\{i}'
                os.makedirs(folder_name, exist_ok=True)
                print(f'Directory "{folder_name}" created sucessfully.')
                
                file_name = os.path.join(folder_name, f'{i}.txt')
                with open(file_name, 'w') as file:
                    file.write(f'This is the file {day:02} on directory {folder_name}.')
                print(f'File "{file_name}" created sucessfully.')
                
                mod_time = datetime.datetime(year, month_test, day)
                change_modification_date(folder_name, mod_time)
                print(f'Modification date of "{folder_name}" changed to {mod_time}.')

            print('All folders were created and their modification dates changed.')
    except:
        pass

month()
days()
severalFiles(severalext)
severalDirs(severalDir)