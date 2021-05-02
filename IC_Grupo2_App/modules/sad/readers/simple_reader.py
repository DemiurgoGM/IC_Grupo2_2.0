from .reader import DocumentReader
import fitz


class SimpleDocumentReader(DocumentReader):

    def read_document(self, path):
        texts = []

        pdf = fitz.open(path)

        for pageNumber in range(len(pdf)):
            text = self.process_text(pdf.getPageText(pageNumber))
            texts.append(text)

        return " ".join(texts)
