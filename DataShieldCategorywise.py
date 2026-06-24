import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

# ---------------------------------------------------------
# Function to create ZIP
# ---------------------------------------------------------
def make_zip(folder):

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"

    zobj = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)

            zobj.write(full_path, relative)

    zobj.close()
    return zip_name


# ---------------------------------------------------------
# Function to calculate hash (for change detection)
# ---------------------------------------------------------
def calculate_hash(path):
    hobj = hashlib.md5()

    with open(path, "rb") as fobj:
        while True:
            data = fobj.read(1024)
            if not data:
                break
            hobj.update(data)

    return hobj.hexdigest()


# ---------------------------------------------------------
# Function to categorize files
# ---------------------------------------------------------
def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()

    if ext == ".py":
        return "Python_Files"
    elif ext == ".pdf":
        return "PDF_Files"
    elif ext == ".java":
        return "Java_Files"
    elif ext == ".cpp":
        return "CPP_Files"
    elif ext in [".jpg", ".jpeg", ".png", ".gif"]:
        return "Images"
    else:
        return "Others"


# ---------------------------------------------------------
# Backup Function (Category-wise)
# ---------------------------------------------------------
def BackupFiles(Source, Destination):
    copied_files = []

    print("Creating category-wise backup...")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root, file)

            category = get_category(file)

            dest_dir = os.path.join(Destination, category)
            os.makedirs(dest_dir, exist_ok=True)

            dest_path = os.path.join(dest_dir, file)

            # Copy only new or modified files
            if (not os.path.exists(dest_path)) or \
               (calculate_hash(src_path) != calculate_hash(dest_path)):

                shutil.copy2(src_path, dest_path)
                copied_files.append(file)

    return copied_files


# ---------------------------------------------------------
# Main Backup Process
# ---------------------------------------------------------
def MarvellousDataShieldStart(Source="New"):

    Border = "-" * 50
    BackupName = "New"

    print(Border)
    print("Backup started at:", time.ctime())
    print(Border)

    files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    print(Border)
    print("Backup completed successfully")
    print("Files copied:", len(files))
    print("Zip file created:", zip_file)
    print(Border)


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------
def main():

    Border = "-" * 50
    print(Border)
    print("----- Marvellous Data Shield System -----")
    print(Border)

    if len(sys.argv) == 2:

        if sys.argv[1] in ["--h", "--H"]:
            print("This script is used to:")
            print("1. Take automatic backup")
            print("2. Backup only new/updated files")
            print("3. Organize files category-wise")
            print("4. Create zip archive")

        elif sys.argv[1] in ["--u", "--U"]:
            print("Usage:")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("Example: python Demo.py 5 Data")

        else:
            print("Invalid option. Use --h or --u")

    elif len(sys.argv) == 3:

        interval = int(sys.argv[1])
        source_dir = sys.argv[2]

        print("Time interval:", interval, "minutes")
        print("Source directory:", source_dir)

        schedule.every(interval).minutes.do(
            MarvellousDataShieldStart, source_dir
        )

        print(Border)
        print("Backup scheduler started...")
        print("Press Ctrl + C to stop")
        print(Border)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid arguments. Use --h for help")

    print(Border)
    print("----- Thank you for using script -----")
    print(Border)


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
