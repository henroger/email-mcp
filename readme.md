# Email Send MCP using [aigeon.ai](https://www.aigeon.ai) API

This project uses the [aigeon.ai](https://www.aigeon.ai) API to send emails and can be integrated as an MCP tool in MCP Clients like Cursor.


For more help, please check the source code or contact the maintainer.

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

## How to Apply for an API Key

To use the email-mcp service, you need an API key.

Please send an email to `mcp@aigeon.ai` to set up your account and receive your API key.

Once you have your key, replace `YOUR_KEY` in the configuration with your actual API key.
