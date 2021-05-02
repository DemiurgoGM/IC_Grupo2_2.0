from .reader import DocumentReader
from pikepdf import Pdf, PdfImage

import pytesseract


class OCRDocumentReader(DocumentReader):

    def read_document(self, file):
        pdf = Pdf.open(file)
        print(pdf)
        document = pdf.pages[0]

        (name, raw_image) = next(document.images.items())

        image = PdfImage(raw_image).as_pil_image()

        text = pytesseract.image_to_string(image)

        return self.process_text(text)
