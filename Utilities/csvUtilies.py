import csv


class CsvUtilities(object):
    """docstring for CsvUtilities"""

    def create_file(file_name='reviews.txt', data=[]):
        if not data:
            return None

        with open(file_name, 'wb') as csvfile:
            csv_writer = csv.writer(
                csvfile,
                delimiter=','
            )

            csv_writer.writerow(
                ['name', 'rating', 'title', 'author', 'email', 'body', 'created_at']
            )

            for row in data:
                add_row = [
                    row[5],
                    row[1],
                    row[2],
                    row[0],
                    row[6],
                    row[3],
                    row[4]
                ]
                # print(add_row)
                csv_writer.writerow(add_row)
        return file_name

    def read_file(filename):
        try:
            with open(filename) as csvfile:
                file_data = csv.DictReader(csvfile)
        except:
            file_data = None

        return file_data

    def get_product_name_and_sku(csv_data):
        return_data = []
        for row in csv_data:
            if not row['Variant SKU'] or not row['Handle']:
                continue

            row_data = [
                row['Variant SKU'],
                row['Handle']
            ]

            return_data.append(row_data)

        return return_data
