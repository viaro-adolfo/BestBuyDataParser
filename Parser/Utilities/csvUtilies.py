import csv


class CsvUtilities(object):
    """docstring for CsvUtilities"""

    def create_file(self, file_name='reviews.txt', data=[], products_info=[], email=''):
        if not data:
            return None

        with open(file_name, 'wb') as csvfile:
            csv_writer = csv.writer(
                csvfile,
                delimiter=','
            )

            csv_writer.writerow(
                ['product_handle', 'rating', 'title', 'author', 'email', 'body', 'created_at']
            )

            for row in data:
                product_name = ''
                for product in products_info:
                    if product[0] == row[0]:
                        product_name = product[1]

                add_row = [
                    product_name,
                    row[2],
                    row[3],
                    row[1],
                    email,
                    row[4],
                    row[5]
                ]
                # print(add_row)
                csv_writer.writerow(add_row)
        return file_name

    def create_file_with_json_data(self, file_name='reviews.txt', data=[], products_info=[], email=''):
        if not data:
            return None

        with open(file_name, 'wb') as csvfile:
            csv_writer = csv.writer(
                csvfile,
                delimiter=','
            )

            csv_writer.writerow(
                ['product_handle', 'rating', 'title', 'author', 'email', 'body', 'created_at']
            )

            for row in data:
                product_name = ''
                for product in products_info:
                    if int(product[0]) == row['sku']:
                        product_name = product[1]

                add_row = [
                    product_name,
                    row['rating'],
                    row['title'],
                    row['reviewer'],
                    email,
                    row['comment'],
                    row['submissionTime']
                ]
                # print(add_row)
                csv_writer.writerow(add_row)
        return file_name

    def get_product_name_and_sku(self, filename):
        with open(filename) as csvfile:
            file_data = csv.DictReader(csvfile)

            return_data = []
            for row in file_data:
                if not row['Variant SKU'] or not row['Handle']:
                    continue

                row_data = [
                    row['Variant SKU'].replace("'", ""),
                    row['Handle']
                ]

                return_data.append(row_data)

            return return_data
