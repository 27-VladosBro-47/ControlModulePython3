# ControleModulePython3

## Project
![alt-текст](https://github.com/27-VladosBro-47/ControlModulePython3/blob/main/for_md/main.jpg "Project")

<p align="center">
  <img src="https://github.com/27-VladosBro-47/ControlModulePython3/blob/main/for_md/review.gif" alt="Project"/>
</p>

## YouTube Videos review
[===== Video 1 =====](https://www.youtube.com/watch?v=ITavp3Tw1Gk)<br/>
[===== Video 2 =====](https://www.youtube.com/watch?v=g3qcdG-vaeE)

## Description
Модуль, створений на основі міні ЕОМ RaspberryPi 3B+ та мікроконтролера Arduino, який здійснює розпізнавання жестів оператора та приведення до руху шасі.
Програмне забезпечення написане на основі мови програмування Python 3 з використанням бібліотеки OpenCV та фраємворку MediaPipe, що забезпечує розпізнавання кисті руки. Також на Python 3 була написана та навчена на власно створених навчальних данних нейромереже, яка базується на алгоритмі зворотного поширення помилки (Перцептрон Розенблата) 

Пристрій складається з Raspberry Pi 3B+, Arduino Nano, камери Raspberry Pi 8 Mpx ver. 1.3, альт-азимутальної установки, колесного шасі, драйвера двигунів L298N, модуль живлення для макетної плати 5В /3.3В, сервоприводи sg90, елементи живлення.

Система розпізнає 5 унікальних жестів, з яких 4 використовуються для керування, п'ятий жест наразі не використовується.

![alt-текст](https://github.com/27-VladosBro-47/ControlModulePython3/blob/main/for_md/gestures.png "Gestures")

Система розпізнає наступні жести:
* Жест 0 - поворот ліворуч
* Жест 1 - рух прямо
* Жест 2 - поворот праворуч
* Жест 3 - рух назад
* Жест 4 - наразі, ніяких дій не задано

Для реалізації процесу навчання нейромережі було власноруч створенно понад 7500 навчальних даних шляхом фотофіксації кисті руки автора.

Запуск програми відбувається із термінала, виконанням команди **python3 source.py** із теки проекта.
![alt-текст](https://github.com/27-VladosBro-47/ControlModulePython3/blob/main/for_md/terminal_def.png "Terminal")
Також програма підтримує ще декілька режимів роботи, які активуються шляхом додавання параметра після назви скрипта (написання дозволено у довільному регістрі).
#### make_data
![alt-текст](https://github.com/27-VladosBro-47/ControlModulePython3/blob/main/for_md/terminal_make_data.png "Terminal")
Прогорама запускається і починає пошук кисті руки.
Після захоплення кисті руки
![alt-текст](https://github.com/27-VladosBro-47/ControlModulePython3/blob/main/for_md/exemple.png "Gesture")
необхідно натиснути клавішу 0,1,2,3 або 4, залежно від жесту і у папці data/test_training_data буде створений файл з навчальними даними (якщо його там не було) training_data_N.json, де N - номер жесту 0-4 (якщо його там не було). Необхідно створити всі 5 файлів із даними і, після того, як була створенна необхідна кількість даних, необхідно файли training_data_N.json перемістити у папку data/training_data перед початком навчання **python3 source.py make_data**
#### learning
![alt-текст](https://github.com/27-VladosBro-47/ControlModulePython3/blob/main/for_md/learning.png "Terminal")
Команда запускає програму і розпочинає процес навчання нейромережі. У папці data/test_neural_network_configurations буде створений файл конфігурацій configurations.json на основі якого буде створенна нейромережа у режимі "learning". Для цього файл configurations.json необхідно перемістити з папки data/test_neural_network_configurations у папку data/neural_network_configurations перед запуском режиму "learning".
#### tracking
![alt-текст](https://github.com/27-VladosBro-47/ControlModulePython3/blob/main/for_md/terminal_def_1.png "Terminal")
Команда запускає програму у звичайному режимі, якби була виконана команда **python3 source.py**


