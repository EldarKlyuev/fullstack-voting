# fullstack-voting

## Первый запуск
### Бэкенд 
```
python -m venv venv
venv/Scripts/activate
cd app
python manage.py migrate
python manage.py runserver
```

### Фронт
```
cd client/quasar-project
npm i
npm run dev
```

<i>Реализовано создание, удаление голосований. Фронт минимальный. Далее будет привязано к пользователю. В таблице уже есть роль для пользователя</i>
<i>Если надо показывать фронт, то по пути есть главный компонент fullstack-voting\client\quasar-project\src\components\PollForm.vue</i>
<i>Если надо показывать бэк и запросы то в app/core url это урлы. В app/vote models это модели/таблицы БД, в app/vote views вью как обрабатываются запросы.</i>
