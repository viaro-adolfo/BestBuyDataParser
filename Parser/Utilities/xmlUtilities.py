import xml.etree.ElementTree as ET


class XmlUtilities(object):
    """docstring for JsonUtilities"""

    def get_xml_data(self, data=''):
        root = ET.fromstring(data)
        data = []
        required_data = [
            'rating',
            'title',
            'reviewer',
            'comment',
            'submissionTime',
            'sku'
        ]

        for child in root:
            row_data = []

            for attr in child:
                tag = attr.tag
                tag_val = attr.text

                if tag not in required_data:
                    continue

                if tag == 'reviewer':
                    tag_val = attr.find('name').text

                row_data.append(tag_val)
            data.append(row_data)
        return data
