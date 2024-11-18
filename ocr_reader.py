import pytesseract
import cv2
from PIL import Image
import easyocr

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\shohk\PycharmProjects\passport-reader\your_image.jpg'


def extract_text_from_image(image_path):
    # Rasmni ochish
    img = cv2.imread(image_path)

    # Matnni chiqarish
    text = pytesseract.image_to_string(img)
    return text


def extract_info_from_text(text):

    lines = text.split('\n')
    info = {}

    for line in lines:
        if "Name" in line:
            info["Name"] = line.split(":")[1].strip()
        if "File Number" in line:
            info["File Number"] = line.split(":")[1].strip()
        if "Issue Date" in line:
            info["Issue Date"] = line.split(":")[1].strip()
        if "Expiry Date" in line:
            info["Expiry Date"] = line.split(":")[1].strip()

    return info



def easyocr_text(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)
    text = " ".join([item[1] for item in result])
    return text



image_path = 'path_to_your_image.jpg'
text = extract_text_from_image(image_path)
info = extract_info_from_text(text)

print(info)
