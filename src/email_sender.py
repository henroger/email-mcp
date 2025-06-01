#!/usr/bin/env python3
import json
import argparse
import requests
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_html(input_html: Path) -> str:
    """Read a .html file and return its contents as a string."""
    with input_html.open("r", encoding="utf-8") as f:
        return f.read()

def send_email(
    api_key: str,
    recipients: list[str],
    subject: str,
    html_body: str,
    text_body: str,
) -> requests.Response:
    """POST the email payload to your send_email endpoint."""
    payload = {
        "api_key":      api_key,
        "display_name": "email_mcp",
        "send_name":    "email_mcp",
        "send_domain":  "aigeonmail.com",
        "emails":       recipients,
        "subject":      subject,
        "html_body":    html_body,
        "text_body":    text_body,
        "use_new_sys":  True
    }
    api_url = f"https://api.aigeonmail.com/v1/send_email"
    headers = {"Content-Type": "application/json"}
    logger.info(f"Sending payload to {api_url} for recipients {recipients}")
    resp = requests.post(api_url, headers=headers, json=payload, timeout=10)
    resp.raise_for_status()
    logger.info(f"Response {resp.status_code}: {resp.text}")
    return resp

def main():
    p = argparse.ArgumentParser(description="Read HTML → send via HTTP API")
    p.add_argument("-i", "--input-html",    required=True,
                   help="Path to input .html file")
    p.add_argument("--api-url",            required=True,
                   help="Full URL to /send_email endpoint")
    p.add_argument("--display-name",       required=True,
                   help="display_name field")
    p.add_argument("--send-name",          required=True,
                   help="send_name field")
    p.add_argument("--send-domain",        required=True,
                   help="send_domain field")
    p.add_argument("--recipients",         required=True, nargs="+",
                   help="Email address(es)")
    p.add_argument("--subject",            required=True,
                   help="Email subject")
    p.add_argument("--text-body",          default="",
                   help="Fallback text body")
    p.add_argument("--use-new-sys", action="store_true",
                   help="Whether to set use_new_sys=true")
    args = p.parse_args()

    html_path = Path(args.input_html)
    if not html_path.exists():
        logger.error(f"Input file not found: {html_path}")
        return

    html = read_html(html_path)
    logger.info(f"Read {len(html)} bytes of HTML from {html_path}")

    try:
        send_email(
            api_url      = args.api_url,
            display_name = args.display_name,
            send_name    = args.send_name,
            send_domain  = args.send_domain,
            recipients   = args.recipients,
            subject      = args.subject,
            html_body    = html,
            text_body    = args.text_body,
            use_new_sys  = args.use_new_sys
        )
    except requests.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
    except requests.RequestException as req_err:
        logger.error(f"Request error: {req_err}")
    else:
        logger.info("Email send request completed successfully.")

if __name__ == "__main__":
    main()