from flask import Flask, jsonify, request
from flask_cors import CORS
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

def sendEmail(message, receiver):
    EMAIL_SENDER = os.getenv('EMAIL')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

    msg = EmailMessage()
    sender = EMAIL_SENDER
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Mensaje de Adrian Ramirez'
    msg.add_alternative(message, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, EMAIL_PASSWORD)
        smtp.send_message(msg)
    return f'Tu correo ha sido enviado a {receiver}'

@app.route('/sendEmail', methods=['POST'])
def send():
    data=request.get_json()
    sendEmail(data, 'adrianxramirez980@gmail.com')
    message = {'message': 'El correo se ha enviado correctamente'}
    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
