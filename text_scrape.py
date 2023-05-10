from PIL import Image
from pytesseract import pytesseract
import enum
########################################################
image_path = str(input("Enter the path of the image: ")) #File path input
########################################################
class OS(enum.Enum):
    Mac = 0
    Windows = 1

class Language(enum.Enum):
    ENG = 'eng'                 # You can add more languages, but this one just has english.
                                #Example: RUS='rus' for russian
class ImageReader:

    def __init__(self,os: OS):
        if os == OS.Windows:
            windows_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Default path for tesseract OCR, if you install it the default way.
            pytesseract.tesseract_cmd = windows_path                       
            print("Running on: Windows\n")    
        if os == OS.Mac:                                #this is just to check if the code is working properly
            print("Running on: MAC\n")


    def extract_text(self,image:str, lang: Language) -> str:
        img = Image.open(image)
        extract_text=pytesseract.image_to_string(img, lang=lang.value)
        return extract_text

if __name__ == '__main__':
    ir = ImageReader(OS.Windows)
    text = ir.extract_text(image_path,lang=Language.ENG)
    print(text)                                                     #your text output!
