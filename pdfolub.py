from pathlib import Path

import pdfplumber
import telebot
from gtts import gTTS

TOKEN = '6143029161:AAH9jjZPe5daGn_kn6hd8AqTirIchaUqVr8'


bot = telebot.TeleBot('6143029161:AAH9jjZPe5daGn_kn6hd8AqTirIchaUqVr8')


@bot.message_handler(commands=['start'])
def send_file(message):
    bot.send_message(message.chat_id, "Send me the file")


def handle_docs(message):
    try:
        chat_id = message.chat.id
        send_audio(chat_id)
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = 'C:/Users/Dun/Downloads/Telegram Desktop/' + message.document.file_name
        pdf_to_mp3(src)
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Processing...")
    except Exception as e:
        bot.reply_to(message, e)


def pdf_to_mp3(src, language='en'):
    file_path = src
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print('[+] Processing...')
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = ''.join(pages)
        text = text.replace('\n', '')
        with open('text2.txt', 'w') as file:
            file.write(text)
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        sends_audio = my_audio.save(f'{file_name}.mp3')
        send_audio(sends_audio)
        return f'[+] {file_name}.mp3 saved successfully!'
    else:
        return 'File not exists, check the file path'


def main():
    print(pdf_to_mp3('C:/Users/Dun/Downloads/Telegram Desktop/'))


if __name__ == '__main__':
    main()


@bot.message_handler(content_types=['send'])
def send_audio(sends_audio, chat_id, message):
    audio = sends_audio
    bot.send_chat_action(message.from_user.id, 'upload_audio')
    bot.send_audio(chat_id=chat_id, audio=open('tests/test.mp3', 'rb'))
    bot.send_audio(message.from_user.id, audio)
    audio.close()


bot.polling(none_stop=True)
