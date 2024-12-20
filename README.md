Вариант №24<br/>
Задание №4<br/>
Разработать ассемблер и интерпретатор для учебной виртуальной машины
(УВМ). Система команд УВМ представлена далее.
Для ассемблера необходимо разработать читаемое представление команд
УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к
которой задается из командной строки. Результатом работы ассемблера является
бинарный файл в виде последовательности байт, путь к которому задается из
командной строки. Дополнительный ключ командной строки задает путь к файлулогу, в котором хранятся ассемблированные инструкции в духе списков
“ключ=значение”, как в приведенных далее тестах.
Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ
и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон
также указывается из командной строки.
Форматом для файла-лога и файла-результата является csv.
Необходимо реализовать приведенные тесты для всех команд, а также
написать и отладить тестовую программу
![image](https://github.com/user-attachments/assets/bf6ce0e6-45d0-4c37-8395-c279f485f78f)</br>
![image](https://github.com/user-attachments/assets/4a83a6a9-a00f-42dc-9fb6-8b90f5ccff14)</br>
![image](https://github.com/user-attachments/assets/b5ce24fa-798a-4c5c-9d5e-75ef7e7df1be)</br>
![image](https://github.com/user-attachments/assets/a63044e8-d9bb-43e7-8598-c056b4b4b37c)</br>
 ОПИСАНИЕ ФУНКЦИЙ </br>
 1. assemble(input_file, binary_output, log_output)<br/>
Назначение: Преобразует текстовый файл с ассемблерным кодом в бинарный формат и создает лог в формате CSV для отслеживания процесса.<br/>
Параметры:input_file (str): Путь к файлу с текстовым кодом.<br/>
binary_output (str): Путь для сохранения выходного бинарного файла.</br>
log_output (str): Путь для сохранения лога преобразования в формате CSV.</br>
Возвращает: Ничего не возвращает. Создает бинарный файл и CSV-лог.<br/>

 2. interpret(binary_file, memory_range, result_file)<br/>
Назначение: Интерпретирует бинарный код, выполняет инструкции, изменяет состояние памяти и сохраняет диапазон памяти в файл CSV.<br/>
Параметры:binary_file (str): Путь к бинарному файлу с машинным кодом.<br/>
memory_range (tuple): Кортеж из двух чисел (start, end), задающий диапазон адресов памяти для сохранения.</br>
result_file (str): Путь для сохранения памяти в формате CSV.</br>
Возвращает: Ничего не возвращает. Выполняет инструкции и сохраняет результат в файл.<br/>

НАСТРОЙКИ<br/>
program.asm </br>
LOAD_CONST 156</br>
LOAD_CONST 0</br>
STORE_MEM 0</br>
LOAD_CONST 1</br>
LOAD_MEM 0</br>
MUL</br>
LOAD_CONST 0</br>
STORE_MEM 1</br>
LOAD_CONST 2</br>
LOAD_MEM 0</br>
MUL</br>
LOAD_CONST 1</br>
STORE_MEM 2</br>
LOAD_CONST 3</br>
LOAD_MEM 0</br>
MUL</br>
LOAD_CONST 2</br>
STORE_MEM 3</br>
LOAD_CONST 4</br>
LOAD_MEM 0</br>
MUL</br>
LOAD_CONST 3</br>
STORE_MEM 4</br>
LOAD_CONST 5</br>
LOAD_MEM 0</br>
MUL</br>
LOAD_CONST 4</br>
STORE_MEM 5</br>
LOAD_CONST 6</br>
LOAD_MEM 0</br>
MUL</br>
LOAD_CONST 5</br>
STORE_MEM 6</br>
LOAD_CONST 7</br>
LOAD_MEM 0</br>
MUL</br>
LOAD_CONST 6</br>
STORE_MEM 7</br>

ТЕСТЫ </br>
![image](https://github.com/user-attachments/assets/f894cfb7-aefd-4f36-a64c-4ae8cc353413)</br>
![image](https://github.com/user-attachments/assets/3cf81dce-f3ec-46db-8c01-0da42868056a)</br>
![image](https://github.com/user-attachments/assets/d7dc95ce-303e-40df-b3d0-5876f7824dd2)</br>
![image](https://github.com/user-attachments/assets/ed78ea1f-8c9b-49f7-9829-b33f3fccc26b)</br>
![image](https://github.com/user-attachments/assets/826ef4e4-2374-4427-8e8f-281a170ac567)</br>
![image](https://github.com/user-attachments/assets/1b0eae54-a8df-4e98-9ec6-e084f9d7aecc)</br>




