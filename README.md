! Файлы .py с пометкой "first" имеют стандартный ввод и вывод, как было указано в условии.

! Файлы .py с пометкой "for_tests" - изменённые "first" для проведения тестов.

Все подсчеты времени в файле .xlsx.

Логин, использованный в контесте: eaibragimova_1@edu.hse.ru

Код, использованный в контесте: tree_first.py

---
**Задача: Точка среди прямоугольников**

Даны прямоугольники на плоскости с углами в целочисленных координатах ([1..10^9],[1..10^9]).
Требуется как можно быстрее выдавать ответ на вопрос «Скольким прямоугольникам принадлежит точка (x,y)?» И подготовка данных должна занимать мало времени.
UPD: только нижние границы включены => (x1<= x) && (x<x2) && (y1<=y) && (y<y2)

---
Задача была реализована тремя разными алгоритмами:
1. **Алгоритм перебора**
- Без подготовки. При поиске – просто перебор всех прямоугольников
- Подготовка O(1), поиск O(N*m)
2. **Алгоритм на карте**
- Сжатие координат и построение карты.
- Подготовка O(N^3), поиск O(logN)
3. **Алгоритм на дереве**
- Сжатие координат и построение персистентного дерева отрезков 
- Подготовка O(NlogN), поиск O(logN)
---
После реализации были проведены тесты и подсчитано время, которое каждая из программ затрачивает на вывод ответа.

Для проведения тестов были использованы рекомендации ниже:
- Для тестового набора прямоугольников, рекомендуется использовать набор вложенных друг-в-друга прямоугольников с координатами с шагом больше 1 {(10*i, 10*i), (10*(2N-i), 10*(2N-i))}.
- Для тестового набора точек, рекомендуется использовать неслучайный набор распределенных более-менее равномерно по ненулевому пересечению прямоугольников, например хэш функции от i с разным базисом для x и y.   (p*i)^31%(20*N), p-большое простое, разное для x и y. Я взяла p1, p2 = 10007, 10009.
---
Я провела два блока тестов:
1. Я увеличивала n, оставляя m неизменным:

![image](https://github.com/future-genius16/alg_lab2/assets/154009217/d3cb2a07-7476-4152-8979-516d45d4c9c3)

2. Я увеличивала m, оставляя n неизменным:

![image](https://github.com/future-genius16/alg_lab2/assets/154009217/dec87466-2347-4fad-a6cf-e1fc0f04e25c)

---
На оснавании полученных данных, я делаю вывод:

1. Алгоритм перебора: 
- Подготовка данных: Отсутствует (O(1)).
- Поиск: Время поиска для каждой точки составляет O(N), где N - количество прямоугольников. Таким образом, поиск всех точек выполняется за О(N*m).
- Итог: Этот алгоритм хорош для небольших наборов данных (маленькое N), но становится не очень эффективным при увеличении количества прямоугольников и точек.
2. Алгоритм на карте:
- Подготовка данных: О(N^3), так как требуется сжатие координат и построение карты.
- Поиск: O(logN), благодаря использованию сжатия координат и карты.
- Итог: Хороший выбор для самых маленьких наборов данных (маленькое N), так как алгоритму требуется О(N^3) времени для сжатия координат и построения карты, что долго при больших N. Время поиска остается логарифмическим, поэтому это отличный вариант для маленьких N.
3. Алгоритм на дереве:
- Подготовка данных: О(NlogN), так как требуется сжатие координат и построение персистентного дерева отрезков.
- Поиск: O(logN), благодаря использованию персистентного дерева отрезков.
- Итог: Как видно по графикам, этому варианту нет равных, когда входные данные растут. Это хороший выбор для очень больших наборов данных (очень большое N), так как время поиска остается логарифмическим.

Вариант с алгоритмом с деревом самый эффективный, но если данные не слишком большие, и при этом нужно, чтобы было быстро и эффективно, смело можно выбирать перебор, так как не небольших данных он не уступает алгоритму с деревом.
