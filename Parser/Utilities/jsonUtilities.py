import json


class JsonUtilities(object):
    """docstring for JsonUtilities"""
    def get_json_data(self, data=''):
        root = json.loads(data)
        data = []
        required_data = [
            'rating',
            'title',
            'reviewer',
            'comment',
            'submissionTime',
            'sku'
        ]

        for child in root['reviews']:
            row_data = {
                'rating': '',
                'title': '',
                'reviewer': '',
                'comment': '',
                'submissionTime': '',
                'sku': ''
            }

            for attr in child:
                if attr not in required_data:
                    continue

                tag_val = child[attr]
                if attr == 'reviewer':
                    tag_val = tag_val[0]['name']

                if type(tag_val) == unicode:
                    # This is done because sometimes is a unicode and not a string
                    # And we have to remove the 'enters'
                    tag_val = tag_val.encode('ascii', 'ignore')
                    tag_val = tag_val.replace("\r\n", " ")
                    tag_val = tag_val.replace(r"\r\n", " ")
                row_data[attr] = tag_val
            data.append(row_data)
        return data
