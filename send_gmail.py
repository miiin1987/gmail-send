from __future__ import print_function
import base64
from email.mime.text import MIMEText

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail送信権限
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# ファイル名
CREDENTIALS_FILE = "credentials.json"
TOKEN_FILE = "token.json"


def gmail_auth():

    creds = None

    # token.json が存在する場合
    try:
        creds = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES
        )
    except:
        pass

    # 初回認証 or 有効期限切れ
    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        # token.json 保存
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return creds


def create_message(to, subject, body):

    message = MIMEText(body)

    message["to"] = to
    message["subject"] = subject

    raw = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    return {"raw": raw}


def send_email(service, to, subject, body):

    message = create_message(
        to,
        subject,
        body
    )

    result = service.users().messages().send(
        userId="me",
        body=message
    ).execute()

    print("\nメール送信成功")
    print("Message ID:", result["id"])


def main():

    # Gmail認証
    creds = gmail_auth()

    # Gmail API 接続
    service = build(
        "gmail",
        "v1",
        credentials=creds
    )

    # 入力
    to = input("宛先メールアドレス: ")
    subject = input("件名: ")
    body = input("本文: ")

    # メール送信
    send_email(
        service,
        to,
        subject,
        body
    )


if __name__ == "__main__":
    main()