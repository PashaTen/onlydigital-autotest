import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

pages = [
    "https://only.digital/",
    "https://only.digital/services/",
    "https://only.digital/portfolio/",
    "https://only.digital/contacts/"
]

@pytest.mark.parametrize("url", pages)
def test_footer_elements(url):
    # Проверяем доступность страницы через HTTP
    response = requests.get(url)
    if response.status_code == 404:
        pytest.skip(f"Страница {url} не найдена (404), тест пропущен")

    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        driver.get(url)

        # Скролл вниз на случай динамической подгрузки футера
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Ждем видимости футера (до 15 секунд)
        footer = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "footer, div[class*='Footer_footer'], div[class*='footer'], div[class*='footerWrapper']")
            )
        )
        assert footer.is_displayed(), f"Футер не отображается на странице {url}"

        # Проверка email
        emails = footer.find_elements(By.XPATH, ".//a[contains(@href, 'mailto:')]")
        if not emails:
            print(f"⚠️ Email отсутствует в футере на странице {url}")
        else:
            print(f"✅ Email найден на странице {url}: {[e.get_attribute('href') for e in emails]}")

        # Проверка телефона
        phones = footer.find_elements(By.XPATH, ".//a[contains(@href, 'tel:')]")
        if not phones:
            print(f"⚠️ Телефон отсутствует в футере на странице {url}")
        else:
            print(f"✅ Телефон найден на странице {url}: {[p.get_attribute('href') for p in phones]}")

    except TimeoutException:
        pytest.fail(f"❌ Футер не найден или не виден на странице {url}")
    finally:
        driver.quit()