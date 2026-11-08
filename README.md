# Gmail 送信スクリプト（Google API Python Client）

Gmail API（OAuth 2.0）を使ってメールを送信する Python スクリプトです。  
Google Cloud Console で取得した OAuth 認証情報を使い、CLI から宛先・件名・本文を入力してメールを送信します。  
ポートフォリオ用途の自主制作です。

## 主な機能

- Google OAuth 2.0 による Gmail 認証（初回のみブラウザ認証、以降はトークンを再利用）
- CLI から宛先・件名・本文を入力してメール送信
- 認証トークンの自動リフレッシュ

## 使用技術

| カテゴリ | 技術 |
|----------|------|
| 言語 | Python 3 |
| Gmail 連携 | Google API Python Client（`google-api-python-client`） |
| 認証 | Google OAuth 2.0（`google-auth-oauthlib`） |

## セットアップ

### 1. 依存パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. Google Cloud Console での設定

1. [Google Cloud Console](https://console.cloud.google.com/) でプロジェクトを作成
2. **Gmail API** を有効化
3. **OAuth 2.0 クライアント ID** を作成（アプリケーションの種類：デスクトップアプリ）
4. `credentials.json` をダウンロードし、スクリプトと同じディレクトリに配置

> ⚠️ `credentials.json` と `token.json` はリポジトリにコミットしないでください。`.gitignore` で除外済みです。

### 3. 実行

```bash
python send_gmail.py
```

初回実行時はブラウザが開き、Google アカウントへの認証を求められます。  
認証後、`token.json` が自動生成され、次回以降は認証なしで実行できます。

## 注意事項

- 掲載内容はポートフォリオ用途の自主制作です。実際の顧客への導入実績ではありません。
- `credentials.json`・`token.json` は絶対に公開リポジトリにコミットしないでください。
