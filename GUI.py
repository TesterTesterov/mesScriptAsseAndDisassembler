import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from SilkyMes import SilkyMes

class GUI:
    def __init__(self):
        self.__window = tk.Tk()
        self.__language = 'eng'
        self.__setWindowTitle()
        self.__width = 400
        self.__height = 500
        self.__window.geometry('{}x{}+{}+{}'.format(
            self.__width,
            self.__height,
            self.__window.winfo_screenwidth()//2-self.__width//2,
            self.__window.winfo_screenheight()//2-self.__height//2))
        self.__window.resizable(width=False, height=False)

        self.__btn_rus = tk.Button(master=self.__window,
                                   text="Русский",
                                   command=self.__toRus,
                                   font=('Helvetica', 15),
                                   bg='white')
        self.__btn_eng = tk.Button(master=self.__window,
                                   text="English",
                                   command=self.__toEng,
                                   font=('Helvetica', 15),
                                   bg='white')
        self.__btn_rus.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=0.1)
        self.__btn_eng.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=0.1)
        self.__lbl_MesPoint = tk.Label(master=self.__window,
                                       bg='white',
                                       text='Enter a title of the .mes file:',
                                       font=('Helvetica', 12))
        self.__mesFile = tk.StringVar()
        self.__ent_MesName = tk.Entry(master=self.__window,
                                      bg='white',
                                      textvariable=self.__mesFile)
        self.__btn_MesFind = tk.Button(master=self.__window,
                                   text="???",
                                   command=self.__FindMes,
                                   font=('Helvetica', 12),
                                   bg='white')
        self.__lbl_TxtPoint = tk.Label(master=self.__window,
                                       bg='white',
                                       text='Enter a title of the .txt file:',
                                       font=('Helvetica', 12))
        self.__txtFile = tk.StringVar()
        self.__ent_TxtName = tk.Entry(master=self.__window,
                                      bg='white',
                                      textvariable=self.__txtFile)
        self.__btn_TxtFind = tk.Button(master=self.__window,
                                   text="???",
                                   command=self.__FindTxt,
                                   font=('Helvetica', 12),
                                   bg='white')
        self.__lbl_MesPoint.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.05)
        self.__ent_MesName.place(relx=0.0, rely=0.15, relwidth=0.9, relheight=0.05)
        self.__btn_MesFind.place(relx=0.9, rely=0.15, relwidth=0.1, relheight=0.05)
        self.__lbl_TxtPoint.place(relx=0.0, rely=0.2, relwidth=1.0, relheight=0.05)
        self.__ent_TxtName.place(relx=0.0, rely=0.25, relwidth=0.9, relheight=0.05)
        self.__btn_TxtFind.place(relx=0.9, rely=0.25, relwidth=0.1, relheight=0.05)

        self.__lblfr_Commands = tk.LabelFrame(master=self.__window,
                                              text="Commands:",
                                              font=('Helvetica', 14),
                                              bg='white',
                                              relief=tk.RAISED)
        self.__lblfr_Status = tk.LabelFrame(master=self.__window,
                                              text="Status:",
                                              font=('Helvetica', 14),
                                              bg='white',
                                              relief=tk.RAISED)
        self.__lblfr_Help = tk.LabelFrame(master=self.__window,
                                              text="Help:",
                                              font=('Helvetica', 14),
                                              bg='white',
                                              relief=tk.RAISED)
        self.__lblfr_Commands.place(relx=0.0, rely=0.3, relwidth=1.0, relheight=0.2)
        self.__lblfr_Status.place(relx=0.0, rely=0.5, relwidth=1.0, relheight=0.2)
        self.__lblfr_Help.place(relx=0.0, rely=0.7, relwidth=1.0, relheight=0.3)

        self.__btm_commonHelp = tk.Button(master=self.__lblfr_Help,
                                   text="Common help",
                                   command=self.__commonHelp,
                                   font=('Helvetica', 12),
                                   bg='white')
        self.__btm_usageHelp = tk.Button(master=self.__lblfr_Help,
                                   text="Usage help",
                                   command=self.__usageHelp,
                                   font=('Helvetica', 12),
                                   bg='white')
        self.__btm_breaksHelp = tk.Button(master=self.__lblfr_Help,
                                   text="Line/message breaks help",
                                   command=self.__breaksHelp,
                                   font=('Helvetica', 12),
                                   bg='white')
        self.__txt_StatusArea = tk.Text(master=self.__lblfr_Status,
                                        font=('Helvetica', 14),
                                        bg='white',
                                        relief=tk.SUNKEN,
                                        state=tk.DISABLED)
        self.__txt_StatusArea.pack()

        self.__btm_commonHelp.pack(fill=tk.X)
        self.__btm_usageHelp.pack(fill=tk.X)
        self.__btm_breaksHelp.pack(fill=tk.X)
        self.__btn_disasse = tk.Button(master=self.__lblfr_Commands,
                  text="Disasseble script",
                  command=self.__dissScript,
                  font=('Helvetica', 12),
                  bg='white')
        self.__btn_asse = tk.Button(master=self.__lblfr_Commands,
                  text="Assemble script",
                  command=self.__asseScript,
                  font=('Helvetica', 12),
                  bg='white')
        self.__btn_disasse.pack(fill=tk.X)
        self.__btn_asse.pack(fill=tk.X)

        self.__window.mainloop()

    def __FindMes(self):
        ftypes = []
        if (self.__language == 'eng'):
            ftypes = [('Silky Engine scripts', '*.mes'), ('All files', '*')]
        elif (self.__language == 'rus'):
            ftypes = [('Скрипты Silky Engine', '*.mes'), ('Все файлы', '*')]
        dialg = filedialog.Open(self.__window, filetypes=ftypes, initialdir=os.getcwd())
        file = dialg.show()
        self.__mesFile.set(file)
    def __FindTxt(self):
        ftypes = []
        if (self.__language == 'eng'):
            ftypes = [('Text files', '*.txt'), ('All files', '*')]
        elif (self.__language == 'rus'):
            ftypes = [('Текстовые файлы', '*.txt'), ('Все файлы', '*')]
        dialg = filedialog.Open(self.__window, filetypes=ftypes, initialdir=os.getcwd())
        file = dialg.show()
        self.__txtFile.set(file)
    def __toRus(self):
        self.__language = 'rus'
        self.__setWindowTitle()
        self.__lbl_MesPoint["text"] = "Введите название файла .mes:"
        self.__lbl_TxtPoint["text"] = "Введите название файла .txt:"
        self.__lblfr_Commands["text"] = "Команды:"
        self.__lblfr_Status["text"] = "Статус:"
        self.__lblfr_Help["text"] = "Помощь:"
        self.__btn_disasse["text"] = "Разобрать скрипт"
        self.__btn_asse["text"] = "Собрать скрипт"
        self.__txt_StatusArea["state"] = tk.NORMAL
        text = self.__txt_StatusArea.get(1.0, tk.END).rstrip('\n')
        self.__txt_StatusArea.delete(1.0, tk.END)
        if (text == 'Assembling succeed.'):
            self.__txt_StatusArea.insert(1.0, "Сборка удалось.")
        elif (text == 'Disassembling succeed.'):
            self.__txt_StatusArea.insert(1.0, "Разборка удалась.")
        elif (text == 'Assembling failed.'):
            self.__txt_StatusArea.insert(1.0, "Сборка не удалась.")
        elif (text == 'Disassembling failed.'):
            self.__txt_StatusArea.insert(1.0, "Разборка не удалась.")
        self.__txt_StatusArea["state"] = tk.DISABLED
        self.__btm_commonHelp["text"] = "Общая помощь"
        self.__btm_usageHelp["text"] = "Помощь по использованию"
        self.__btm_breaksHelp["text"] = "Помощь по переносам (по строкам/сообщениям)"
    def __toEng(self):
        self.__language = 'eng'
        self.__setWindowTitle()
        self.__lbl_MesPoint["text"] = "Enter a title of the .mes file:"
        self.__lbl_TxtPoint["text"] = "Enter a title of the .txt file:"
        self.__lblfr_Commands["text"] = "Commands:"
        self.__lblfr_Status["text"] = "Status:"
        self.__lblfr_Help["text"] = "Help:"
        self.__btn_disasse["text"] = "Disasseble script"
        self.__btn_asse["text"] = "Assemble script"
        self.__txt_StatusArea["state"] = tk.NORMAL
        text = self.__txt_StatusArea.get(1.0, tk.END).rstrip('\n')
        self.__txt_StatusArea.delete(1.0, tk.END)
        if (text == 'Сборка удалось.'):
            self.__txt_StatusArea.insert(1.0, "Assembling succeed.")
        elif (text == 'Разборка удалась.'):
            self.__txt_StatusArea.insert(1.0, "Disassembling succeed.")
        elif (text == 'Сборка не удалась.'):
            self.__txt_StatusArea.insert(1.0, "Assembling failed.")
        elif (text == 'Разборка не удалась.'):
            self.__txt_StatusArea.insert(1.0, "Disassembling failed.")
        self.__txt_StatusArea["state"] = tk.DISABLED
        self.__btm_commonHelp["text"] = "Common help"
        self.__btm_usageHelp["text"] = "Usage help"
        self.__btm_breaksHelp["text"] = "Line/message breaks help"
    def __setWindowTitle(self):
        if (self.__language == 'eng'):
            self.__window.title("mesScriptAsseAndDisassembler by Tester")
        elif (self.__language == 'rus'):
            self.__window.title("mesScriptAsseAndDisassembler от Tester-а")

    def __dissScript(self):
        mesFile = ''
        txtFile = ''
        status = True
        mesFile, txtFile, status = self.__getMesAndTxt()
        if (not (status)):
            return False
        ScriptMes = SilkyMes(mesFile, txtFile)
        try:
            ScriptMes.dissasemble()
            self.__txt_StatusArea["state"] = tk.NORMAL
            self.__txt_StatusArea.delete(1.0, tk.END)
            if (self.__language == 'eng'):
                self.__txt_StatusArea.insert(1.0, "Disassembling succeed.")
            elif (self.__language == 'rus'):
                self.__txt_StatusArea.insert(1.0, "Разборка удалась.")
            self.__txt_StatusArea["state"] = tk.DISABLED
        except:
            self.__txt_StatusArea["state"] = tk.NORMAL
            self.__txt_StatusArea.delete(1.0, tk.END)
            if (self.__language == 'eng'):
                self.__txt_StatusArea.insert(1.0, "Disassembling failed.")
            elif (self.__language == 'rus'):
                self.__txt_StatusArea.insert(1.0, "Разборка не удалась.")
            self.__txt_StatusArea["state"] = tk.DISABLED
        del ScriptMes
        return True

    def __asseScript(self):
        mesFile = ''
        txtFile = ''
        status = True
        mesFile, txtFile, status = self.__getMesAndTxt()
        if (not (status)):
            return False
        ScriptMes = SilkyMes(mesFile, txtFile)
        try:
            ScriptMes.assemble()
            self.__txt_StatusArea["state"] = tk.NORMAL
            self.__txt_StatusArea.delete(1.0, tk.END)
            if (self.__language == 'eng'):
                self.__txt_StatusArea.insert(1.0, "Assembling succeed.")
            elif (self.__language == 'rus'):
                self.__txt_StatusArea.insert(1.0, "Сборка удалось.")
            self.__txt_StatusArea["state"] = tk.DISABLED
        except:
            self.__txt_StatusArea["state"] = tk.NORMAL
            self.__txt_StatusArea.delete(1.0, tk.END)
            if (self.__language == 'eng'):
                self.__txt_StatusArea.insert(1.0, "Assembling failed.")
            elif (self.__language == 'rus'):
                self.__txt_StatusArea.insert(1.0, "Сборка не удалась.")
            self.__txt_StatusArea["state"] = tk.DISABLED
        del ScriptMes
        return True

    def __getMesAndTxt(self):
        status = True
        mesFile = self.__ent_MesName.get()
        if (mesFile == ''):
            status = False
            if (self.__language == 'eng'):
                tk.messagebox.showerror("Error",
                                    "Error!\n.mes file title wasn't given!")
            elif (self.__language == 'rus'):
                tk.messagebox.showerror("Ошибка",
                                    "Ошибка!\nНазвание файла .mes не введено!")
        txtFile = self.__ent_TxtName.get()
        if (txtFile == ''):
            status = False
            if (self.__language == 'eng'):
                tk.messagebox.showerror("Error",
                                    "Error!\n.txt file title wasn't given!")
            elif (self.__language == 'rus'):
                tk.messagebox.showerror("Ошибка",
                                    "Ошибка!\nНазвание файла .txt не введено!")
        return mesFile, txtFile, status

    def __commonHelp(self):
        if (self.__language == 'eng'):
            tk.messagebox.showinfo("Common help", ''' Dual languaged (rus+eng) tool for disassembling and assembling scripts .me sfrom the visual novel's engine Silky Engine (also known as Silky's Engine or SilkyEngine). With it thou can fully edit code, not just strings, as with some earlier tools. Thou can add line or even message breaks without restrictions!\n\n It has some useful features.\nFirstly, during disassembling all opcodes '\x0A' changes to '\x0B', so the engine wouldn't try to decrypt new strings and break latin and half-width kana symbols.\nSecondly, thou can make comments in txt file with "\u0024" at the beginning of the string.\nThirdly, some definations: "#0-" are "free bytes", "#1-" are commands (and "[...]" are arguments below) and "#2-" are labels.\n\nDeveloped by Tester: https://anivisual.net/index/8-78951.''')
        elif (self.__language == 'rus'):
            tk.messagebox.showinfo("Общая помощь", ''' Двуязычное (рус+англ) средство для разборки и сборки скриптов .mes движка визуальных новелл Silky Engine, также как Silky's Engine и SilkyEngine. С ним вы можете полностью редактирвоать код, а не только строки, как с ранее существовшими средствами. Вы можете добавлять разрывы текста по строкам и даже сообщениям без ограничений!\n\n В нём есть несколько полезных особенностей.Во-первых, во время дизассемблирования все опкоды '\x0A' меняются на '\x0B', дабы движок не пытался дешифровать новые строки и не ломал при том латиницу и полуширинные символы.\nВо-вторых, можно делать комментарии, при этом в начало строки необходимо ставить "\u0024".\nВ-третьих, опишем некоторые определения: "#0-" есть "вольные байты", "#1-" есть команды (и под ними "[...]" аргументы) и "#2-" есть метки.\n\nРазработано Tester-ом: https://anivisual.net/index/8-78951.''')
    def __usageHelp(self):
        if (self.__language == 'eng'):
            tk.messagebox.showinfo("Usage help", '''1. Enter a title of the .mes file in the top entry (do see, with extension). Thou can also enter relative or absolute path.\n2. Enter a title of the .txt file (do see, with extension). Thou can also enter relative or absolute path.\n3. For dissassemble push the button "Disassemble script".\n4. For assemble push the button "Assemble script".\n5. Status will be displayed on the text area below.''')
        elif (self.__language == 'rus'):
            tk.messagebox.showinfo("Помощь по использованию", '''1. Введите название файла .mes в верхней форме (заметьте, с исключением). Также можно вводить относительный или абсолютный до него путь.\n2. Введите название файла .txt в нижней форме (заметьте, с исключением). Также можно вводить относительный или абсолютный до него путь.\n3. Для разборки нажмите на кнопку "Разобрать скрипт".\n4. Для сборки нажмите на кнопку "Собрать скрипт".\n5. Статус сих операций будет отображаться на текстовом поле ниже.''')
    def __breaksHelp(self):
        if (self.__language == 'eng'):
            tk.messagebox.showinfo("Break help", '''Sometimes there could be a very big problem: text may not fully get in textbox. But with this tool thou don't need to cut some part of text, no. Thou can use line and message breaks. Methods are below.\n\n- For line breaks insert this below the current message ('SomeString' -> text on the new line):\n#1-TO_NEW_STRING\n[0]\n#1-STR_UNCRYPT\n['SomeString']\n\n- For message breaks insert this below the current message ('SomeString' -> text on the new message):\n#1-32\n[0, 3]\n#1-32\n[0, 22]\n#1-NVL?\n[]\n#1-32\n[0, 0]\n#1-32\n[0, 3]\n#1-17\n[]\n#1-MESSAGE\n[0]\n#1-STR_UNCRYPT\n['SomeString']''')
        elif (self.__language == 'rus'):
            tk.messagebox.showinfo("Помощь по переносам", '''Иногда можно столкнуться с одной большой-пребольшой проблемой: текст может не полностью влезать в текстовое окно. Однако, с сим средством вам не нужно обрезать его, отнюдь. Вы можеет организовывать переносы по строкам и сообщениям. Методы указаны ниже.\n\n- Для переносов по строкам добавьте под текущее сообщение следующий код ('Какая_то_строка' -> текст на новой строке):\n#1-TO_NEW_STRING\n[0]\n#1-STR_UNCRYPT\n['SomeString']\n\n- Для переносов по сообщениям добавьте под текущее сообщение следующий код ('Какая_то_строка' -> текст на новой строке):\n#1-32\n[0, 3]\n#1-32\n[0, 22]\n#1-NVL?\n[]\n#1-32\n[0, 0]\n#1-32\n[0, 3]\n#1-17\n[]\n#1-MESSAGE\n[0]\n#1-STR_UNCRYPT\n['SomeString']''')