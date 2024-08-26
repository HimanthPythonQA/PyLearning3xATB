# fixture is a concept in python/fixture is used to do multi task.
# fixture is used to add context to test/similar to pre condition & post condition
# eg we need to update a request the pre conditions we require is TOKEN-->Booking id-->fixture
# setUP and TearDown--->> pre and post condition
import pytest


@pytest.fixture()
def is_married():
    return True


def test_i_need_confirm(is_married):
    assert is_married == True
