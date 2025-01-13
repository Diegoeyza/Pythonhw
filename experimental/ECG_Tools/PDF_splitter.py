import os
from PyPDF2 import PdfReader
from PIL import Image
import fitz  # PyMuPDF for rendering PDF to images

def get_pdf_dimensions(input_folder):
    """Extract the dimensions of the first page of the first PDF."""
    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, file_name)
            document = fitz.open(pdf_path)
            first_page = document[0]
            pix = first_page.get_pixmap()
            width, height = pix.width, pix.height
            return width, height
    return None, None

def get_crop_ranges(input_folder):
    """Get crop ranges from the user, showing the available image dimensions."""
    width, height = get_pdf_dimensions(input_folder)
    if width is None or height is None:
        print("No valid PDFs found in the input folder.")
        return []

    print(f"The dimensions of the PDF pages are approximately {width}x{height} (width x height).")
    print("Enter the three ranges for cropping height (e.g., 20-200, 210-400, 410-600):")

    ranges = []
    '''
    for i in range(4):
        while True:
            try:
                user_input = "150-250"
                start, end = map(int, user_input.split('-'))
                if 0 <= start < end <= height:
                    ranges.append((start, end))
                    break
                else:
                    print(f"Invalid range. Ensure 0 <= start < end <= {height}.")
            except ValueError:
                print("Please enter a valid range in the format start-end.")
    '''
#83
    try:
        user_input = ["192-277","277-362","362-447","447-532"]
        for i in range(4):
            start, end = map(int, user_input[i].split('-'))
            if 0 <= start < end <= height:
                ranges.append((start, end))
            else:
                print(f"Invalid range. Ensure 0 <= start < end <= {height}.")
    except ValueError:
        print("Please enter a valid range in the format start-end.")
    return ranges

def crop_and_save_pdfs(input_folder, output_folder, crop_ranges):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(input_folder):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, file_name)
            reader = PdfReader(pdf_path)
            document = fitz.open(pdf_path)

            for page_number, page in enumerate(document, start=1):
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                page_output_folder = os.path.join(output_folder, f"{file_name[:-4]}_page_{page_number}")
                if not os.path.exists(page_output_folder):
                    os.makedirs(page_output_folder)

                for i, (start, end) in enumerate(crop_ranges):
                    cropped_img = img.crop((88, start, img.width-44, end))
                    output_path = os.path.join(page_output_folder, f"crop_{i+1}.png")
                    cropped_img.save(output_path)
                    print(f"Saved: {output_path}")

def main():
    input_folder = r"C:\Users\diego\OneDrive\Escritorio\PDF_2024-12"
    output_folder = r"D:\Dataset_out"

    if not os.path.exists(input_folder):
        print("Input folder does not exist. Exiting.")
        return

    crop_ranges = get_crop_ranges(input_folder)
    if not crop_ranges:
        print("No crop ranges provided. Exiting.")
        return

    crop_and_save_pdfs(input_folder, output_folder, crop_ranges)
    print("Processing complete!")

if __name__ == "__main__":
    main()
