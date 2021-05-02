from .extractors.information_extractor import InformationExtractor
from .helpers.directory import Directory
from .readers.reader import DocumentReader
from .application import Application
from .readers.ocr_reader import OCRDocumentReader
from .readers.simple_reader import SimpleDocumentReader
from .output.output import Output
from .searchers.fuzzy_search import FuzzySearch

import os


class ApplicationFactory:

    def get_application_instance(self, file, address):
        directory = Directory()
        readers = [SimpleDocumentReader(), OCRDocumentReader()]
        extractor = InformationExtractor()
        output = Output()
        search = FuzzySearch()

        return Application(file, address, directory, readers, extractor, output, search)
