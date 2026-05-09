#!/usr/bin/env python3
import sys
import random
from lxml import etree


def main():
    if len(sys.argv) < 2:
        print("Usage: xpath.py <query>", file=sys.stderr)
        sys.exit(1)

    query = sys.argv[1]

    import glob
    xml_files = glob.glob("./spec-build/*.xml")
    if not xml_files:
        print("No XML files found in ./spec-build/", file=sys.stderr)
        sys.exit(1)

    random_file = random.choice(xml_files)
    tree = etree.parse(random_file)

    results = tree.xpath(query)

    for result in results:
        if isinstance(result, str):
            print(result)
        else:
            print(etree.tostring(result, pretty_print=True, encoding="unicode"))


if __name__ == "__main__":
    main()