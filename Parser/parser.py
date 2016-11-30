from Utilities.csvUtilies import CsvUtilities
from Utilities.xmlUtilities import XmlUtilities
from Utilities.bestBuyRequestUtilies import BestBuyRequests


class Parser(object):
    """ This class will help us to parse data from JSON to CSV """
    csv_utilities = None
    xml_utilities = None
    api_request = None

    def __init__(self):
        super(Parser, self).__init__()
        self.csv_utilities = CsvUtilities()
        self.xml_utilities = XmlUtilities()
        self.api_request = BestBuyRequests()

    def generate_reviews_csv_file(self, file_name, api_key, email):
        products_info = self.csv_utilities.get_product_name_and_sku(file_name)
        print(products_info)
        skus = ','.join(str(i[0]) for i in products_info)
        products_xml_file = self.api_request.getReviews_by_products_sku(skus, api_key)
        xml_data = self.xml_utilities.get_xml_data(products_xml_file)
        self.csv_utilities.create_file('productsTest.csv', xml_data, products_info, email)


parser = Parser()
parser.generate_reviews_csv_file(
    '/home/viaro-adolfo/Downloads/products_export.csv',
    'vgQ8Iy2MFywrleVbzW3ZgAtF',
    'adolfo.morales@viaro.net'
)
