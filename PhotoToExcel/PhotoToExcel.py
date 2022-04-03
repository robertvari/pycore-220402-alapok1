import os

# r = raw string
photo_folder = r"C:\Work\_PythonSuli\pycore-220402\photos"

# what if path doesn't exist?
assert os.path.exists(photo_folder), f"Könyvtár nem létezik: {photo_folder}"

# what if the path is a file??
assert os.path.isdir(photo_folder), "Egy könyvtárra van szükségem!"

# todo get photos from photo_folder and create a list from that
print(os.listdir(photo_folder))