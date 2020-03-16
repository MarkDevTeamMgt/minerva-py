#!/usr/bin/env python
import sys

import pytest


def run_all(argv=None):
    # always insert coverage when running tests through setup.py
    if argv is None:
        argv = ['--verbose', '--junitxml', 'junit.xml', '--variables', 'tests/variables.yaml']
    else:
        argv = argv[1:]

    sys.exit(pytest.main(argv))


if __name__ == '__main__':
    run_all(sys.argv)
