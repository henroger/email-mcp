from flask import Flask, request, jsonify
from email_sender import send_email

app = Flask(__name__)

# HTTP API: /send_email
@app.route('/send_email', methods=['POST'])
def api_send_email():
    data = request.json
    required_fields = ['to_email', 'subject', 'body', 'api_key']
    for field in required_fields:
        if field not in data:
            return jsonify({'success': False, 'message': f'缺少参数: {field}'})
    success, message = send_email(
        data['api_key'],
        data['recipients'],
        data['subject'],
        data['html_body'],
        data['text_body'],
    )
    return jsonify({'success': success, 'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 