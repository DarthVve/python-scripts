import  os
import shutil

# Directory to organize, in my case organiser-test.
directory = os.path.join(os.path.expanduser('~'), 'Desktop/organiser-test')

extensions = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".webp": "Images/web-assets",
    ".svg": "Images/web-assets",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".pptx": "Documents",
    ".json": "Documents",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".exe": "Programs",
    ".msi": "Programs",
    ".apk": "Programs",
    ".iso": "Programs",
    ".mp3": "Music",
    ".wav": "Music",
}

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file_path)[1].lower()

        if extension in extensions:
            folder_name  = extensions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved: {filename} to {folder_name}")
        else:
            print(f"Skipping: {filename}. Unknown file extension")
    else:
        print(f"Skipping: {filename}. It is a directory")

print("Done: Files have been organized.")
    