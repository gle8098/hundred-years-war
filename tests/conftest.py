import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--run_load_tests", action="store_true", default=False, help="run load tests"
    )
    parser.addoption(
        "--run_stress_tests", action="store_true", default=False, help="run stress tests"
    )


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--run_load_tests"):
        # do not run load tests
        skip_load_test = pytest.mark.skip(reason="need --run_load_tests option to run")
        for item in items:
            if "loadtest" in item.keywords:
                item.add_marker(skip_load_test)
    if not config.getoption("--run_stress_tests"):
        # do not run stress tests
        skip_stress_test = pytest.mark.skip(reason="need --run_stress_tests option to run")
        for item in items:
            if "stresstest" in item.keywords:
                item.add_marker(skip_stress_test)