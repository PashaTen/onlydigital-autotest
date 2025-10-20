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

Пример теста
import pytest
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
def test_footer_exists(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))
        print(f"Футер найден на странице: {url}")
    except TimeoutException:
        pytest.fail(f"Футер не найден на странице: {url}")
    finally:
        driver.quit()

