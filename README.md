# mesScriptAsseAndDissasembler
## On English
 Dual languaged (rus+eng) tool for disassembling and assembling scripts .mes from the visual novel's engine Silky Engine (also known as Silky's Engine or SilkyEngine). With it thou can fully edit code, not just strings, as with some earlier tools. Thou can add line or even message breaks without restrictions!
 Mes script files can be used not just in Silky Engine, but also in AI6WIN. For assembling and disassembling mes script files of AI6WIN use [AI6WINScriptTool](https://github.com/TesterTesterov/AI6WINScriptTool).
 Sometimes mes scripts may not contain strings. If this is the case, they can be found in MAP string patch files in data.arc. For them use [MAPTool](https://github.com/TesterTesterov/MAPTool).
 Sometimes you may need to work with Silky Engine .arc scripts. For it use [SilkyArcTool](https://github.com/TesterTesterov/SilkyArcTool) instead.
 
 It has some useful features.
 Firstly, during disassembling all opcodes '\x0A' changes to '\x0B', so the engine wouldn't try to decrypt new strings and break latin and half-width kana symbols.
 Secondly, thou can make comments in txt file with "$" at the beginning of the string.
 Thirdly, some definations: "#0-" are "free bytes", "#1-" are commands (and "\[...]" are arguments below), "#2-" are labels and "#3" are speacial header labels.
 
 ### Tested on
 - [Hikari no Umi no Apeiria](https://vndb.org/v20860)
 - [Hikari no Umi no Apeiria \~Casablanca no Kishi\~](https://vndb.org/v21857).
 
## На русском
 Двуязычное (рус+англ) средство для разборки и сборки скриптов .mes движка визуальных новелл Silky Engine, также известного как Silky's Engine и SilkyEngine. С ним вы можете полностью редактирвоать код, а не только строки, как с ранее существовшими средствами. Вы можете добавлять разрывы текста по строкам и даже сообщениям без ограничений!
 Скрипты с расширением "mes" используются не только в Silky Engine, но также и в AI6WIN. Чтобы дизассемблировать и ассемблировать скрипты движка AI6WIN используйте иное средство -- [AI6WINScriptTool](https://github.com/TesterTesterov/AI6WINScriptTool).
 Ежель не найти в скриптах mes строк, то оные в файлах патча строк MAP могут быть, что в data.arc лежат. Для оных используйте [MAPTool](https://github.com/TesterTesterov/MAPTool).
 Вам также может понадобиться необходимость работать с архивами .arc Silky Engine. Для этого используйте [SilkyArcTool](https://github.com/TesterTesterov/SilkyArcTool).
 
 В нём есть несколько полезных особенностей.
 Во-первых, во время дизассемблирования все опкоды '\x0A' меняются на '\x0B', дабы движок не пытался дешифровать новые строки и не ломал при том латиницу и полуширинные символы.
 Во-вторых, можно делать комментарии, при этом в начало строки необходимо ставить "$".
 В-третьих, опишем некоторые определения: "#0-" есть "вольные байты", "#1-" есть команды (и под ними "\[...]" аргументы), "#2-" есть метки и "#3" есть специальные заголовочные метки.
 
 ### Протестировано на
 - [Апейрия живописных морей](https://vndb.org/v20860)
 - [Апейрия живописных морей: Рыцари Касабланки](https://vndb.org/v21857).

# Usage / Использование
## On English
![image](https://user-images.githubusercontent.com/66121918/147385333-3d1c72bd-fe1d-48b9-afd5-419ed14286f9.png)
1. Choose the mode, file or directory. In first mode you will work with one .mes - .txt pair, in second -- with all files in a pair of directories.
2. Enter a name of the .mes file in the top entry (do see, with extension) or the directory name. Thou can also enter relative or absolute path. You can also click on "..." to choose.
3. Enter a name of the .txt file (do see, with extension) or the directory name. Thou can also enter relative or absolute path. You can also click on "..." to choose.
4. For dissassemble push the button "Disassemble script".
5. For assemble push the button "Assemble script".
6. Status will be displayed on the text area below.

## На русском
![image](https://user-images.githubusercontent.com/66121918/147385353-1df10e15-ffc0-4084-9621-9e184bb07768.png)
1. Выберите режим: файл или директорию. В первом вы будете работать с парой .mes - .txt, во втором -- со всеми файлами в паре директорий.
2. Введите название файла .mes в верхней форме (заметьте, с расширением) или имя директории. Также можно вводить относительный или абсолютный до него путь. Также вы можете нажать на кнопку "...", чтобы выбрать.
3. Введите название файла .txt в нижней форме (заметьте, с расширением) или имя директории. Также можно вводить относительный или абсолютный до него путь. Также вы можете нажать на кнопку "...", чтобы выбрать.
4. Для разборки нажмите на кнопку "Дизассемблировать скрипт".
5. Для сборки нажмите на кнопку "Ассемблировать скрипт".
6. Статус сих операций будет отображаться на текстовом поле ниже.

# Line and Message Breaks Help / Помощь по организации переносов по строкам и сообщениям.
## On English
Sometimes there could be a very big problem: text may not fully get in textbox. But with this tool thou don't need to cut some part of text, no. Thou can use line and message breaks. Methods are below.
### For line breaks insert this below the current message ('SomeString' -> text on the new line).
```
#1-TO_NEW_STRING
[0]
#1-STR_UNCRYPT
["SomeString"]
```
### For message breaks insert this below the current message ('SomeString' -> text on the new message).
```
#1-32
[0, 3]
#1-32
[0, 22]
#1-24
[]
#1-32
[0, 0]
#1-32
[0, 3]
#1-17
[]
#1-MESSAGE
[0]
#1-STR_UNCRYPT
["SomeString"]
```

## На русском
Иногда можно столкнуться с одной большой-пребольшой проблемой: текст может не полностью влезать в текстовое окно. Однако, с сим средством вам не нужно обрезать его, отнюдь. Вы можеет организовывать переносы по строкам и сообщениям. Методы указаны ниже.
### Для переносов по строкам добавьте под текущее сообщение следующий код ('Какая_то_строка' -> текст на новой строке).
```
#1-TO_NEW_STRING
[0]
#1-STR_UNCRYPT
["Какая_то_строка"]
```
### Для переносов по сообщениям добавьте под текущее сообщение следующий код ('Какая_то_строка' -> текст на новой строке).
```
#1-32
[0, 3]
#1-32
[0, 22]
#1-24
[]
#1-32
[0, 0]
#1-32
[0, 3]
#1-17
[]
#1-MESSAGE
[0]
#1-STR_UNCRYPT
["Какая_то_строка"]
```
