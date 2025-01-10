from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfFileReader, PdfReader
import os, random, datetime
from pathlib import Path
import pytesseract
from pypdf import PdfReader
import sys, pathlib
from pdfminer.high_level import extract_text
from pathlib import Path
import shutil
from tqdm import tqdm
import nltk
from nltk import tokenize
nltk.download('punkt_tab')


def pdf_to_images(pdf_path:str, output_in=None):
    """
    Provide for a given pdf document provided its path, images of all
    pages in separated .jpeg files stored in the output directory. If
    the output directory is not provided pdf directory is considered as
    output directory
    """
    try:
        # print("***converting pdf to images***")
        pdf_basename = os.path.basename(pdf_path).split(".")[0] # removing file extension
        if not output_in:
            out_directory = Path(pdf_path).parent.absolute()
        else:
            out_directory = Path(output_in)
        os.makedirs(out_directory, exist_ok=True)
        reader = PdfReader(pdf_path)
        pdf_pages = convert_from_path(pdf_path, 500)
        image_file_list = []
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = os.path.join(out_directory, f"{page_enumeration}.jpg")
            page.save(filename, "JPEG")
            image_file_list.append(filename)
        # print("***convertion completed***")
        return image_file_list
    except Exception as e:
        print(e)
        return None


def get_pdf_nature(filepath):
    options = ['scanned', 'digital', 'unknown']
    file_content = None
    try: #latin1
        file_content = open(filepath, mode='r', encoding="latin1").read()
    except Exception as e: #utf8
        file_content = open(filepath, mode='r', encoding="utf8").read()
    file_content = str(file_content)
    if '/Text' in file_content and '/Image' in file_content:
        return options[1]
    elif '/Text' in file_content and '/Image' not in file_content:
        return options[1]
    elif '/Text' not in file_content and '/Image' in file_content:
        return options[0]
    else:
        return options[2]


def extract_tesseract(pdf_path):
    pdf_pages = convert_from_path(pdf_path, 500)
    basename = os.path.basename(pdf_path).split(".")[0]
    parent = Path(pdf_path).parent.absolute()
    image_file_list = []
    output_dir = os.path.join(parent, basename)
    final_text = ""
    os.makedirs(output_dir, exist_ok=True)
    for page_enumeration, page in enumerate(pdf_pages, start=1):
        filename = os.path.join(f"{output_dir}", f"{basename}_{page_enumeration}.jpg")
        page.save(filename, "JPEG")
        image_file_list.append(filename)
    for image_file in image_file_list:
        text = str(((pytesseract.image_to_string(Image.open(image_file)))))
        text = text.replace("-\n", "")
        final_text += "\n" + text
    shutil.rmtree(output_dir)
    return final_text


def extract_tesseract(pdf_path):
    pdf_pages = convert_from_path(pdf_path, 500)
    basename = os.path.basename(pdf_path).split(".")[0]
    parent = Path(pdf_path).parent.absolute()
    image_file_list = []
    output_dir = os.path.join(parent, basename)
    final_text = ""
    os.makedirs(output_dir, exist_ok=True)
    for page_enumeration, page in enumerate(pdf_pages, start=1):
        filename = os.path.join(f"{output_dir}", f"{basename}_{page_enumeration}.jpg")
        page.save(filename, "JPEG")
        image_file_list.append(filename)
    for image_file in image_file_list:
        text = str(((pytesseract.image_to_string(Image.open(image_file)))))
        text = text.replace("-\n", "")
        final_text += "\n" + text
    shutil.rmtree(output_dir)


#pypdf
def extract_pypdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += "\n" + page.extract_text()
    return text


def extract_document_objects(image_path):
    """
    Use the document segmentation models to extract object from pdf page image
    """
    pass


def inline_text(file_path):
    res = ""
    _switch = False # switch from writting all on the same line to writting as in file.
    mfile = None
    try:
        mfile = open(file_path,"r", encoding="utf-8")
    except Exception as e:
        mfile = open(file_path,"r", encoding="latin1")
    for line in mfile.readlines():
        # exclude document references section and subsequent sections
        if line.lower().strip().startswith("references"):
            break
        nline = line.replace("-\n", " ")
        nline = nline.replace("\n", " ")
        nline = nline.replace("| ", "")
        nline = nline.replace("\'", "")
        nline = nline.replace("  ", " ")
        nline = nline.replace("\t", " ")
        # if nline.lower().strip().startswith("key"):
        #     nline = "MAIN BODY: \n" + nline
        res += nline
    # res = "HEADER: \n" + res
    res = tokenize.sent_tokenize(res)
    return res


def extract_pdf_text(pdf_path, output_folder):
    """
    Extract from a document only it main text not the noises (such as footnotes, page numbers, etc)
    """
    try:
        pdf_basename = os.path.basename(pdf_path).split(".")[0] # removing file extension
        out_directory = Path(output_folder)
        os.makedirs(out_directory, exist_ok=True)
        pdf_nature=get_pdf_nature(pdf_path)
        if pdf_nature == "scanned":
            text = extract_tesseract(pdf_path)
            with open(os.path.join(out_directory,f"{pdf_basename}.txt"), "w+", encoding="utf-8") as output_file:
                output_file.write(text)
        elif pdf_nature == "digital":
            text = extract_pypdf(pdf_path)
            with open(os.path.join(out_directory,f"{pdf_basename}.txt"), "w+", encoding="utf-8") as output_file:
                output_file.write(text)
        mtext = inline_text(os.path.join(out_directory,f"{pdf_basename}.txt"))
        with open(os.path.join(out_directory,f"{pdf_basename}.txt"), "w+", encoding="utf-8") as output_file:
                output_file.write("\n".join(mtext))
        return True
    except Exception as e:
        print(e)
        return False


def extract_pdf_text_from_folder(parent_path, extraction_path):
    res = True
    files = None
    extension=".pdf"
    for (root,dirs,files) in os.walk(parent_path, topdown=True):
        for file in tqdm(files[:1], position=0, leave=True):
            if file.endswith(extension):
                extract_pdf_text(os.path.join(parent_path, file), output_folder=extraction_path)
    return res



if __name__ == '__main__':
    parent_folder = "../pdfs"
    res = extract_pdf_text_from_folder(parent_folder, "../text_extractions")