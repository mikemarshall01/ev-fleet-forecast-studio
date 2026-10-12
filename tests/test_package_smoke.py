import fleet_studio


def test_package_import_and_version() -> None:
    assert fleet_studio.__version__ == "0.1.0"
