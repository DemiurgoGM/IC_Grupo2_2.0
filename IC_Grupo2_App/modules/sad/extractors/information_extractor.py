import re


class InformationExtractor:

    def __init__(self, content=""):
        self.content = content

    def extract_all_informations(self, content):
        self.content = content
        return (
            self.extract_office_number(), self.extract_process_number(), self.extract_subject(),
            self.extract_originator())

    def extract_office_number(self):
        regex1 = '((?<=o)([ ]*[0-9]+[ ]*\/[ ]*[0-9]{4}))'
        regex2 = '((?<=deg)([ ]*[0-9]+[ ]*\/[ ]*[0-9]{4}))'

        pattern = re.compile(r'(%s|%s)' % (regex1, regex2))

        return self.search_pattern(pattern)

    def extract_process_number(self):
        pattern = re.compile(r'([0-9]{10}\.[0-9]{6}\/[0-9]{4}-[0-9]{2})')
        return self.search_pattern(pattern)

    def extract_subject(self):
        pattern = re.compile(
            r'([0-9]{7}[ ]*[.-][ ]*[0-9]{2}[ ]*[.]*[ ]*[0-9]{4}[ ]*[.]*[ ]*[0-9][ ]*[.]*[ ]*[0-9]{2}[ ]*[.]*[ ]*[0-9]{4})')
        return self.search_pattern(pattern)

    def extract_originator(self):
        regex1 = '((?<=promovida por)([\s\S]*)(?=naquela))'
        regex2 = '((?<=movid[ao] por )([\s\S]*?)(?=,))'
        regex3 = '((?<=movida por )([\s\S]*)(?= notadamente))'
        regex4 = '((?<=INTERESSADO: )([\s\S]*)(?=  Senhor Secretario))'
        regex5 = '((?<=Requerente: )([\s\S]*)(?= Interessado))'
        regex6 = '((?<=promovida por)([\s\S]*)(?=,))'
        regex7 = '((?<=[.][0-9]{4}-)([\s\S]*?)(?=notadamente))'
        regex8 = '((?<=proposta pelo)([\s\S]*)(?=. Referencia))'
        regex9 = '((?<=proposta por)([\s\S]*)(?=.   Senhor))'

        pattern = re.compile(
            r'(%s|%s|%s|%s|%s|%s|%s|%s|%s)' % (regex1, regex2, regex3, regex4, regex5, regex6, regex7, regex8, regex9))

        return self.search_pattern(pattern)

    def search_pattern(self, pattern):
        matches = pattern.search(self.content)
        return matches.group().strip() if matches else ""
