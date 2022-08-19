# coding=utf-8
import sys, re, os, pyperclip, winshell, configparser, codecs, random, time
from win32com.client import Dispatch
from PIL import Image
from win10toast import ToastNotifier

# Сonfig
config = configparser.ConfigParser()
config.read("!settings.ini", encoding="utf-8")

# Library
def getClipboard():
    data = pyperclip.paste()
    return data


def cache(command):
    match command:
        case "check":
            if not (os.path.isdir("temp")):
                os.makedirs("temp")
        case "clear":
            for file in os.scandir("temp"):
                os.remove(file.path)


def isYoutube(link):
    link = link.lower()
    n = 0
    if re.search("https://", link):
        n += 1
    if re.search("youtube", link):
        n += 1
    if re.search("youtu.be", link):
        n += 1

    return True if n > 1 else False


def fileType(link):

    if link.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff")):
        return "image"
    elif link.lower().endswith((".gif", ".mp4", ".webm")):
        return "animation"
    else:
        return False
    # return True if link.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.tif', '.tiff')) else False


def imageAutoResizer(path, limitWidth, limitHeight):
    image = Image.open(path)
    width, height = image.size

    if width > limitWidth or height > limitHeight:
        currentDir = os.path.dirname(os.path.realpath(__file__))
        tempFile = r"\temp\result.png"

        s = width / height

        if width > height:
            newHeight = round(limitWidth / s)
            newWidth = limitWidth
            print("original width:", width, "height:", height)
            print("s:", s, "width:", newWidth, "height:", newHeight)
        else:
            newHeight = limitHeight
            newWidth = round(limitHeight * s)

        resize = image.resize((newWidth, newHeight))
        resize.save(currentDir + tempFile)

        return currentDir + tempFile
    else:
        return path


def isCommand(cmd=None):
    match cmd.lower():
        case "exit":
            end("p")

    if cmd.lower().startswith("хорошо призрачку?"):
        words = ["порно", "хентай", "hentai", "r34", "rule 34", "лисошиз"]
        clipboardData = getClipboard()

        def finderWord(str_, words):
            for word in words:
                if word.lower() in str_.lower():
                    return True
            return False

        if finderWord(clipboardData, words):
            idEgg = random.randint(1, 6)
            match idEgg:
                case 1:
                    print(
                        "призрачку не нравится что у "
                        + os.getlogin()
                        + " содержится в буфере обмена 3:"
                    )
                case 2:
                    print(
                        "призрачку совсем не нравится что у "
                        + os.getlogin()
                        + " в буфере обмена 3:"
                    )
                case 3:
                    print("плохо призрачку в компьютере у " + os.getlogin() + " 3:")
                case 4:
                    print("призрачку не нравится что содержится в буфере обмена 3:")
                case 5:
                    print("призрачку не нравятся пошлости в буфере обмена 3:")
                case 6:
                    print("плохо призрачку 3:")
        else:
            idEgg = random.randint(1, 4)
            match idEgg:
                case 1:
                    print("хорошо призрачку в компьютере " + os.getlogin() + " :3")
                case 2:
                    print("призрачку хорошо живётся в компьютере :3")
                case 3:
                    print("да, призрачку хорошо в компьютере :3")
                case 4:
                    print(
                        "хорошо призрачку, но призрачку будет лучше, когда "
                        + os.getlogin()
                        + " даст ссылочку на видео :3"
                    )


def renderToVid(outFile, file, link, type):
    audBitrate = config["Audio"]["bitrate"]
    outFile = outFile + ".webm"

    match config["Main"]["OwnUtils"].lower():
        case "true":
            if os.path.exists(r".\utils\ffmpeg.exe") and os.path.exists(
                r".\utils\yt-dlp.exe"
            ):
                ffmpeg_path = r".\utils\ffmpeg.exe"
                ytdlp_path = r".\utils\yt-dlp.exe"
            else:
                if os.system("ffmpeg -version") or os.system("yt-dlp --version"):
                    errId(6)
                else:
                    print(
                        "Встроенные утилиты не найдены, но в вашем компьютере есть эти недостоющие зависимости. Измените в !settings.ini значение OwnUtils на false"
                    )
                    errId(6)

        case "false":
            ffmpeg_path = "ffmpeg.exe"
            ytdlp_path = "yt-dlp.exe"
        case _:
            errId(5)

    os.system(ytdlp_path + " -f 251 " + link + r" -o temp\temp.webm")
    os.system(ffmpeg_path + r" -i temp\temp.webm temp\temp.wav")
    if os.path.exists(outFile):
        os.remove(outFile)

    if type == "image":
        os.system(
            ffmpeg_path
            + ' -r 10 -loop 1 -i "'
            + file
            + r'" -i temp\temp.wav -c:a libopus -b:a '
            + audBitrate
            + 'K -c:v libvpx-vp9 -strict -2 -shortest "'
            + outFile
            + '"'
        )
    elif type == "animation":
        os.system(
            ffmpeg_path
            + ' -stream_loop -1 -i "'
            + file
            + r'" -i temp\temp.wav -shortest -map 0:v:0 -map 1:a:0 -y "'
            + outFile
            + '"'
        )

    if os.path.exists(outFile):
        setIcon(True)
        notify("done")
    else:
        notify("undone")
        errId(4)
        end()


def notify(type):
    def notify(header, text=" ", delay=3, icon="icons/m_h.ico"):
        ToastNotifier().show_toast(
            header,
            text,
            duration=delay,
            icon_path=icon,
            threaded=True,
        )

    match type.lower():
        case "done":
            notify("Готово!")
        case "undone":
            notify("ошибка", " ", 3, "icons/m_s.ico")
        case "firstrun":
            notify("Готово!", "Установка завершена", 5)


def errId(id):
    def showNumErr(n):
        return "::ОШИБКА " + str(n) + " ::"

    setIcon(False)

    match id:
        case 1:
            print(showNumErr(1), "В буфере обмена не найдена ссылка на Youtube")
        case 2:
            print(showNumErr(2), "Недостаточно аргументов")
        case 3:
            print(showNumErr(3), "Файл не является изображением/видео")
        case 4:
            print(showNumErr(4), "Выходного файла не существует. Ошибка в рендере")
        case 5:
            print(showNumErr(5), "Ошибка в конфиге, проверьте !settings.ini")
            print(
                showNumErr(5),
                "Если удалите конфигурационный файл, то создастся рабочий с параметрами по умолчанию.",
            )
            end()
        case 6:
            print(
                showNumErr(6),
                "Не хватает утилит для выполнения рендера. Возможно, вы установили не полный пакет, поставьте полноценную версию",
            )
            end()
        case _:
            print(showNumErr("неизвестно"), "неизвестная ошибка")
            end()


def shortcutCreator(path, target, wDir, icon):
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()


def sendToBridgeCreator():
    fp = open("scr.cmd", "w")
    fp.write("@echo off")
    fp.write("\n")
    fp.write("cls")
    fp.write("\n")
    fp.write('"' + sys.argv[0] + '"' + " %1")
    fp.close()


def setIcon(val):
    linkName = config["Shortcut"]["SendTo_Name"] + ".lnk"
    currentDir = os.path.dirname(os.path.realpath(__file__))

    sendTo = winshell.sendto()
    path = os.path.join(sendTo, linkName)
    target = currentDir + r"\scr.cmd"
    wDir = currentDir
    typeIcon = r"\icons\m_h.ico" if val else r"\icons\m_s.ico"
    icon = currentDir + typeIcon

    shortcutCreator(path, target, wDir, icon)


def end(code=None):
    match code:
        case "p":
            sys.exit()
        case "sleep":
            time.sleep(5)
            sys.exit()
        case _:
            input()
            sys.exit()


# Inicialization Program
if not (os.path.exists("scr.cmd")):
    sendToBridgeCreator()
    setIcon(True)
    notify("firstRun")
    print(":: Первоначальная настройка завершена!")
    end("p")

if not (os.path.exists("!settings.ini")):
    # Да что вы знаете о безумии? :3
    fp = codecs.open("!settings.ini", "w", "utf-8")
    fp.write("[Main]")
    fp.write("\n")
    fp.write("OwnUtils=true")
    fp.write("\n")
    fp.write("\n")
    fp.write("[Shortcut]")
    fp.write("\n")
    fp.write("SendTo_Name=Картинку В Видео из юбуба")
    fp.write("\n")
    fp.write("\n")
    fp.write("[Audio]")
    fp.write("\n")
    fp.write("bitrate=128")
    fp.write("\n")
    fp.write("\n")
    fp.write("[Video]")
    fp.write("\n")
    fp.write("autoSizeChanger=true")
    fp.write("\n")
    fp.write("limitWidth=1920")
    fp.write("\n")
    fp.write("limitHeight=1080")
    fp.close()

# Main Program
argCount = len(sys.argv)
cache("check")
cache("clear")

if argCount > 1:
    argFileLink = sys.argv[1]

    if argFileLink.lower() == "uninstall":
        linkName = config["Shortcut"]["SendTo_Name"] + ".lnk"
        sendTo = winshell.sendto()
        path = os.path.join(sendTo, linkName)

        if os.path.exists(path):
            os.remove(path)

        end("p")

    videoLink = getClipboard()
    while isYoutube(videoLink) == False:
        errId(1)
        videoLink = input("Введите ссылку: ")
        isCommand(videoLink)

    if fileType(argFileLink) == "image":
        match (config["Video"]["autoSizeChanger"].lower()):
            case "true":
                FileLink = imageAutoResizer(
                    argFileLink,
                    int(config["Video"]["limitWidth"]),
                    int(config["Video"]["limitHeight"]),
                )
            case "false":
                FileLink = argFileLink
            case _:
                errId(5)

        renderToVid(argFileLink, FileLink, videoLink, "image")

    elif fileType(argFileLink) == "animation":
        FileLink = argFileLink
        renderToVid(argFileLink, FileLink, videoLink, "animation")

    else:
        errId(3)
        end()

    cache("clear")
else:
    errId(2)
    end("sleep")
