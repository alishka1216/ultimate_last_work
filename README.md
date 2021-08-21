# KitchenBot
Для запуска проекта установите python версии 3.7 и выше, pip и virualenv

Поссле клонирования перейдите в склонированную папку и вывполните следующие команды:

Создайте виртуальное окружение командой
```bash
python3 -m venv venv
```

Активируйте виртуальное окружение командой
```bash
source venv/bin/activate
```

Перейдите в папку server
```bash
cd server
```

Установите зависимости командой

```bash
pip install -r requirements.txt
```

Примените миграции командой
```bash
./manage.py migrate
```

изменил настройки для postgress

изменил поля баз данных и сикрет кей

данные для пользования базы данных находяться в файле .env

.env
DEBUG=True


SECRET_KEY=django-insecure-l87w5hu551=#rh)1bbtw+=&uar+_+0a4yzq&29&g^%82^rtnnh


DB_NAME=postgres


DB_USER=alishka


DB_PASSWORD=admin


DB_HOST=localhost


DB_PORT=5432


