from Utilities.csvUtilies import CsvUtilities
from Utilities.xmlUtilities import XmlUtilities
from Utilities.bestBuyRequestUtilies import BestBuyRequests
from Utilities.jsonUtilities import JsonUtilities


class Parser(object):
    """ This class will help us to parse data from JSON to CSV """
    csv_utilities = None
    xml_utilities = None
    json_utilities = None
    api_request = None
    skus = []
    products_info = []

    def __init__(self):
        super(Parser, self).__init__()
        self.csv_utilities = CsvUtilities()
        self.xml_utilities = XmlUtilities()
        self.api_request = BestBuyRequests()
        self.json_utilities = JsonUtilities()

    def read_skus_and_products_info(self, file_name):
        products_info = self.csv_utilities.get_product_name_and_sku(file_name)
        print(products_info)
        skus = ','.join(str(i[0]) for i in products_info)

        self.skus = skus
        self.products_info = products_info

    def generate_reviews_csv_file_with_xml_format(self, api_key, email):
        products_xml_file = self.api_request.getReviews_by_products_sku(self.skus, api_key, 'xml')
        xml_data = self.xml_utilities.get_xml_data(products_xml_file)
        self.csv_utilities.create_file('productsTest.csv', xml_data, self.products_info, email)

    def generate_reviews_csv_file_with_json_format(self, api_key, email):
        products_xml_file = self.api_request.getReviews_by_products_sku(self.skus, api_key, 'json')
        json_data = self.json_utilities.get_json_data(products_xml_file)
        self.csv_utilities.create_file_with_json_data('products.csv', json_data, self.products_info, email)


parser = Parser()
parser.read_skus_and_products_info('/home/viaro-adolfo/Downloads/products_export.csv')
parser.generate_reviews_csv_file_with_json_format(
    'vgQ8Iy2MFywrleVbzW3ZgAtF',
    'adolfo.morales@viaro.net'
)
