# mIY - mix Image & YouTube
Утилита для микса изображения с аудиодорожкой из YouTube с помощью контекстного меню "Отправить"

## Зачем?
Короткий ответ: **Имиджборды.**

Некоторые пользователи имиджборд часто встречаются с ситуациями, когда необходимо поделиться музыкой. Имиджборды не позволяют загружать Mp3, Aac и другие контейнеры. Поэтому пользователи в качестве альтернативы начали использовать видеоконтейнер webm, чтобы делиться музыкой. На видеоряд для "разнообразия" начали использовать различные изображения из своего компьютера.

Проблема состоит в том, что для того, чтобы поделиться таким образом музыкой на имиджбордах - это очень трудозатратный процесс.

Утилита призвана упростить этот процесс буквально до нескольких щелчков мыши.

# Как пользоваться?
[Демонстрация работы.webm](https://user-images.githubusercontent.com/110712717/183269146-1bd6d245-9b8f-4ddb-8854-1ef2781ed747.webm)

1. Скопируйте ссылку на музыку из YouTube;
2. Нажмите правой кнопкой мыши по изображению чтобы вызвать контекстное меню;
3. В контекстном меню в пункте "Отправить" выберите утилиту;
4. После процесса миксирования, в каталоге, где находится это изображение, появится файл с таким же именем и расширением .webm;
5. Отправить музыкальный .webm на имиджборду.

# Установка
На данный момент, установочный пакет не хранит в себе необходимые утилиты FFmpeg и YT-dlp, поэтому вам необходимо будет установить эти зависимости самостоятельно.

### 1. Установка зависимостей с помощью Chocolatey
> Если у вас не установлен Chocolatey, вы можете сделать по этой инструкции: [Подробная установка](https://github.com/nanCreate/mIY/wiki/%D0%9F%D0%BE%D0%B4%D1%80%D0%BE%D0%B1%D0%BD%D0%B0%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0 "Подробная установка")

Не забывайте, что для установки этих зависимостей, у вас должен быть открыт терминал от имени администратора.

```choco install ffmpeg yt-dlp -y```

### 2. Установка mIY
1. Скачайте установочный пакет из [страницы релизов](https://github.com/nanCreate/mIY/releases "страницы релизов")
2. Запустите его и примите лицензию чтобы началась автоматическая установка
