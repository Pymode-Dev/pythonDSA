import argparse
import datetime
from pathlib import Path


parse = argparse.ArgumentParser(
    prog="ls",
    description="List the content of a directory",
    epilog="Thanks for using %(prog)s! 👍",
    argument_default=argparse.SUPPRESS
)

general = parse.add_argument_group("general output")
general.add_argument("path")

detailed = parse.add_argument_group("detailed ouput")
detailed.add_argument("-l", "--long", action="store_true")

args = parse.parse_args()
target_dir = Path(args.path)

def build_output(entry, long=False):
    if long:
        size = entry.stat().st_size
        date = datetime.datetime.fromtimestamp(
            entry.stat().st_mtime
        ).strftime("%b %d %H:%M:%S")
        return f"{size:>6d} {date} {entry.name}"
    return entry


for entry in target_dir.iterdir():
    try:
        long = args.long
    except AttributeError:
        long = False
    print(build_output(entry, long=long))