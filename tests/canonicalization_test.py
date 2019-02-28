import canonicalization
import os
import sys


def test_canonical():
    directory = os.path.dirname(sys.argv[0])
    canonicalization.canonicalize(os.path.join(directory, 'canonical-test-data'), directory)
    master_path = os.path.join(directory, 'Master.txt')
    master_file = open(master_path, 'r')
    i = 1
    match = 0
    for line in master_file:
        if line == i:
            i += 1
            match += 1
    assert match == len(master_file)
    os.remove(master_path)


if __name__ == '__main__':
    test_canonical()
