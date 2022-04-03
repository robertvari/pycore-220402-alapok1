import os

# r = raw string
photo_folder = r"C:\Work\_PythonSuli\pycore-220402\photos"

# what if path doesn't exist?
assert os.path.exists(photo_folder), f"Könyvtár nem létezik: {photo_folder}"

# what if the path is a file??
assert os.path.isdir(photo_folder), "Egy könyvtárra van szükségem!"

# todo get photos from photo_folder and create a list from that
# list comprehension
file_list = [os.path.join(photo_folder, file) for file in os.listdir(photo_folder)]

# file_list = os.listdir(photo_folder)
# new_file_list = []
# for file in file_list:
#     new_file_list.append(os.path.join(photo_folder, file))

# todo filter file list
allowed_extensions = [".jpg"]
for file_item in file_list:
    # skip folders
    if os.path.isdir(file_item):
        continue

    # skip files if extension not in allowed_extensions
    print(os.path.splitext(file_item))