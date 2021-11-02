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



