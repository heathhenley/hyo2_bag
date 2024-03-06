import os
import logging
import sys
import argparse

from hyo2.bag import __version__
from hyo2.bag.bag import BAGFile, is_bag

logging.getLogger().setLevel(logging.DEBUG)


def main(argv=None):
    if argv is not None:
        sys.argv = argv
    app_name = "bag_validate"
    app_info = "Validation of an OpenNS BAG file, using hyo2.bag r%s" % __version__

    parser = argparse.ArgumentParser(prog=app_name, description=app_info)
    parser.add_argument("bag_file", type=str, help="a valid BAG file to validate")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.debug("> verbosity: ON")

        logging.debug("> input: %s" % args.bag_file)

    if not os.path.exists(args.bag_file):
        parser.exit(1, "ERROR: the input valid does not exist: %s" % args.bag_file)

    if not is_bag(args.bag_file):
        parser.exit(1, "ERROR: the input valid does not seem a BAG file: %s" % args.bag_file)

    bf = BAGFile(args.bag_file, mode='r')
    logging.debug(bf.validation_info())


if __name__ == "__main__":
    main()
