# coding=utf-8
import sys, re, os, pyperclip, winshell, configparser
from win32com.client import Dispatch
# Сonfig
config = configparser.ConfigParser()
config.read('!settings.ini', encoding='utf-8')

# Library
def getClipboard():
    data = pyperclip.paste()
    return(data)

def isYoutube(link):
    link = link.lower()
    n = 0
    if (re.search('https://', link)): n+=1
    if (re.search('youtube', link)): n+=1
    if (re.search('youtu.be', link)): n+=1

    return True if n>1 else False

def isImage(link):
    return True if link.lower().endswith(('.png', '.jpg', '.jpeg', '.avif', '.webp', '.tif', '.tiff')) else False

def isCommand(cmd=None):
    match cmd.lower():
        case 'exit': end('p')

    if (cmd.lower().startswith('хорошо призрачку')): 
        print('да, призрачку тоже хорошо :3')

def renderToVid(file, link):
    audBitrate = config["Audio"]["bitrate"]

    match config["Main"]["OwnUtils"].lower():
        case 'true':
            if (os.path.exists(r'.\utils\ffmpeg.exe') and os.path.exists(r'.\utils\yt-dlp.exe')):
                ffmpeg_path = r'.\utils\ffmpeg.exe'
                ytdlp_path = r'.\utils\yt-dlp.exe'
            else: 
                if (os.system('ffmpeg -version') or os.system('yt-dlp --version')):
                    errId(6)
                else: 
                    print('Встроенные утилиты не найдены, но в вашем компьютере есть эти недостоющие зависимости. Измените в !settings.ini значение OwnUtils на false')
                    errId(6)
                
        case 'false':
            ffmpeg_path = 'ffmpeg.exe'
            ytdlp_path = 'yt-dlp.exe'
        case _:
            errId(5)

    if(os.path.exists('temp.webm')): os.remove('temp.webm')
    if(os.path.exists('temp.wav')): os.remove('temp.wav')
    os.system(ytdlp_path+" -f 251 "+link+" -o temp.webm")
    os.system(ffmpeg_path+' -i temp.webm temp.wav')
    os.remove('temp.webm')
    if(os.path.exists(file+'.webm')): os.remove(file+'.webm')
    os.system(ffmpeg_path+' -r 10 -loop 1 -i "'+file+'" -i temp.wav -c:a libopus -b:a '+audBitrate+'K -c:v libvpx-vp9 -strict -2 -shortest "'+file+'.webm"')
    os.remove('temp.wav')

    if(os.path.exists(file+'.webm')): 
        setIcon(True)
    else:
        errId(4)
        end()

def errId(id):
    def showNumErr(n):
        return ('::ОШИБКА '+str(n)+' ::')

    setIcon(False)

    match id:
        case 1:
            print(showNumErr(1),'В буфере обмена не найдена ссылка на Youtube')
        case 2:
            print(showNumErr(2),'Недостаточно аргументов')
        case 3:
            print(showNumErr(3),'Файл не является изображением')
        case 4:
            print(showNumErr(4),'Выходного файла не существует. Ошибка в рендере')
        case 5:
            print(showNumErr(5),'Ошибка в конфиге, проверьте !settings.ini')
            end()
        case 6:
            print(showNumErr(6),'Не хватает утилит для выполнения рендера. Возможно, вы установили не полный пакет, поставьте полноценную версию')
            end()
        case _:
            print(showNumErr('неизвестно'),'неизвестная ошибка')

def shortcutCreator(path, target, wDir, icon):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

def sendToBridgeCreator():
    fp = open('scr.cmd', 'w')
    fp.write('@echo off')
    fp.write('\n')
    fp.write('cls')
    fp.write('\n')
    fp.write('"'+sys.argv[0]+'"'+' %1')
    fp.close()

def setIcon(val):
    linkName = config["Shortcut"]["SendTo_Name"]+'.lnk'
    currentDir = os.path.dirname(os.path.realpath(__file__))

    sendTo = winshell.sendto()
    path = os.path.join(sendTo, linkName)
    target = currentDir+r"\scr.cmd"
    wDir = currentDir
    typeIcon = r'\icons\m_h.ico' if val else r'\icons\m_s.ico'
    icon = currentDir+typeIcon

    shortcutCreator(path, target, wDir, icon)

def end(code=None):
    match code:
        case 'p':
            sys.exit()
        case _:
            input()
            sys.exit()

# Inicialization Program
if not (os.path.exists('scr.cmd')):
    sendToBridgeCreator()
    setIcon(True)
    print(':: Первоначальная установка завершена!')
    print(':: Нажмите любую клавишу, чтобы выйти')
    end()

# Main Program
argCount = len(sys.argv)

if argCount > 1:
    argFileLink = sys.argv[1]
    if (isImage(argFileLink) == False):
        errId(3)
        end()

    videoLink = getClipboard()
    while (isYoutube(videoLink) == False):
        errId(1)
        videoLink = input('Введите ссылку: ')
        isCommand(videoLink)
    else:
        print('DEB: призрачек приступает к работе :3')
        renderToVid(argFileLink, videoLink)
else:
    errId(2)
    end()