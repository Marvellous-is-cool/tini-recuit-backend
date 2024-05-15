from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.environ.get('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mail = Mail(app)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.get_json()
    full_name = data.get('fullName')
    age = data.get('age')
    country = data.get('country')
    is_techie = data.get('isTechie')
    selected_niche = data.get('selectedNiche')
    selected_level = data.get('selectedLevel')

    message = (
        f"Alert! New Recruiter\n"
        f"Info\n"
        f"____________________\n"
        f"Name: {full_name}\n"
        f"Age: {age}\n"
        f"Country: {country}\n"
        f"Is Techie: {'yes' if is_techie == 'yes' else 'no'}\n"
        f"{f'Current Niche: {selected_niche}\nCurrent Level: {selected_level}' if is_techie == 'yes' else f'Aspired Niche: {selected_niche}'}\n"
        f"______________________________________\n"
        f"Good luck!"
    )

    msg = Message('New Recruiter Information', sender=os.environ.get('MAIL_USERNAME'), recipients=['recipient_email@example.com'])
    msg.body = message

    try:
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
