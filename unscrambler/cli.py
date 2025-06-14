import argparse
import yaml
from .core import unscramble

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("numpages", type=int, help="The number of pages per document", nargs="?")
    parser.add_argument("-b", "--booklet", action="store_true", help="Use this option if the original is an A3 booklet. Source PDF is expected to be in landscape with the middle pages coming first.")
    parser.add_argument("-s", "--split", action="store_true", help="Use this option if you would like the output to be split into multiple files.")
    parser.add_argument("-r", "--rearrange", action="store_true", help="Use this option to rearrange the pages.")
    parser.add_argument("-d", "--doublePage", action="store_true", help="Use this option to rearrange pages so that double pages stay together. This assumes there is a front and back cover.")
    parser.add_argument("-D", "--doublePageReversed", action="store_true", help="Use this option when unscrambling a document for which the -d option was used.")
    parser.add_argument("-y", "--parseYAML", help="Use when options are being parsed from a YAML file.")

    args = parser.parse_args()
    
    if args.parseYAML:
        with open(args.parseYAML, "r") as yamlFile:
            options = yaml.safe_load(yamlFile.read())
            numpages = options["number_of_pages"]
            booklet = options["booklet"]
            split = options["split"]
            rearrange = options["rearrange"]
            doublePage = options["double_page"]
            doublePageReversed = options["reverse_double_page"]
        unscramble(args.filename, numpages, booklet, split, rearrange, doublePage, doublePageReversed)
    else:
        unscramble(args.filename, args.numpages, args.booklet, args.split, args.rearrange, args.doublePage, args.doublePageReversed)

if __name__ == "__main__":
    main() 