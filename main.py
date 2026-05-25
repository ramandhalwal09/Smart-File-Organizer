import os
import shutil
from datetime import datetime

SOURCE_FOLDER = r"C:\Users\Raman\Downloads"

File_Types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "PDFs": [".pdf"],
    "Documents": [".docx", ".txt", ".pptx"],
    "Programs": [".exe", ".msi"],
    "Compressed": [".zip", ".rar"],
    "Python Files": [".py"]
}

def Create_Folder(folderpath):
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        print(f"Created folder : {folderpath}")

def Move_File(file_name, destination_folder):
    source_path = os.path.join(SOURCE_FOLDER, file_name)
    destination_path = os.path.join(destination_folder, file_name)

    if os.path.exists(destination_path):
        name, extension = os.path.splitext(file_name)
        timestamp = datetime.now().strftime("%H%M%S")
        new_name = f"{name}_{timestamp}{extension}"
        destination_path = os.path.join(destination_folder, new_name)
    
    shutil.move(source_path, destination_path)
    print(f"Moved : {file_name} --> {destination_folder}")

def organize_files():

    files = os.listdir(SOURCE_FOLDER)
    file_count = 0
    moved_count = 0

    for file in files:
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isdir(file_path):
            continue
        file_count += 1
        moved = False
        _, extension = os.path.splitext(file)
        extension = extension.lower()

        for folder_name, extensions in File_Types.items():

            if extension in extensions:

                folder_path = os.path.join(SOURCE_FOLDER, folder_name)
                Create_Folder(folder_path)
                Move_File(file, folder_path)
                moved_count += 1
                moved = True
                break

        if not moved:

            other_folder = os.path.join(SOURCE_FOLDER, "Others")
            Create_Folder(other_folder)
            Move_File(file, other_folder)
            moved_count += 1

    print("\nSummary :- ")
    print(f"Total Files Found : {file_count}")
    print(f"Files Organized   : {moved_count}")
    print("Organization Complete.")

if __name__ == "__main__":
    organize_files()