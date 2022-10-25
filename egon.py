import argparse
from jls import jls
from lcsec import csec
from nvloc import nvloc

# Percentile code taken from Python recipes/templates found here:
## {{{ http://code.activestate.com/recipes/511478/ (r1)
import math


def percentile(N, percent, key=lambda x: x):
    """
    Find the percentile of a list of values.

    @parameter N - is a list of values. Note N MUST BE already sorted.
    @parameter percent - a float value from 0.0 to 1.0.
    @parameter key - optional key function to compute value from each element of N.

    @return - the percentile of the values
    """
    if not N:
        return None
    k = (len(N) - 1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c - k)
    d1 = key(N[int(c)]) * (k - f)
    return d0 + d1


## end of http://code.activestate.com/recipes/511478/ }}}


def egon(path, seuil):
    metadata = jls(args.path)
    csec_dict = csec(args.path, metadata)
    for m in metadata:
        f_path = m[0]
        m.append(len(csec_dict[f_path]))
        m.append(nvloc(f_path))

    sorted_by_csec = sorted(metadata, key=lambda m: m[3], reverse=True)
    sorted_by_nvloc = sorted(metadata, key=lambda m: m[4], reverse=True)

    csec_threshold = percentile(sorted_by_csec, seuil, key=lambda m: m[3])
    nvloc_threshold = percentile(sorted_by_nvloc, seuil, key=lambda m: m[4])

    # only keep classes divines:
    metadata = list(
        filter(lambda m: m[4] >= nvloc_threshold and m[3] >= csec_threshold,
               metadata))
    return metadata


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--path',
                        type=str,
                        help='Path of a Java package',
                        required=True)
    parser.add_argument('--seuil',
                        type=float,
                        help='Value between 0 and 1 representing a %',
                        required=True)
    args = parser.parse_args()

    metadata = egon(args.path, args.seuil)
    for m in metadata:
        print(m[0], m[1], m[2], m[3], m[4], sep=',')