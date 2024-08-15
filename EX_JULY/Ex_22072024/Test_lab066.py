import pytest
import allure

@allure.title("Smoke TC1")
@allure.description("check 1-1 = 0")
@pytest.mark.smoke
def test_sub0():
    assert 1-1 == 0


@allure.title("TC2")
@allure.description("check 2-2 = 0")
@pytest.mark.regression
def test_sub1():
    assert 2-2 == 0


@allure.title("TC3")
@allure.description("check 3-3 = 0")
@pytest.mark.smoke
def test_sub2():
    assert 3-3 == 0


@allure.title("TC4")
@allure.description("check 4-4 = 0")
@pytest.mark.sanity
def test_sub3():
    assert 4 - 4 == 0


@allure.title("TC5")
@allure.description("check 5-5 != 0")
@pytest.mark.skip(reason="not working skip it" )
def test_sub4():
    assert 5-5 != 0