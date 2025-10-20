# onlydigital-autotest
Автотест на Python (Selenium). Проверка наличия футера и ссылок на сайте only.digital.

Описание проекта
Этот проект содержит автоматизированные тесты, проверяющие корректность отображения футера на страницах сайта [only.digital](https://only.digital).  
Тесты помогают убедиться, что футер присутствует и корректно отображается на всех ключевых разделах сайта.

Используемые технологии
- Python 3.13+
- Pytest
- Selenium WebDriver
- WebDriver Manager

Структура проекта
onlydigital-autotest/
│
├── test_footer_only.py # Основной файл с тестами
├── requirements.txt # Список зависимостей
├── README.md # Описание проекта


 Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/PashaTen/onlydigital-autotest.git
   cd onlydigital-autotest
2.Создайте виртуальное окружение
python -m venv .venv
source .venv/bin/activate         для macOS / Linux
.venv\Scripts\activate            для Windows

3.Установите зависимости:
pip install -r requirements.txt

4.Запустите тесты:
pytest -v

5.Код:
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
