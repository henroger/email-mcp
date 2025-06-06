import requests
import json

def send_email(api_key, recipients, subject, html_body="", text_body="", cc=None, bcc=None):
    """
    Send email using Aigeon API
    
    Args:
        api_key (str): API key for Aigeon
        recipients (list): List of recipient email addresses
        subject (str): Email subject
        html_body (str): HTML body of the email
        text_body (str): Text body of the email
        cc (list): List of CC email addresses
        bcc (list): List of BCC email addresses
        
    Returns:
        tuple: (success, message)
    """
    url = "https://api.aigeon.com/v1/emails"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "to": recipients,
        "subject": subject,
        "html": html_body,
        "text": text_body
    }
    
    if cc:
        data["cc"] = cc
    if bcc:
        data["bcc"] = bcc
        
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        return True, "Email sent successfully"
    except requests.exceptions.RequestException as e:
        error_message = f"Failed to send email: {str(e)}"
        if hasattr(e.response, 'text'):
            try:
                error_detail = json.loads(e.response.text)
                error_message = f"Failed to send email: {error_detail.get('message', str(e))}"
            except:
                pass
        return False, error_message 