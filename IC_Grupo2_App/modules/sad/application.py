from .extractors.information_extractor import InformationExtractor
from .helpers.directory import Directory
from .readers.reader import DocumentReader
from .readers.ocr_reader import OCRDocumentReader
from .readers.simple_reader import SimpleDocumentReader
from .output.output import Output
from .searchers.fuzzy_search import FuzzySearch


class Application:
    def __init__(self, file, address: str, directory: Directory, readers: [DocumentReader],
                 extractor: InformationExtractor, output: Output, search: FuzzySearch):
        self.file = file
        self.output = output
        self.search = search
        self.readers = readers
        self.address = address
        self.directory = directory
        self.extractor = extractor

    def run(self):
        extracted_text = self.readers[0].read_document(self.file)
        print("EXTRACTED", extracted_text)
        fields = self.extractor.extract_all_informations(extracted_text)

        if self.should_try_ocr(fields):
            extracted_text = self.readers[1].read_document(self.file)
            fields = self.extractor.extract_all_informations(extracted_text)

        highlighted_pdf = self.output.generate_highlighted_pdf(self.file, fields)

        office_no, process_no, subject, originator = fields

        addresses, score = self.search.for_address('Endereço', self.address)

        csv = self.output.generate_csv(self.file, office_no, process_no, subject, originator,
                                       addresses[['Endereço', 'Bairro', 'Município']], score)

        return highlighted_pdf, csv

    def should_try_ocr(self, extracted_information: [str]):
        return all(information is "" for information in extracted_information)
