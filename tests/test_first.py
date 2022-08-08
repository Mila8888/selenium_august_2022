def test_hello_selenium1(driver):
    driver.get(url="http://192.168.0.101:8081/")
    assert driver.title == "YourStore"


def test_hello_selenium2(driver):
    driver.get(url="http://192.168.0.101:8081/")
    assert driver.title == "Your Store"
