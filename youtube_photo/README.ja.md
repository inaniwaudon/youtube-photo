# youtube-photo

[日本語版READMEはこちら](README.ja.md)

- YouTubeのプラットフォームを写真用クラウドの代わりにする
- 指定した写真からH.264動画を生成し、YouTubeにアップロードする

## インストール

### ソースから

```bash
git clone --depth 1 https://github.com/inanu\iwaudon/youtube-photo
cd youtube-photo
pip install -e .
```

### PyPIから

```bash
pip install youtube-photo
```

## 使用方法

まず`client_secrets.json`を作成し、YouTube Data APIの認証情報を以下のように記述します。

```json
{
  "web": {
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uris": [],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token"
  }
}
```

### アップロード

1. アップロード用の画像は、同じディレクトリ内の `img` フォルダに格納
2. `ytp up`を実行
3. アップロード終了後、動画ID(`https://www.youtube.com/watch?v=***`)が表示される
4. 表示されたIDを覚えておく

### ダウンロード

1. `ytp dl <Video ID>`を実行
2. ダウンロード終了後、復号化された画像ファイルが解凍され `download-img` フォルダに保存される

## コマンドラインヘルプ

```shellsession
$ ytp -h
usage: ytp [-h] [-V] {upload,up,download,dl} ...

Generating a H.264 video from the specified pictures and upload to YouTube.

positional arguments:
  {upload,up,download,dl}
    upload (up)            upload images
    download (dl)          download images

optional arguments:
  -h, --help               show this help message and exit
  -V, --version            show program's version number and exit
$ ytp up -h
usage: ytp upload [-h] [-d DIR] [-a JSON]

optional arguments:
  -h, --help                 show this help message and exit
  -d DIR, --img_dir DIR      upload dir (default: img)
  -a JSON, --auth_path JSON  credencial path (default: client_secrets.json)
$ ytp dl -h
usage: ytp download [-h] [-d DIR] ID

positional arguments:
  ID                     target youtube video id

optional arguments:
  -h, --help             show this help message and exit
  -d DIR, --img_dir DIR  dir contains pictures (default: download-img)
```

## ライセンス

???

## 解説記事

- [容量無制限のYouTubeに写真を保存してGoogleフォト代わりに使うソフトを作ったよ！！](https://soudakyoto-ikou.hatenadiary.jp/entry/20210322/1616418041) (in Japanese)
