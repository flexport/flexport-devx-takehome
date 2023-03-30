import warnings
import os

import pytest

from rock_paper_scissors.app import app


@pytest.fixture(scope="session")
def apply_migrations():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    os.environ["ENDPOINT"] = "http://localhost:5000"
