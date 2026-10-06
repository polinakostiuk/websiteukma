# Сайт факультету гуманітарних наук (НаУКМА)

Навчальний проєкт на Django: головна, кафедри, спеціальності, програми обміну.

## Запуск

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate          # створює таблиці й наповнює сайт даними
python manage.py createsuperuser  # для входу в /admin/
python manage.py runserver
```

## Сторінки

| URL | Що там |
|---|---|
| `/` | опис факультету, контакти |
| `/programs/`, `/programs/<id>/` | спеціальності |
| `/departments/`, `/departments/<id>/` | кафедри та викладачі |
| `/exchange/` | програми академічного обміну |
| `/admin/` | керування контентом |

## Про дані

Назви кафедр і спеціальностей, координатори та описи програм узяті з 
(https://www.ukma.edu.ua/index.php/osvita/fakulteti/fen)
Файл бази `db.sqlite3` не додаю на git: структуру й початкові дані відтворюють міграції.

## Використання ШІ 
- Інструменти. Claude.
-Що зроблено з допомогою ШІ. 
чернетка міграцій частини 2 (RunSQL, RunPython, зворотні операції) та розбір помилок.
Також з пошуком інформації про факультет економічних наук на сайтах НаУКМА
Дані про факультет взято з ukma.edu.ua та vstup.ukma.edu.ua.
-Як перевірено. makemigrations --check, migrate faculty_site zero
і повторний migrate, а також роботу сторінок сайту й адмінки. 

Відповіді на питання завдання: [ANSWERS.md](ANSWERS.md).