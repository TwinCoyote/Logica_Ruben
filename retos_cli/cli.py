import sys
from retos_cli.core.create import create_challenge_file
from retos_cli.core.review import review_challenge
import argparse


def main(args: list[str] | None = None) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    # Main parser
    parser = argparse.ArgumentParser(
        prog="reto",
        description="CLI tool to manage coding challenges.",
    )

    # Create subcommands handler (create, review, etc.)
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Command to execute",
    )

    # Subcommand: create
    parser_create = subparsers.add_parser("create", help="Create a file for the specified challenge.")
    parser_create.add_argument("number", type=int, help="Challenge number")

    # Subcommand: review
    parser_review = subparsers.add_parser("review", help="Review the challenge solution.")
    parser_review.add_argument("number", type=int, help="Challenge number")

    # Parse arguments: pass custom args sliced if provided, otherwise argparse uses sys.argv[1:]
    parsed_args = parser.parse_args(args[1:] if args is not None else None)

    # Execute logic based on the parsed command
    if parsed_args.command == "create":
        print(create_challenge_file(parsed_args.number))
    elif parsed_args.command == "review":
        print(review_challenge(parsed_args.number))


if __name__ == "__main__":
    main()
