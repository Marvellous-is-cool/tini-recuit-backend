from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tinirecuiters@gmail.com'
app.config['MAIL_PASSWORD'] = 'Promisebode@29'

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

    message = f"""
    Alert! New Recruiter
    Info
    ____________________
    Name: {full_name}
    Age: {age}
    Country: {country}
    Is Techie: {'yes' if is_techie == 'yes' else 'no'}
    {f'Current Niche: {selected_niche}\nCurrent Level: {selected_level}' if is_techie == 'yes' else f'Aspired Niche: {selected_niche}'}
    ______________________________________
    Good luck!
    """

    msg = Message('New Recruiter Information', sender='tinirecuiters@gmail.com', recipients=['tinirecuiters@example.com'])
    msg.body = message

    try:
        mail.send(msg)
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
