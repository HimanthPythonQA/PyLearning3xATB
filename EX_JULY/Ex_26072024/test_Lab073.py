import pytest

@pytest.fixture()
def sample_data():
    data = [1,2,3,4,5]
    return data


@pytest.fixture()
def sample_data1():
    return True


def test_consume_sample_1_2(sample_data,sample_data1):
    print(sample_data)
    print(sample_data1)