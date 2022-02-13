"""Basic test for version check."""
import os
import unittest

from napalm_panos import __version__ as project_version

import toml


class TestVersion(unittest.TestCase):
    """Test Version is the same."""

    def test_version(self):
        """Verify that pyproject.toml version is same as version specified in the package."""
        parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        poetry_version = toml.load(f"{parent_path}/pyproject.toml")["tool"]["poetry"]["version"]
        self.assertEqual(project_version, poetry_version)
