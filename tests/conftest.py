import sys
from pathlib import Path

# Make the repo root importable so `scripts` resolves when pytest is run
# from any directory.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from scripts import helpers


@pytest.fixture(autouse=True)
def reset_kev_catalog():
    """
    Clear the process-wide CISA KEV cache around every test.

    _get_kev_catalog memoises the catalog in a module-level global, so without
    this a test that populates it would leave later tests reading that copy
    instead of their own stub.
    """
    helpers._kev_catalog = None
    yield
    helpers._kev_catalog = None
