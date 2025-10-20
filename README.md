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
