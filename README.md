# DRF

## Продолжаем проект DRF

### Задание 1

* Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью
  SerializerMethodField()

### Задание 2

* Добавьте новую модель в приложение users:

#### Платежи

- пользователь,
- дата оплаты,
- оплаченный курс или урок,
- сумма оплаты,
- способ оплаты: наличные или перевод на счет.

##### Поля пользователь, оплаченный курс и отдельно оплаченный урок должны быть ссылками на соответствующие модели.

#### Запишите в эту модель данные через инструмент фикстур или кастомную команду.

### Задание 3

* Для сериализатора для модели курса реализуйте поле вывода уроков. Вывод реализуйте с помощью сериализатора для
  связанной модели.

#### Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

### Задание 4

* Настройте фильтрацию для эндпоинтов вывода списка платежей с возможностями:
    - менять порядок сортировки по дате оплаты,
    - фильтровать по курсу или уроку,
    - фильтровать по способу оплаты.