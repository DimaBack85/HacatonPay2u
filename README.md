# The backend of the project with services and subscriptions. Created to participate in a team hackathon.

## Эндпойнты:

### GET

* /api/v1/subscription/ (Список названий всех доступных подписок приложения. Главная страница)
* /api/v1/subscription/details/<int:pk>/ (Конкретная подписка с описанием)
* /api/v1/user/notification/ (Список уведомлений пользователя)
* /api/v1/user/subscription/ (Список всех подписок пользователя)