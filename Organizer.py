import os,shutil
categories = {
    ".png": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".txt": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".py": "Python"
}

def organize_files(path):
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        name, extension = os.path.splitext(file)
        extension = extension.lower()

        if extension in categories:
            category = categories[extension]
        else:
            category = "Others"

        category_folder = os.path.join(path, category)

        if not os.path.exists(category_folder):
            os.makedirs(category_folder)

        shutil.move(file_path, category_folder)

def main():
    path = input("Enter folder path: ")

    try:
        if not os.path.isdir(path):
            print("Invalid folder path.")
            return
        organize_files(path)
        print("\nFiles organized successfully.")

    except Exception as e:
        print("An error occurred:", e)

if __name__=="__main__":
    main()
