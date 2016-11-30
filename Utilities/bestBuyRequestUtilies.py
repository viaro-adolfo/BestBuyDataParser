import requests


class BestBuyRequests(object):

    def getReviews_by_products_sku(self, SKU, Api_Key):
        url = 'https://api.bestbuy.com/v1/reviews(sku in({}))?size=400&apiKey={}'
        url = url.format(SKU, Api_Key)
        print(url)
        response = requests.get(url)

        status = response.status_code
        headers = response.headers['content-type']
        print (status)
        print (headers)
        return response.text


#b = BestBuyRequests()
#b.getReviews_by_products_sku("8880044","vgQ8Iy2MFywrleVbzW3ZgAtF")
