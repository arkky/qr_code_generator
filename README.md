# QR Code Generator

## Features

- You can generate any QR code with your word and add it to Google Authenticator
- You can check your generated QR code in the same google authenticator or using the program

## Usage

```sh
pip install opencv-python qrcode climage pyotp
```

```sh
python3 main.py --generate-qr example@gmail.com
```

![Semantic description of image](/imgs/generated_qr_code.png "Generated QR Code")
<br>

```sh
python3 main.py --get-otp 
```

```sh
scan or type: type
```

```sh
Your secret key, please: <enter your secret qr code>
```

![Semantic description of image](/imgs/get_otp.png "6 digit code")
<br>

OR

```sh
scan
```

```sh
Path to qr code: <enter path to your image with qr code>
```
