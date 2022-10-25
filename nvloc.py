import argparse
import os


def is_java_file(f_path):
    ext = os.path.splitext(f_path)[-1].lower()
    return ext == ".java"


def nvloc(path):
    loc = 0
    with open(path) as f:
        for line in f:
            if line.strip() not in ['', '\n', '\r\n']:
                loc += 1
    return loc


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path',
                        type=str,
                        help='Path of a Java class',
                        required=True)
    args = parser.parse_args()

    if not os.path.isfile(args.path) or not is_java_file(args.path):
        raise Exception("Input path needs to be a Java class")

    print(nvloc(args.path))