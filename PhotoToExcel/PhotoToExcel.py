import os, json
from PIL import Image, ExifTags
from PIL import UnidentifiedImageError
from openpyxl import Workbook

# r = raw string
photo_folder = r"C:\Work\_PythonSuli\pycore-220402\photos"

# what if path doesn't exist?
assert os.path.exists(photo_folder), f"Könyvtár nem létezik: {photo_folder}"

# what if the path is a file??
assert os.path.isdir(photo_folder), "Egy könyvtárra van szükségem!"

# get photos from photo_folder and create a list from that
# list comprehension
file_list = [os.path.join(photo_folder, file) for file in os.listdir(photo_folder)]

# file_list = os.listdir(photo_folder)
# new_file_list = []
# for file in file_list:
#     new_file_list.append(os.path.join(photo_folder, file))

# filter file list to get only image files
allowed_extensions = [".jpg", ".jpeg", ".bmp"]
image_files = []
for file_item in file_list:
    # skip folders
    if os.path.isdir(file_item):
        continue

    # skip files if extension not in allowed_extensions
    filepath, extension = os.path.splitext(file_item)
    if not extension.lower() in allowed_extensions:
        continue

    image_files.append(file_item)

# get data from all photos and store them in dictionary
photo_data = {}
for photo in image_files:
    try:
        img = Image.open(photo)
        data = {
            "size": img.size,
            "date": None,
            "camera": None,
            "iso": None,
        }

        # get exif data
        exif_data = img._getexif()

        if exif_data:
            data["date"] = exif_data.get(0x9003)
            data["camera"] = exif_data.get(0x0110)
            data["iso"] = exif_data.get(0x8827)

        photo_data[photo] = data

    except UnidentifiedImageError:
        print(f"WARNING: {photo} is not an image file :(")

# todo save data to a .txt file
text_file_path = "photo_data.txt"
with open(text_file_path, "w") as f:
    f.write(str(photo_data))

# todo save data to a .json file
json_file_path = "photo_data.json"
with open(json_file_path, "w") as f:
    json.dump(photo_data, f)

# load json back
with open(json_file_path) as f:
    data = json.load(f)
    print(data['C:\\Work\\_PythonSuli\\pycore-220402\\photos\\IMG_1069.JPG'])

# todo save data to an xlsx file
xlsx_file_path = "photo_data.xlsx"

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "File Path"
sheet.column_dimensions['A'].width = 80

sheet["B1"] = "Date"
sheet.column_dimensions['B'].width = 40

sheet["C1"] = "Size"
sheet.column_dimensions['C'].width = 40

sheet["D1"] = "Camera"
sheet.column_dimensions['D'].width = 40

sheet["E1"] = "ISO"
sheet.column_dimensions['E'].width = 40

for index, root_key in enumerate(photo_data):
    row = index + 3

    sheet[f"A{row}"] = root_key
    sheet[f"B{row}"] = photo_data[root_key]["date"]
    sheet[f"C{row}"] = str(photo_data[root_key]["size"])
    sheet[f"D{row}"] = photo_data[root_key]["camera"]
    sheet[f"E{row}"] = photo_data[root_key]["iso"]

workbook.save(xlsx_file_path)