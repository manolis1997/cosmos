import argparse

def args():
    # Create the parser
    parser = argparse.ArgumentParser(description="Process table and load parameters.")

    # Add arguments
    parser.add_argument(
        "--table",
        type=str,
        required=True,
        help="Name of the table"
    )

    parser.add_argument(
        "--load",
        type=str,
        choices=["FL", "CDC"],  # restrict to these options
        required=True,
        help="Load type: 'FL' or 'CDC'"
    )

    # Parse the arguments
    args = parser.parse_args()

    return args.table, args.load