from ocr_reader import extract_text

def main():
    image_path = input("Enter the image path: ")
    extracted_text = extract_text(image_path)
    print("Extracted Text:\n", extracted_text)

if __name__ == "__main__":
    main()
