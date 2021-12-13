# youtube-photo - Substitute YouTube platform with a cloud for photos

Generating a H.264 video from the specified pictures and upload to YouTube.

## Install

### From source

```bash
git clone --depth 1 https://github.com/inanu\iwaudon/youtube-photo
cd youtube-photo
pip install -e .
```

### From PyPI

```bash
pip install youtube-photo
```

## Usage

First, cleate `client_secrets.json` and write credential information of YouTube Data API like this:

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

### When uploading

1. Store images for upload in `img` folder in the same directory
2. Execute `ytp up`
3. After finishing the upload, Video URL (`https://www.youtube.com/watch?v=***`) will be printed
4. Keep its ID

### When downloading

1. Execute `ytp dl <Video ID>`
2. After finishing the download, The decrypted image files will be extracted to the `download-img` folder

## CLI Help

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

## License

???

## Article

- [容量無制限のYouTubeに写真を保存してGoogleフォト代わりに使うソフトを作ったよ！！](https://soudakyoto-ikou.hatenadiary.jp/entry/20210322/1616418041) (in Japanese)
