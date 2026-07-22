"""Simple challenge retrieval script."""


import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), os.pardir))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from repository.challenge_repository import find_challenge

x = find_challenge(25)
print(x.get("name"))

