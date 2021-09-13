import struct
import os

class SilkyMes:
    #[Opcode, struct, name, isInSea], modifier].
    CommandLibrary = [
        [0x00, '', 'NULL', []],
        [0x02, '', '', []],
        [0x0A, 'S', 'STR_CRYPT', ['']],
        [0x0B, 'S', 'STR_UNCRYPT', ['']],
        [0x10, 'B', '', ['']],
        [0x14, 'I', 'JUMP', ['>']],
        [0x15, 'I', 'MSG_OFSETTER',['>']],
        [0x18, '', 'NVL?', []],
        [0x19, 'I', 'MESSAGE', ['>']],
        [0x1C, 'B', 'TO_NEW_STRING', ['']],
        [0x33, 'S', 'STR_RAW', ['']],
        [0x3A, '', '', []],
        [0x04, '', '', []],
        [0x05, '', '', []],
        [0x0C, '', '', []],
        [0x0D, '', '', []],
        [0x0E, '', '', []],
        [0x0F, '', '', []],
        [0x17, '', '', []],
        [0x32, 'HH', '', ['>', '>']],
        [0x34, '', '', []],
        [0x36, 'B', '', ['']],
        [0x3C, '', '', []],
        [0x42, '', '', []],
        [0x43, '', '', []]
    ]
    OffsetsLibrary = [
        [0x14, 0],
        [0x15, 0]
    ]

    def __init__(self, mesname : str, txtname : str):
        self.__mesName = mesname
        try:
            filer = open(mesname, 'rb')
            self.__mesBytes = filer.read()
            filer.close()
        except:
            self.__mesBytes = b''
        self.__txtname = txtname
        self.__prm = [0, 0]
        self.__offsets = []
        self.__strings = []
        self.__commands = []
        self.__args = []

    def dissasemble(self):
        self.__prm, self.__offsets = self.__dissHeaderPlus()
        print(self.__prm)
        print(self.__offsets)
        self.__strings, self.__commands, self.__args = self.__dissCommands()
    def assemble(self):
        inFile = open(self.__txtname, 'r', encoding='shift-jis')
        try:
            os.rename(self.__mesName, self.__mesName + '.bak')
        except:
            pass
        outFile = open(self.__mesName, 'wb')
        firstSection = b''
        secondSection = b''
        offsets = []
        offsetsCount = 0
        messageCount = 0

        #Первый заход: подсчёт смещений и запись заголовка.
        line = inFile.readline()
        pointer = 0
        while (line != ''):
            if ((line == '\n') or (line[0] == '$')):
                line = inFile.readline()
                continue
            if (line[1] == '0'):
                pointer += len(line[2:-1].split(' '))
            elif (line[1] == '1'):
                comString = line[3:-1]
                comIndex = -1
                for i in range(len(self.CommandLibrary)):
                    if (comString == self.CommandLibrary[i][2]):
                        comIndex = i
                        break
                if (comIndex == -1):
                    comString = int(comString, 16)
                    for i in range(len(self.CommandLibrary)):
                        if (comString == self.CommandLibrary[i][0]):
                            comIndex = i
                            break
                if (comIndex == -1):
                    raise Exception(comString)
                if (self.CommandLibrary[comIndex][0] == 0x19):
                    messageCount += 1
                    secondSection += struct.pack('I', pointer)
                pointer += 1
                line = inFile.readline()
                commands = line[1:-2].split(', ')
                for i in range(len(self.CommandLibrary[comIndex][1])):
                    currentPart = self.CommandLibrary[comIndex][1][i]
                    if ((currentPart == 'I') or (currentPart == 'i')):
                        pointer += 4
                    elif ((currentPart == 'h') or (currentPart == 'H')):
                        pointer += 2
                    elif ((currentPart == 'b') or (currentPart == 'B')):
                        pointer += 1
                    elif (currentPart == 'S'):
                        pointer += len(commands[i][1:-1].encode('shift-jis'))
                        pointer += 1

            elif (line[1] == '2'):
                offNum = int(line[3:-1])
                offsets.append([])
                offsets[offsetsCount].append(offNum)
                offsets[offsetsCount].append(pointer)
                offsetsCount += 1
            line = inFile.readline()
        inFile.close()

        firstSection = struct.pack('I', messageCount)
        firstSection += struct.pack('I', 0)
        outFile = open(self.__mesName, 'wb')
        outFile.write(firstSection)
        outFile.write(secondSection)

        #Второй заход: запись основной секции.
        pointer = 0
        inFile = open(self.__txtname, 'r', encoding='shift-jis')
        messageCount = 0
        line = inFile.readline()

        while (line != ''):
            if ((line == '\n') or (line[0] == '$')):
                line = inFile.readline()
                continue
            if (line[1] == '0'):
                pointer += len(line[2:-1].split(' '))
                outFile.write(bytes.fromhex(line[2:-1]))
            elif (line[1] == '1'):
                comString = line[3:-1]
                comIndex = -1
                for i in range(len(self.CommandLibrary)):
                    if (comString == self.CommandLibrary[i][2]):
                        comIndex = i
                        break
                if (comIndex == -1):
                    comString = int(comString, 16)
                    for i in range(len(self.CommandLibrary)):
                        if (comString == self.CommandLibrary[i][0]):
                            comIndex = i
                            break
                if (comIndex == -1):
                    raise Exception(comString)
                pointer += 1
                outFile.write(struct.pack('B', self.CommandLibrary[comIndex][0]))
                line = inFile.readline()
                commands = line[1:-2].split(', ')
                args = b''
                for i in range(len(self.CommandLibrary[comIndex][1])):
                    currentPart = self.CommandLibrary[comIndex][1][i]
                    if ((currentPart == 'I') or (currentPart == 'i')):
                        znach = int(commands[i]) #!!!
                        if (self.CommandLibrary[comIndex][0] == 0x19):
                            znach = messageCount
                            messageCount += 1
                        else:
                            ofsetter = False
                            for j in range(len(self.OffsetsLibrary)):
                                if (self.CommandLibrary[comIndex][0] == self.OffsetsLibrary[j][0]):
                                    ofsetter = True
                                    break
                            if (ofsetter):
                                for k in range(len(offsets)):
                                    if (int(commands[i]) == offsets[k][0]):
                                        znach = offsets[k][1]
                                        break
                            else:
                                znach = int(commands[i])
                        args += struct.pack(self.CommandLibrary[comIndex][3][i] + currentPart, znach)
                        pointer += 4
                    elif ((currentPart == 'h') or (currentPart == 'H')):
                        znach = int(commands[i])
                        args += struct.pack(self.CommandLibrary[comIndex][3][i] + currentPart, znach)
                        pointer += 2
                    elif ((currentPart == 'b') or (currentPart == 'B')):
                        znach = int(commands[i])
                        args += struct.pack(self.CommandLibrary[comIndex][3][i] + currentPart, znach)
                        pointer += 1
                    elif (currentPart == 'S'):
                        pointer += len(commands[i][1:-1].encode('shift-jis'))
                        args += commands[i][1:-1].encode('shift-jis')
                        pointer += 1
                        args += b'\x00'
                outFile.write(args)
            line = inFile.readline()
        inFile.close()
        outFile.close()

    def __dissCommands(self):
        outFile = open(self.__txtname, 'w', encoding='shift-jis')
        self.__offsets = []
        self.__args = []
        self.__commands = []

        strings = []
        commands = []
        args = []
        # [Opcode, struct, name, isInSea].
        pointer = self.__prm[0]*4 + 8
        nointer = pointer
        strer = ''
        zlo = -1

        while (nointer < len(self.__mesBytes)):
            currentByte = self.__mesBytes[nointer]
            analyzer = str(hex(currentByte))[2:]
            if (len(analyzer) == 1):
                analyzer = '0' + analyzer
            libIndex = -1
            for i in range(len(self.CommandLibrary)):
                if (currentByte == self.CommandLibrary[i][0]):
                    libIndex = i
            if (libIndex != -1):
                nointer += 1
                angron = []
                for j in range(len(self.CommandLibrary[libIndex][1])):
                    currentCom = self.CommandLibrary[libIndex][1][j]
                    if ((currentCom == 'I') or (currentCom == 'i')):
                        owBytes = self.__mesBytes[nointer:nointer+4]
                        angron.append(struct.unpack(self.CommandLibrary[libIndex][3][j] + currentCom, owBytes)[0])
                        nointer += 4
                    elif ((currentCom == 'h') or (currentCom == 'H')):
                        owBytes = self.__mesBytes[nointer:nointer+2]
                        angron.append(struct.unpack(self.CommandLibrary[libIndex][3][j] + currentCom, owBytes)[0])
                        nointer += 2
                    elif ((currentCom == 'b') or (currentCom == 'B')):
                        owBytes = self.__mesBytes[nointer:nointer+1]
                        angron.append(struct.unpack(self.CommandLibrary[libIndex][3][j] + currentCom, owBytes)[0])
                        nointer += 1
                    elif (currentCom == 'S'):
                        mode = currentByte
                        leng, result = self.__getString(mode, nointer)
                        nointer += leng
                        nointer += 1
                whatIndex = 0
                while (whatIndex < len(self.OffsetsLibrary)):
                    if (currentByte == self.OffsetsLibrary[whatIndex][0]):
                        break
                    whatIndex += 1
                if (whatIndex < len(self.OffsetsLibrary)):
                    notHere = True
                    wellOffset = angron[self.OffsetsLibrary[whatIndex][1]] + (self.__prm[0]*4 + 8)
                    for i in range(len(self.__offsets)):
                        if (wellOffset == self.__offsets[i]):
                            notHere = False
                    if (notHere):
                        self.__offsets.append(wellOffset)
            else:
                nointer += 1
        print(len(self.__offsets))
        while (pointer < len(self.__mesBytes)):
            for i in range(len(self.__offsets)):
                if (pointer == self.__offsets[i]):
                    #outFile.write("#2-" + str(i) + " " + str(pointer) + "\n")
                    outFile.write("#2-" + str(i) + "\n")
                    break
            currentByte = self.__mesBytes[pointer]
            zlo += 1
            args.append([])
            commands.append(currentByte)
            analyzer = str(hex(currentByte))[2:]
            if (len(analyzer) == 1):
                analyzer = '0' + analyzer
            libIndex = -1
            for i in range(len(self.CommandLibrary)):
                if (currentByte == self.CommandLibrary[i][0]):
                    libIndex = i
            if (libIndex != -1):
                if (strer != ''):
                    strer = strer.lstrip(' ')
                    strer = '#0-' + strer
                    strer += '\n'
                    outFile.write(strer)
                    strer = ''

                # Здесь функционал по командам.
                outFile.write("#1-")
                if (self.CommandLibrary[libIndex][2] == ''):
                    outFile.write(analyzer)
                else:
                    if (self.CommandLibrary[libIndex][2] == 'STR_CRYPT'):
                        outFile.write('STR_UNCRYPT')
                    else:
                        outFile.write(self.CommandLibrary[libIndex][2])
                #outFile.write(' ' + str(pointer) + '\n')
                outFile.write('\n')
                pointer += 1

                for j in range(len(self.CommandLibrary[libIndex][1])):
                    currentCom = self.CommandLibrary[libIndex][1][j]
                    if ((currentCom == 'I') or (currentCom == 'i')):
                        owBytes = self.__mesBytes[pointer:pointer+4]
                        args[zlo].append(struct.unpack(self.CommandLibrary[libIndex][3][j] + currentCom, owBytes)[0])
                        pointer += 4
                    elif ((currentCom == 'h') or (currentCom == 'H')):
                        owBytes = self.__mesBytes[pointer:pointer+2]
                        args[zlo].append(struct.unpack(self.CommandLibrary[libIndex][3][j] + currentCom, owBytes)[0])
                        pointer += 2
                    elif ((currentCom == 'b') or (currentCom == 'B')):
                        owBytes = self.__mesBytes[pointer:pointer+1]
                        args[zlo].append(struct.unpack(self.CommandLibrary[libIndex][3][j] + currentCom, owBytes)[0])
                        pointer += 1
                    elif (currentCom == 'S'):
                        mode = currentByte
                        leng, result = self.__getString(mode, pointer)
                        args[zlo].append(result)
                        pointer += leng
                        pointer += 1 #После строк всегда \x00.

                whatIndex = 0
                while (whatIndex < len(self.OffsetsLibrary)):
                    if (currentByte == self.OffsetsLibrary[whatIndex][0]):
                        break
                    whatIndex += 1
                if (whatIndex < len(self.OffsetsLibrary)):
                    for i in range(len(self.__offsets)):
                        if ((args[zlo][self.OffsetsLibrary[whatIndex][1]] + (self.__prm[0]*4 + 8)) == self.__offsets[i]):
                            args[zlo][self.OffsetsLibrary[whatIndex][1]] = i
                            break
                    if (args[zlo][self.OffsetsLibrary[whatIndex][1]] > 500):
                        print("КАРАУЛ!", zlo)

                outFile.write(str(args[zlo]))
                if (pointer != len(self.__mesBytes)):
                    outFile.write('\n')

            else:
                strer += ' ' + analyzer
                pointer += 1
        if (strer != ''):
            strer = strer.lstrip(' ')
            strer = '#0-' + strer
            outFile.write(strer)

        outFile.close()
        return strings, commands, args
    def __dissHeaderPlus(self):
        prm = []
        offsets = []
        prm = list(struct.unpack('II', self.__mesBytes[0:8]))

        pointer = 8
        for i in range(prm[0]):
            offsets.append(struct.unpack('I', self.__mesBytes[pointer:pointer+4])[0])
            pointer+=4
        print(pointer)
        return prm, offsets
    def __getString(self, mode : int, pointer : int):
        #0x0A, 0x0B, 0x33.
        lenner = 0
        string = b''
        byte = self.__mesBytes[pointer:pointer+1]
        while (byte != b'\x00'):
            string += byte
            lenner += 1
            byte = self.__mesBytes[pointer+lenner:pointer+lenner+1]
        if (mode == 0x0A):
            list = string.hex(' ').split(' ')
            string = b''
            i = 0
            while (i < len(list)):
                number = int(list[i], 16)
                if (number < 0x81):
                    zlo = number - 0x7D62
                    high = (zlo & 0xff00) >> 8
                    low = zlo & 0xff
                    marbas = str(hex(high))[2:]
                    if (len(marbas) == 1):
                        marbas = "0" + marbas
                    string += byte.fromhex(marbas)
                    marbas = str(hex(low))[2:]
                    if (len(marbas) == 1):
                        marbas = "0" + marbas
                    string += byte.fromhex(marbas)
                    i += 1
                else:
                    high = int(list[i], 16)
                    marbas = str(hex(high))[2:]
                    if (len(marbas) == 1):
                        marbas = "0" + marbas
                    string += byte.fromhex(marbas)
                    if ((i+1) < len(list)):
                        i += 1
                        low = int(list[i], 16)
                        marbas = str(hex(low))[2:]
                        if (len(marbas) == 1):
                            marbas = "0" + marbas
                        string += byte.fromhex(marbas)
                    i += 1
            try:
                return lenner, (string.decode('shift-jis').replace('\u3000', '　'))
            except:
                return lenner, string.hex(' ')
        elif ((mode == 0x33) or (mode == 0x0B)):
            try:
                return lenner, string.decode('shift-jis')
            except:
                print(string)
                return lenner, string
        else:
            return lenner, string