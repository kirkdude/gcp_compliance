# -*- coding: utf-8 -*-
import argparse
import logging
from checker import ComplianceChecker


def parse_args():
    parser = argparse.ArgumentParser(description="GCP Compliance Checker")
    parser.add_argument(
        "--dry-run", action="store_true", help="Run the checks without making changes"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    return parser.parse_args()


def setup_logging(verbose):
    logging_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=logging_level, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def main():
    args = parse_args()
    setup_logging(args.verbose)
    checker = ComplianceChecker(dry_run=args.dry_run)
    checker.run_checks()


if __name__ == "__main__":
    main()
