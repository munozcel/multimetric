import csv
import os
import argparse
import itertools
from collections import defaultdict


def metadata_from_csv(csv_path):
    metadata = []
    with open(csv_path) as f:
        reader = csv.reader(f)
        for row in reader:
            metadata.append(row)
    return metadata


def csec(dir_path, metadata):
    result = defaultdict(set)

    for a, b in itertools.combinations(metadata, 2):
        a_path, a_pkg, a_name = a[0], a[1], a[2]
        b_path, b_pkg, b_name = b[0], b[1], b[2]
        if uses(a_path, b_name) or uses(b_path, a_name):
            result[a_path].add(b_path)
            result[b_path].add(a_path)
    return result


def uses(f_path, name):
    with open(f_path) as f:
        for line in f:
            if name in line:
                return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir_path',
                        type=str,
                        help='Path of a Java package',
                        required=True)
    parser.add_argument('--jls_path',
                        type=str,
                        help='Path of the jls output in csv',
                        required=True)

    args = parser.parse_args()

    if not os.path.isdir(args.dir_path):
        raise Exception("--dir_path must be a directory")

    if not os.path.isfile(args.jls_path):
        raise Exception("--jls_path must be a csv file")

    metadata = metadata_from_csv(args.jls_path)
    csec_dict = csec(args.dir_path, metadata)

    for m in metadata:
        f_path, pkg, name = m[0], m[1], m[2]
        print(f_path, pkg, name, len(csec_dict[f_path]), sep=",")