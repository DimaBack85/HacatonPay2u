# The backend of the project with services and subscriptions. Created to participate in a team hackathon.

## Эндпойнты:

|Метод|Эндпойнт|Описание|
|-|--------|---|
|GET|/api/v1/subscription/|Список названий всех доступных подписок приложения. Главная страница|
|GET|/api/v1/subscription/details/<int:pk>/|Конкретная подписка с описанием|
|GET|/api/v1/user/notification/|Список уведомлений пользователя|
|GET|/api/v1/user/subscription/|Список всех подписок пользователя|
