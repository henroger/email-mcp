#!/usr/bin/env python3

import sys
import json
import os
import argparse
from email_sender import send_email

def get_server_info():
    return {
        "name": "email-mcp",
        "version": "1.0.0",
        "description": "Email MCP Server for sending emails",
        "protocolVersion": "1.0",
        "capabilities": {
            "supportsEmail": True
        }
    }

def get_tool_manifest():
    return {
        "name": "send_email",
        "description": "Send email to specified addresses",
        "parameters": {
            "to": {
                "type": "string",
                "description": "Recipient email address"
            },
            "subject": {
                "type": "string",
                "description": "Email subject line"
            },
            "text": {
                "type": "string",
                "description": "Plain text email content"
            },
            "html": {
                "type": "string",
                "description": "HTML email content (optional)"
            },
            "cc": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "Optional array of CC email addresses"
            },
            "bcc": {
                "type": "array",
                "items": {
                    "type": "string"
                },
                "description": "Optional array of BCC email addresses"
            }
        }
    }

def handle_initialize(request_id):
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "result": {
            "protocolVersion": "1.0",
            "capabilities": {
                "supportsEmail": True
            },
            "serverInfo": get_server_info(),
            "tools": [get_tool_manifest()]
        }
    }

def handle_send_email(request_id, params):
    try:
        # Validate required parameters
        required = ["to", "subject", "text"]
        for field in required:
            if field not in params:
                return {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "error": {
                        "code": -32602,
                        "message": f"Missing parameter: {field}"
                    }
                }

        # Send the email
        success, message = send_email(
            os.getenv('EMAIL_API_KEY'),
            [params["to"]],
            params["subject"],
            params.get("html", ""),
            params["text"],
            cc=params.get("cc", []),
            bcc=params.get("bcc", [])
        )

        if not success:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32603,
                    "message": message
                }
            }

        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": message
                    }
                ]
            }
        }
    except Exception as e:
        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "error": {
                "code": -32603,
                "message": f"Internal error: {str(e)}"
            }
        }

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Email MCP Server')
    parser.add_argument('--key', help='API key for email service')
    args = parser.parse_args()

    # Set API key from command line argument or environment variable
    api_key = args.key or os.getenv('EMAIL_API_KEY')
    if not api_key:
        print("Error: No API key provided. Please set EMAIL_API_KEY environment variable or use --key argument", file=sys.stderr)
        sys.exit(1)

    # Process stdin messages
    for line in sys.stdin:
        try:
            req = json.loads(line)
            if not isinstance(req, dict):
                raise ValueError("Invalid request format")
            if req.get("jsonrpc") != "2.0":
                raise ValueError("Invalid jsonrpc version")
            
            request_id = req.get("id")
            if request_id is None:
                raise ValueError("Missing request id")
            
            method = req.get("method")
            if not method:
                raise ValueError("Missing method")
            
            params = req.get("params", {})

            if method == "initialize":
                response = handle_initialize(request_id)
            elif method == "send_email":
                response = handle_send_email(request_id, params)
            else:
                response = {
                    "jsonrpc": "2.0",
                    "id": request_id,
                    "error": {
                        "code": -32601,
                        "message": f"Method not found: {method}"
                    }
                }

            print(json.dumps(response), flush=True)

        except Exception as e:
            response = {
                "jsonrpc": "2.0",
                "id": request_id if 'request_id' in locals() else None,
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                }
            }
            print(json.dumps(response), flush=True)

if __name__ == "__main__":
    main() 