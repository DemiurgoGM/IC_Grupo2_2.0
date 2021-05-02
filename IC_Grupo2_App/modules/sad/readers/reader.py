from unidecode import unidecode


class DocumentReader:

    def read_document(self, path):
        raise NotImplementedError("You must implement this method!")

    def process_text(self, text):
        text = unidecode(text)
        text = text.replace("\n", " ")
        return text
