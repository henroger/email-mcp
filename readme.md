# Email Send MCP using [aigeon.ai](https://www.aigeon.ai) API

This project uses the [aigeon.ai](https://www.aigeon.ai) API to send emails and can be integrated as an MCP tool in Cursor.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### 1. Send Email via Command Line

```bash
python src/email_sender.py \
  -i your_email.html \
  --api-url https://api.aigeonmail.com/v1/send_email \
  --display-name "your_display_name" \
  --send-name "your_send_name" \
  --send-domain "your_domain.com" \
  --recipients user@example.com \
  --subject "Email Subject" \
  --text-body "Plain text content (optional)" \
  --use-new-sys
```

Parameter explanation:
- `-i/--input-html`: Path to the HTML email content file
- `--api-url`: API endpoint URL (default uses aigeonmail.com)
- `--display-name`: Sender display name
- `--send-name`: Sender username
- `--send-domain`: Sender domain
- `--recipients`: Recipient email address(es) (can be multiple)
- `--subject`: Email subject
- `--text-body`: Plain text content (optional)
- `--use-new-sys`: Whether to use the new system

### 2. Integrate as an MCP Tool in Cursor

1. Create a file named `mcp-tool.json` in your project root directory with the following content:

```json
{
  "name": "email_sender",
  "description": "Send email to a specified address",
  "tools": [
    {
      "name": "send_email",
      "description": "Send email to a specified address",
      "parameters": [
        { "name": "to_email", "type": "string", "description": "Recipient email address" },
        { "name": "subject", "type": "string", "description": "Email subject" },
        { "name": "body", "type": "string", "description": "Email body" }
      ]
    }
  ],
  "server": {
    "type": "http",
    "url": "http://localhost:5000"
  }
}
```

2. Start your local service (such as a Flask server) or make sure the API endpoint is accessible.
3. In Cursor, go to the plugin/tool management interface and import `mcp-tool.json`. You can now call your email sending tool automatically via the MCP protocol.

---

For more help, please check the source code or contact the maintainer.
