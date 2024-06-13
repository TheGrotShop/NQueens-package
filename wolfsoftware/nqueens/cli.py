"""
This module provides command-line argument parsing, processing, and execution functionalities for the application.

This module defines the main functions for setting up the argument parser, processing the arguments, and running the
main logic of the application. The module uses the argparse library to handle command-line arguments and the wolfsoftware.drawlines
module to draw lines for output formatting. It also utilizes the config module to create configurations from the parsed arguments.
"""

import argparse
import sys

from types import SimpleNamespace

from .config import create_configuration_from_arguments
from .globals import ARG_PARSER_DESCRIPTION, ARG_PARSER_EPILOG, ARG_PARSER_PROG_NAME, VERSION_STRING
from .nqueens import Board


def positive_int(value: str) -> int:
    """
    Validate that a given value is a positive integer greater than 0.

    Argument:
        value (str): The value to validate.

    Returns:
        int: The validated positive integer.

    Raises:
        argparse.ArgumentTypeError: If the value is not a positive integer greater than 0.
    """
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"Invalid board size: {value}. Must be a positive integer greater than 0.")
    return ivalue


def setup_arg_parser() -> argparse.ArgumentParser:
    """
    Set up and returns the argument parser with all required flags, optional, and required arguments.

    This function creates an ArgumentParser object and defines the available command-line arguments, including flags for help,
    debug, verbose, and version information. It also sets up optional and required argument groups for additional parameters.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = argparse.ArgumentParser(prog=ARG_PARSER_PROG_NAME,
                                     add_help=False,
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=ARG_PARSER_DESCRIPTION,
                                     epilog=ARG_PARSER_EPILOG)

    flags: argparse._ArgumentGroup = parser.add_argument_group(title='flags')

    flags.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Show this help message and exit")
    flags.add_argument("-v", "--verbose", action="store_true", default=False, help="Enable verbose output - show the actual boards")
    flags.add_argument('-V', '--version', action="version", version=VERSION_STRING, help="Show program's version number and exit.")

    # Add the board_size as a positional argument
    parser.add_argument("board_size", nargs="?", type=positive_int, default=8, help="Size of the board (default is 8 for the Eight Queens puzzle)")

    return parser


def process_arguments(parser: argparse.ArgumentParser) -> argparse.Namespace:
    """
    Process and validates the command-line arguments.

    This function uses the provided argument parser to parse the command-line arguments. It validates the parsed arguments
    and returns them in a Namespace object.

    Args:
        parser (argparse.ArgumentParser): The argument parser to use for parsing the command-line arguments.

    Returns:
        argparse.Namespace: The parsed and validated arguments.
    """
    args: argparse.Namespace = parser.parse_args()
    return args


def run() -> None:
    """
    Master controller function.

    This function sets up the argument parser, processes the command-line arguments, creates the configuration from
    the arguments, and executes the main functionality. It handles errors related to argument parsing and exits with
    an appropriate status code in case of failure.
    """
    parser: argparse.ArgumentParser = setup_arg_parser()
    try:
        args: argparse.Namespace = process_arguments(parser)
        config: SimpleNamespace = create_configuration_from_arguments(args)
        board = Board(config)
        board.solve()
    except argparse.ArgumentTypeError as err:
        parser.print_usage()
        print(err)
        sys.exit(1)
