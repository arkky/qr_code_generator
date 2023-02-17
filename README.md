# QR Code Generator

## Features

- You can generate any QR code with your word and add it to Google Authenticator
- You can check your generated QR code in the same google authenticator or using the program

## Usage

1) ```sh
pip install opencv-python qrcode climage pyotp
```

2) ```sh
python3 main.py --generate-qr example@gmail.com
```

![Semantic description of image](/imgs/generated_qr_code.png "Generated QR Code")
<br>

3) ```sh
python3 main.py --get-otp 
```

```sh
type
```

```sh
<enter your secret qr code>
```

![Semantic description of image](/imgs/get_otp.png "6 digit code")
<br>

OR

```sh
scan
```

```sh
<enter path to your image with qr code>
```

4) 6 digit code will be printed to the terminal
5) SWAG
