import os
import argparse


def get_metadata(f_path, f):
    return [f_path, path_as_pkg(f_path), file_without_ext(f)]


def path_as_pkg(f_path):
    norm_f_path = os.path.normpath(f_path)
    norm_dir_path = os.path.dirname(norm_f_path)
    parts = norm_dir_path.split(os.sep)
    return '.'.join(parts)


def file_without_ext(f):
    return os.path.splitext(f)[0]


def is_java_file(f_path):
    ext = os.path.splitext(f_path)[-1].lower()
    return ext == ".java"


def jls(path):
    metadata = []

    def dfs(path):
        for f in os.listdir(path):
            f_path = os.path.join(path, f)
            if os.path.isdir(f_path):
                dfs(f_path)
            elif os.path.isfile(f_path) and is_java_file(f_path):
                metadata.append(get_metadata(f_path, f))

    dfs(path)
    return metadata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path',
                        type=str,
                        help='Path of a Java package',
                        required=True)
    args = parser.parse_args()
    metadata = jls(args.path)
    for m in metadata:
        print(m[0], m[1], m[2], sep=',')