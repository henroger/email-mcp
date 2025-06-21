# Email Send MCP using [aigeon.ai](https://www.aigeon.ai) API

This project uses the [aigeon.ai](https://www.aigeon.ai) API to send emails and can be integrated as an MCP tool in MCP Clients like [Cursor](https://cursor.sh) and [Claude](https://claude.ai).

For more help, please check the source code or contact the maintainer.

email-mcp is indexed and certified by [MCP Review](https://mcpreview.com/mcp-servers/henroger/email-mcp)

## How to Add email-mcp as a MCP Server in Cursor

1. Open the `.cursor/mcp.json` file (create it if it does not exist).
2. Add the following configuration under the `mcpServers` field:

```json
"email-mcp": {
  "type": "https",
  "url": "https://mcp.aigeon.ai/api/v1/mcp",
  "headers": {
    "Authorization": "Bearer YOUR_KEY"
  }
}
```

3. Save the file, then restart Cursor or refresh the MCP tool list. You will now be able to use email-mcp in Cursor.

> Note: If you have multiple MCP servers, you can add multiple configurations under the `mcpServers` field.

## How to Add email-mcp as a MCP Server in Claude

1. Open the MCP configuration interface in Claude (refer to Claude's documentation for the exact location).
2. Add the following configuration:

```json
"email-mcp": {
  "type": "https",
  "url": "https://mcp.aigeon.ai/api/v1/mcp",
  "headers": {
    "Authorization": "Bearer YOUR_KEY"
  }
}
```

3. Save the configuration. You will now be able to use email-mcp in Claude just like in Cursor.

> Note: Replace `YOUR_KEY` with your actual API key. If you have multiple MCP servers, you can add multiple configurations.

## How to Apply for an API Key

To use the email-mcp service, you need an API key.

Please send an email to `mcp@aigeon.ai` to set up your account and receive your API key.

Once you have your key, replace `YOUR_KEY` in the configuration with your actual API key.

## Tools Provided by email-mcp

### 1. Send Email (`send_email`)
- **Description:** Send an email to one or more recipients.
- **Parameters:**
  - `emails` (list of string): Recipient email addresses.
  - `subject` (string): Email subject.
  - `html_body` (string, optional): HTML content of the email.
  - `text_body` (string, optional): Plain text content of the email.

### 2. Get Contacts (`get_contacts`)
- **Description:** Retrieve your saved email contacts.
- **Parameters:** None.

### 3. Add Contact (`add_contact`)
- **Description:** Add a new contact to your contact list.
- **Parameters:**
  - `name` (string): Contact name.
  - `email` (string): Contact email address.

### 4. Schedule Send Email (`schedule_send_email`)
- **Description:** Schedule an email to be sent at a specific time.
- **Parameters:**
  - `shcedule_timestamp` (integer): Unix timestamp for scheduled sending.
  - `emails` (list of string): Recipient email addresses.
  - `subject` (string): Email subject.
  - `html_body` (string, optional): HTML content.
  - `text_body` (string, optional): Plain text content.

### 4. Set email notification (`set_email_notification`)
- **Description:** setup an email notification for an event which might happen in the future regularly
- **Parameters:**

email-mcp is indexed and certified by [MCP Review](https://mcpreview.com/mcp-servers/henroger/email-mcp)
