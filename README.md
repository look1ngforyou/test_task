Привет читающему:)

Так как ТЗ было неполным, я руководствовался здравым смыслом и опытом для реализации простенькой тестовой среды, например реализаовал "вход" UUID у GET запроса через его передачу в URL 
(в ТЗ про способ передачи ничего не написано). Также не было указано тестируем ли мы в рамках задания только модели или поверх них ещё raw responses. Я реализовал эти два подхода. 
Очень подробно описал работу приложения и тестов уже в самом коде через docstring. Постарался максимально прояснить каждый момент.


Использованные библиотеки/фреймворки указаны в файле requirements.txt , дублирую их здесь:

curlify - для логирования

Faker - для тестовых данных, в нашем случае UUID

pydantic - для валидации и отправки JSON моделей

pytest - для проведения тестов

Requests - для HTTP запросов
