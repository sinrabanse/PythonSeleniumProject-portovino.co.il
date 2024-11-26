import pytest


@pytest.fixture()
def set_up(request):
    test_name = request.node.name
    print(f"Start Test: {test_name}")
    yield
    print(f"Finish Test: {test_name}")

@pytest.fixture(scope="module")
def set_group():
    print(f"Enter system")
    yield
    print(f"Exit system")