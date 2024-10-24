13.1 Введение в ООП

Контекст: зачем решать подобные задачи
Большая часть разработки использует ООП-подход для создания своих сервисов, а также для работы с данными, которые представляют собой сущности или объекты со своими параметрами и методами. В рамках этих домашних заданий мы проработаем использование классов и объектов на основе популярной темы e-commerce.
E-commerce — электронная торговля, или электронная коммерция. На данном этапе работы мы не будем реализовывать систему платежей, однако подготовим всё для того, чтобы у нас появилось ядро для интернет-магазина. В дальнейшем для этого ядра возможно будет реализовать любой интерфейс — от сайта до телеграм-бота.

Критерии выполнения домашнего задания
- Создали классы и описали их инициализацию со всеми свойствами.
- Объекты продуктов хранятся в соответствующем атрибуте объекта категории.
- Результат выполнения всего задания залили на GitHub и сдали в виде ссылки на репозиторий.
- Все написанные тесты выполняются без ошибок.

Пояснение к заданиям
В этом домашнем задании у вас есть две сущности: категории и продукты. У этих сущностей сразу определены поля. В задачах редко пишут, что нужно создать класс с атрибутами и методами, при этом четко описывают, какие атрибуты и каких типов должны быть. Поэтому важно внимательно рассматривать условия. Например, в классе «Категории» мы видим список товаров, значит, это должен быть список list и в нём должны содержаться продукты, которые описаны уже ниже.
Разберемся детальнее с заданиями. В первом задании вам нужно создать два класса, которые вы позже будете развивать. То есть только создать класс и описать атрибуты, которые будут принадлежать к каждому классу. При этом хорошей практикой будет являться сразу описание типов данных, которые предполагаются для значений, которые будут храниться в них. Что касается второй задачи, то в ней упор идет на отработку навыка описания инициализации в классах. Важно определить, что принимает на вход метод инициализации. А в третьем задании важно убедиться, что сделано всё верно, и протестировать функционал. Не переживайте, что можете написать слишком много тестов: лучше проверить, что всё корректно работает и заполняется.
Также важно прочитать всю задачу целиком, чтобы сразу выделить все важные для себя моменты. Обратите внимание на критерии приемки, они тоже могут сильно повлиять на само выполнение задания.

Задание 1
Создайте классы Category и Product. Для класса Category определите следующие свойства:
- название,
- описание,
- товары.
Для класса Product:
- название,
- описание,
- цена,
- количество в наличии.
Для каждого поля используйте наиболее подходящий тип данных на ваше усмотрение, но обратите внимание, что цена может быть указана с копейками, а количество лучше измерять в штуках.
#атрибуты #типы_данных #создание_класса #class

Задание 2
Для двух классов, которые были реализованы в задании 1, добавьте инициализацию так, чтобы каждый параметр был передан в инициализацию объекта и сохранен. А также для класса Category добавьте два атрибута, в которых будут храниться общее количество категорий и общее количество уникальных продуктов, не учитывая количество в наличии.
#__init__ #конструктор_класса #self

Задание 3
Напишите тесты для классов, которые проверяют:
- корректность инициализации объектов класса Category,
- корректность инициализации объектов класса Product,
- подсчет количества продуктов,
- подсчет количества категорий.
#pytest #assert #fixtures

*Дополнительное задание
Реализуйте подгрузку данных по категориям и товарам из файла JSON. Для этого опишите специальную функцию, которая будет читать файл и создавать объекты классов.
Ссылка на файл:products.json
#json #loads #load
