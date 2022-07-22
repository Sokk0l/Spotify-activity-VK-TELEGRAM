from spotipy.oauth2 import SpotifyOAuth
import spotipy
import vk_api
from time import sleep

config = {
    'vk-default-status': "sample if not playing in VK",
    'telegram-default-status': 'sample if not playing in Telegram',
    'status-update-timeout': 10,
    'spotify-client-id': "find in https://developer.spotify.com/dashboard/",
    'spotify-client-secret': "find in https://developer.spotify.com/dashboard/",
    'spotify-redirect-uri': "set in https://developer.spotify.com/dashboard/",
    'spotify-username': "get in your profile open.spotify.com/user/sample",
    'vk-token': "token",
    'vk-online-when-listen-spotify': True,
    'use-telegram': True,
    'telegram-api-id': https://my.telegram.org/,
    'telegram-api-hash': 'https://my.telegram.org/'
    }


if config['use-telegram']:
    from telethon.tl.functions.account import UpdateProfileRequest
    from telethon.sync import TelegramClient
    telegram = TelegramClient('telegram', config['telegram-api-id'], config['telegram-api-hash']).start()

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-playback-state user-library-read", client_id=config['spotify-client-id'], client_secret=config['spotify-client-secret'], redirect_uri=config['spotify-redirect-uri'], username=config['spotify-username']))
api = vk_api.VkApi(token=config['vk-token']).get_api()
current_status = api.status.get()['text']

def change_status(status):
    if not status == current_status:
        api.status.set(text=status[:140])
        if config['vk-online-when-listen-spotify']: api.account.setOnline(voip=1)
        print('VK status updated')
    if config['use-telegram']:
        telegram(UpdateProfileRequest(about=status[:70]))
        print('Telegram status updated')
    print(status)
def default_status():
    api.status.set(text=config['vk-default-status'][:140])
    print('VK status updated')
    if config['use-telegram']:
        telegram(UpdateProfileRequest(about=config['telegram-default-status'][:70]))
        print('Telegram status updated')
    print('Normal status set')
while True:
    current_playing = spotify.current_user_playing_track()
    if current_playing is None or current_playing["currently_playing_type"] == "ad":
        default_status()
        sleep(int(config['status-update-timeout'])*2)
        continue
    play_emoji = '' if current_playing['is_playing'] == True else ''
    change_status(play_emoji+'Listening to Spotify: '+current_playing["item"]["artists"][0]["name"]+' — '+current_playing["item"]["name"]+'')
    sleep(int(config['status-update-timeout']))
