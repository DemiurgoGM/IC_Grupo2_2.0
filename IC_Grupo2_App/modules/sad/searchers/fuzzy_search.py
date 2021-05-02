import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


class FuzzySearch:

    def __init__(self):
        self.contents = pd.read_excel(r'IC_Grupo2_App/modules/sad/database/enderecos.xlsx')

    def for_address(self, column, address):
        matches = process.extract(address, self.contents[column], limit=5, scorer=fuzz.token_sort_ratio)

        score = [s[1] for s in matches]

        match_addresses = [match_address[0] for match_address in matches]

        output_data_frame = pd.DataFrame()

        for match in match_addresses:
            results = self.contents.loc[self.contents[column] == match]
            output_data_frame = output_data_frame.append(results)

        return output_data_frame, score
