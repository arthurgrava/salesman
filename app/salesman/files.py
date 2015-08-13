#encoding:utf-8
import csv


def read_csv(filepath, index_label, has_header=False):
    """
    Reads a csv file transforming it into a dictionary
    """
    if has_header:
        return _read_csv_with_header(filepath, index_label)
    else:
        return None


def _read_csv_with_header(filepath, index_label):
    """
    Reads a csv file expecting it to have a header
    """
    data = {}
    with open(filepath, 'r') as csv_to_read:
        reader = csv.DictReader(csv_to_read, delimiter='\t')
        for row in reader:
            index_id = row[index_label]
            del row[index_label]
            if index_id not in data:
                data[index_id] = []
            data[index_id].append(tuple(row.values()))
    return data
