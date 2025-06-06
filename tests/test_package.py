from __future__ import annotations

import importlib.metadata

import hiden as m


def test_version():
    assert importlib.metadata.version("hiden") == m.__version__
