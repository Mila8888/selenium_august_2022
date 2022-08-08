def test_hello_selenium1(driver):
    driver.get(url=driver.base_url)
    assert driver.title == "YourStore"


def test_hello_selenium2(driver):
    driver.get(url=driver.base_url)
    assert driver.title == "Your Store"
