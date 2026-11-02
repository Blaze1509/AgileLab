# Start the app first:  docker run -d -p 8080:5000 attendance-app
# Then run:             python login_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "http://localhost:8080"


def login(driver, username, password):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "#login-btn").click()
    return wait


driver = webdriver.Chrome()

# Test 1: valid login
wait = login(driver, "student", "1234")
welcome = wait.until(EC.visibility_of_element_located((By.ID, "welcome")))
assert "Login successful" in welcome.text
print("PASS: valid login ->", welcome.text)

# Test 2: invalid login
wait = login(driver, "student", "wrong")
error = wait.until(EC.text_to_be_present_in_element((By.ID, "message"), "Invalid"))
assert error
print("PASS: invalid login ->", driver.find_element(By.XPATH, "//p[@id='message']").text)

driver.quit()
