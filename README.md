# Youtube-Photo
Youtube-Photo - Substitute YouTube platform with a cloud for photos

## Description
フォルダ内に保存した写真から4K解像度のH.264動画を生成し、YouTubeにアップロードします。
ダウンロードした

## Requirement
- [googleapis/google-api-python-client](https://github.com/googleapis/google-api-python-client)
- [googleapis/oauth2client](https://github.com/googleapis/oauth2client)
- [ytdl-org/youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [python-pillow/Pillow](https://github.com/python-pillow/Pillow)
- [opencv-python](https://pypi.org/project/opencv-python/)

## Usage
+ upload.py, youtube_upload.py, download.py を配置したディレクトリ上に client_secrets.json を作成し、YouTube Data API に関して記述します。
```json
{
  "web": {
    "client_id": "676728775297-t47fsof0a3o86094t8unk4gipd7b9kvk.apps.googleusercontent.com",
    "client_secret": "M_7iLBqUXqLqyB2633kPcZYM",
    "redirect_uris": [],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token"
  }
}
```
+ 同ディレクトリ上のimgフォルダ内にアップロード用の画像を格納します。
+ 