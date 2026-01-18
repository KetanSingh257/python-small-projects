import os

def arrange_files(files, ext):
    files_with_ext = [file for file in files if file.endswith(ext)]
    print(files_with_ext)

    if not os.path.exists("imagesfolder"):
        os.mkdir("imagesfolder")
    for i, file in enumerate(files_with_ext, 1):
        os.rename(file, f" image{i}{ext}")
   

if __name__ == "__main__":
    files = os.listdir('.')
    arrange_files(files, '.jpg')