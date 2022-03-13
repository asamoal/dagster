import inspect
import re

import pytest

import dagster


def test_all():
    dagster_dir = dir(dagster)
    for each in dagster.__all__:
        assert each in dagster_dir
    for exported in dagster_dir:
        if (
            not exported.startswith("_")
            and not inspect.ismodule(getattr(dagster, exported))
            and not exported in dagster._DEPRECATED  # pylint: disable=protected-access
        ):
            assert exported in dagster.__all__


def test_deprecated_imports():
    with pytest.warns(DeprecationWarning, match=re.escape('"EventMetadataEntry" is deprecated')):
        from dagster import EventMetadataEntry, MetadataEntry
    assert EventMetadataEntry is MetadataEntry


def test_deprecated_submodule_import_paths():
    import dagster._core
    import dagster._core.definitions
    import dagster.core  # type: ignore
    import dagster.core.definitions  # type: ignore

    assert dagster.core == dagster._core  # pylint: disable=protected-access
    assert dagster.core.definitions == dagster._core.definitions  # pylint: disable=protected-access
