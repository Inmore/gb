# Итоговая проверочная работа
 
## Как использовать функцию FilterArray()
 
1. Выполните команду
 
```
dotnet run
```
 
2. Введите в консоль желаемое количество элементов массива со строками
 
3. Введите поочередно элементы массива
 
4. Функция вернет массив со строками из введенного в п.3 массива, длина которых не превышает 3.
 
## Реализация
 
1. Получаем посредством ввода с консоли количество элементов массива.
 
2. Заполняем массив значениями с консоли
 
3. Подсчитываем количество элементов в этом массиве и сохраняем его в переменную count.
 
4. Создаем новый массив, число элементов в котором берем из переменной count.
 
5. Проходим по элементам изначального массива. Значения элементов, длина которых не больше 3, присваиваем элементам нового массива.
 
6. Возвращаем новый массив.