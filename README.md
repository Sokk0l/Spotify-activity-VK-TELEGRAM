
# Автостатус в ВК и автобио в Telegram c текущей песней Spotify

Нужно заполнить конфиг, затем, после запуска, войти в Spotify в браузере и войти в Telegram в консоли



## Конфиг

```bash
vk-default-status - Статус в ВК, когда в Spotify ничего не играет
telegram-default-status - О себе в Telegram, когда в Spotify ничего не играет
status-update-timeout - Количество секунд, спустя которое нужно обновить статус
spotify-client-id - Client ID приложения Spotify
spotify-client-secret - Client secret приложения Spotify
spotify-redirect-uri - redirect uri приложения Spotify
spotify-username - Часть ссылки на ваш профиль Spotify
vk-token - Токен ВК
vk-online-when-listen-spotify - Нужно ли делать вас онлайн в ВК, когда включен Spotify (True/False)
use-telegram - Нужно ли обновлять био в телеграм (поставьте False, если хотите автостатус только в ВК)
telegram-api-id - API ID приложения Telegram
telegram-api-hash - API hash приложения Telegram
```
    
## Spotify
Заходим на https://developer.spotify.com/dashboard/, если нужно, авторизуемся. Скорее всего, понадобится VPN.
Создаем приложение![App Screenshot](https://i.ibb.co/Hn6tqHn/2022-07-22-222552037.png)
вводим любое имя и описание
![App Screenshot](https://i.ibb.co/zxGgKbY/2022-07-22-222711349.png)
водим какой-нибудь адрес в redirect url. Например, http://localhost:8888/callback. Нужно, чтобы адрес совпадал с адресом в конфиге
Для получения ссылки на свой профиль заходим на https://open.spotify.com/, для пользователей из России понадобится VPN. Копируем значение после user/ это  spotify-username

## Telegram

Заходим на https://my.telegram.org/, авторизуемся
Создаем приложение
Вот и данные

## Запуск

```bash
  python main.py
```

# Autostatus in VK and autobio in Telegram with the current Spotify song

You need to fill in the config, then, after launch, enter Spotify in the browser and enter Telegram in the console



## Config

```bash
vk-default-status - VK status when nothing is playing on Spotify
telegram-default-status - About me on Telegram when nothing is playing on Spotify
status-update-timeout - The number of seconds after which to update the status
spotify-client-id - Client ID of the Spotify app
spotify-client-secret - Client secret of the Spotify application
spotify-redirect-uri - the redirect uri of the Spotify app
spotify-username - Part of the link to your Spotify profile
vk-token - VK token
vk-online-when-listen-spotify - Do you need to make you online in VK when Spotify is on (True/False)
use-telegram - Do I need to update the bio in telegram (set False if you want autostatus only in VK)
telegram-api-id - Telegram application API ID
telegram-api-hash - Telegram hash API
```
    
##Spotify
We go to https://developer.spotify.com/dashboard/, if necessary, log in. You will most likely need a VPN.
Building an app![App Screenshot](https://i.ibb.co/Hn6tqHn/2022-07-22-222552037.png)
enter any name and description
![App Screenshot](https://i.ibb.co/zxGgKbY/2022-07-22-222711349.png)
enter some address in the redirect url. For example, http://localhost:8888/callback. It is necessary that the address matches the address in the config
To get a link to your profile, go to https://open.spotify.com/, for users from Russia you will need a VPN. Copy the value after user/ is spotify-username

##telegram

Go to https://my.telegram.org/, log in
We create an application
Here is the data

## Run

```bash
  python main.py
```