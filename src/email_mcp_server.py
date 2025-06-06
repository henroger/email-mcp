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

@app.route('/', methods=['GET', 'POST'])
@app.route('/tools', methods=['GET', 'POST'])
@app.route('/openapi.json', methods=['GET', 'POST'])
@app.route('/mcp', methods=['GET', 'POST'])
def index():
    return jsonify({
        "name": "email_mcp",
        "description": "Send email via MCP server",
        "tools": [
            {
                "name": "send_email",
                "description": "Send email to a specified address",
                "parameters": [
                    { "name": "api_key", "type": "string", "description": "API key" },
                    { "name": "recipients", "type": "string", "description": "Recipient email addresses, comma separated" },
                    { "name": "subject", "type": "string", "description": "Email subject" },
                    { "name": "html_body", "type": "string", "description": "HTML body" },
                    { "name": "text_body", "type": "string", "description": "Text body" }
                ]
            }
        ]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 