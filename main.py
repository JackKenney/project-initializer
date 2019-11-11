#! Python 3
from subprocess import call
import argparse
import sys

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "--root",
    default=".",
    help="The full path or relative path from the current\
    directory to the location where the folder should be created. Ex. --root test",
)
parser.add_argument(
    "--features",
    metavar="N",
    type=str,
    nargs="+",
    default="example",
    help="The list of features that belong to the system. Ex. --features feat1 feat2",
)

folders = [
    "build",
    "src/features",
    "src/types",
    "db",
    "references",
    "examples",
    "public/scripts",
    "public/styles",
]


def build_tree(args):
    for folder in folders:
        call(["mkdir", "-p", args.root + folder])

    for feature in args.features:
        call(["mkdir", "-p", args.root + "features/" + feature + "/api"])
        call(["mkdir", "-p", args.root + "features/" + feature + "/components"])
        call(["mkdir", "-p", args.root + "features/" + feature + "/tests"])
        call(["mkdir", "-p", args.root + "features/" + feature + "/types"])


if __name__ == "__main__":
    args = parser.parse_args(sys.argv)
    if args.root[len(args.root) - 1] != "/":
        args.root = args.root + "/"
    build_tree(args)
