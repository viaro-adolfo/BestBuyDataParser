from Utilities.csvUtilies import CsvUtilities
from Utilities.xmlUtilities import XmlUtilities
import requests


class Parser(object):
    """ This class will help us to parse data from JSON to CSV """
    csv_utilities = None
    xml_utilities = None

    def __init__(self):
        super(Parser, self).__init__()
        self.csv_utilities = CsvUtilities()
        self.xml_utilities = XmlUtilities()

    def generate_reviews_csv_file(self, file_name):
        csv_products = self.csv_utilities.read_file(file_name)
        products_info = self.csv_utilities.get_product_name_and_sku(csv_products)
        skus = ','.join(str(i[0]) for i in products_info)
