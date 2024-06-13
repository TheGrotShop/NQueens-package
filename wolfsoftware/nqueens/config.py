"""
This module provides functionality to create a configuration object from parsed command-line arguments.

This module defines a function that converts parsed command-line arguments into a SimpleNamespace configuration
object. The configuration object contains all necessary parameters derived from the command-line arguments.
"""

from argparse import Namespace
from types import SimpleNamespace


def create_configuration_from_arguments(args: Namespace) -> SimpleNamespace:
    """
    Create and returns a configuration object from the provided command-line arguments.

    This function takes a Namespace object containing parsed command-line arguments and converts it into a
    SimpleNamespace configuration object. The configuration object includes parameters for verbose mode, debug
    mode, required parameters, and optional parameters.

    Args:
        args (Namespace): The parsed command-line arguments.

    Returns:
        SimpleNamespace: The configuration object containing the parameters derived from the command-line arguments.
    """
    config: SimpleNamespace = SimpleNamespace()

    config.verbose = args.verbose
    config.board_size = args.board_size

    return config
