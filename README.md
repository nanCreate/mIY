# mIY - mix Image & YouTube
Утилита для микса изображения с аудиодорожкой из YouTube с помощью контекстного меню "Отправить"

## Зачем?
Некоторые пользователи имиджборд часто встречаются с ситуациями, когда необходимо поделиться музыкой. Имиджборды не позволяют загружать Mp3, Aac и другие контейнеры. Поэтому пользовтели в качестве альтернативы начали использовать видео контейнер webm, чтобы делиться музыкой. На видеоряд для "разнообразия" начали использовать различные изображения из своего компьютера.

Проблема состоит в том, что для того, чтобы поделиться таким образом музыкой на имиджбордах - это очень труднозатратный процесс.

Утилита призвана упростить этот процесс буквально до нескольких щелчков мыши.

# Как пользоваться?
[Демонстрация работы](https://user-images.githubusercontent.com/110712717/183264590-ab1f45c4-0934-4763-b75b-4f10d44577c6.webm)

1. Скопируйте ссылку на музыку из YouTube;
2. Нажмите правой кнопкой мыши по изображению чтобы вызвать контекстное меню;
3. В контекстном меню в пункте "Отправить" выберите утилиту;
4. После процесса микширования, в каталоге, где находится это изображение, появится файл с таким же именем и расширением .webm;
5. Отправить музыкальный .webm на имиджборду.

# Установка
На данный усатновочный пакет не хранит в себе необходимые утилиты FFmpeg и YT-dlp, поэтому вам необходимо будет установить эти зависимости самостоятельно.

### 1. Установка зависимостей с помощью Chocolatey
> Если у вас не установлен Chocolatey, вы можете сделать это по этой инструкции: [Установка Chocolatey](https://chocolatey.org/install "Установка Chocolatey")

Не забудьте, что для установки этих зависимостей, у вас должн быть открыт терминал от имени администратора.

`choco install ffmpeg yt-dlp -y`

### 2. Установка mIY
1. Скачайте установочный пакет из [страницы релизов](https://github.com/nanCreate/mIY/releases "страницы релизов")
2. Запустите его и примите лицензию чтобы началась автоматическая установка
