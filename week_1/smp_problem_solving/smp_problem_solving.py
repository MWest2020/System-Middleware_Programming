import os, datetime, stat

# if file is empty, delete

def delete_empty_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if os.stat(os.path.join(root, name))[stat.ST_SIZE] == 0:
                os.remove(os.path.join(root, name))


#  check age files

def check_old_files(folder_path, years:int):
    now = datetime.datetime.now()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_stats = os.stat(file_path)
            file_modified_time = datetime.datetime.fromtimestamp(file_stats[stat.ST_MTIME])
            if (now - file_modified_time).days > 365*years:
                match years:
                    case 2 | 5:
                        with open("check_files.txt", "w") as file:
                            file.write("{file_path} is older than {years} years.")
                    case 10:
                        # archive path hardcoded, should be variable
                        new_path = os.path.join("c:/User/documents/archive", file)
                        os.rename(file_path, new_path)
                        print(f"{file_path} is older than {years} years. File is archived in {new_path}")


