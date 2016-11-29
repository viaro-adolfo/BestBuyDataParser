class JsonUtilities(object):
    """docstring for JsonUtilities"""
    def __init__(self, arg):
        super(JsonUtilities, self).__init__()
        self.arg = arg

    def json_to_array(self, isProduct=True, data={}):
        if isProduct:
            return self.get_products_data(data)
        return self.get_reviews_data(data)

    def get_json_headers(self, isProduct=True, data={}):
        if isProduct:
            return self.get_products_headers(data)
        return self.get_reviews_headers(data)
        return True

    def get_products_data(data={}):
        return True

    def get_reviews_data(data={}):
        return True

    def get_products_headers(data={}):
        return True

    def get_reviews_headers(data={}):
        return True
