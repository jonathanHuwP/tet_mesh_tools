#!/usr/bin/env python3
"""
 mrc_threshold.py

  A script that reads a mrc file and set all voxels less than than the
  thershold to zero, then outputs to a new file.


  ----------------------


 This file is part of the FFEA simulation package

 Copyright (c) by the Theory and Development FFEA teams,
 as they appear in the README.md file.

 FFEA is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 FFEA is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with FFEA.  If not, see <http://www.gnu.org/licenses/>.

 To help us fund FFEA development, we humbly ask that you cite
 the research papers on the package.
"""
# set up linting conditions
# pylint: disable = import-error

import argparse
import pathlib
import sys
import datetime
import getpass
import mrcfile
from ffeamesh.mrc_utility import (threshold_mrc_image,
                                  get_cell_props,
                                  write_mrcfile)

def get_args():
    """
    get the command line arguments
        Returns
            (argparse.namespace)
    """
    description = ("reads a mrc file and set all voxels less than than "
                   "the thershold to zero, then outputs to a new file")
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-i",
                        "--input",
                        type=pathlib.Path,
                        required=True,
                        help="input file")

    parser.add_argument("-o",
                        "--output",
                        type=pathlib.Path,
                        required=True,
                        help="output file")

    parser.add_argument("-t",
                        "--threshold",
                        type=float,
                        required=True,
                        help="""filter limit all voxels with values less
                                than or equal will be set to zero""")

    parser.add_argument("-w",
                        "--overwrite",
                        action="store_true",
                        help="overwrite")

    return parser.parse_args()

def validate_args(args):
    """
    check the command line arguments are sane
    Args
        args (argparse.Namespace)
    Returns:
        (str/None) error message if problem else None
    """
    if not args.input.exists():
        return f"file {args.input} does not exist!"

    if not args.overwrite and args.output.exists():
        return f"file {args.output} already exists run with -w to overwrite"

    return None

def main():
    """
    run the script
    """
    args = get_args()
    message = validate_args(args)
    if message is not None:
        print(message, file=sys.stderr, flush=True)
        sys.exit()

    with mrcfile.mmap(args.input, 'r') as mrc:
        data = threshold_mrc_image(mrc.data, args.threshold)
        date = datetime.datetime.now().strftime("%x")
        label = f"made by {getpass.getuser()}, on {date}"
        write_mrcfile(data, get_cell_props(mrc), args.output, label, args.overwrite)
        print(f"thresholded output from {args.input} written to {args.output}")

if __name__ == "__main__":
    main()
