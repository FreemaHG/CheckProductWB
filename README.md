# Описание проекта

Проект представляет скрипт, который выводит порядковый номер товара (по его артикулу) 
при поиске товара по названию (форма поиска).

## Сборка и запуск
1. Скачиваем содержимое репозитория в отдельную папку:
    ```
    git clone https://github.com/FreemaHG/CheckProductWB.git
    ```
   
2. Создаем и активируем виртуальное окружение:
    ```
    python3 -m venv venv
    ```
    Unix-системы:
    ```
    source venv/bin/activate
   ```
   Windows:
   ```
    venv\Scripts\activate
    ```

3. Устанавливаем зависимости:
    ```
    pip install -r requirements.txt
    ```

4. Запускаем скрипт:
    ```
    python3 main.py
    ```
Артикул и фраза для поиска товара задаются в переменных **ARTICLE** и **SEARCH_PHRASE** соответственно.

![](/screens/2.png)
![](/screens/1.png)