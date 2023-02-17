#! /usr/bin/python3

import time
import qrcode
import pyotp
import cv2
import argparse
import climage

from urllib.parse import urlparse
from urllib.parse import parse_qs


def read_qrcode(filename):
    img = cv2.imread(filename)
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)
    return value

def get_secret(uri):
    parsed_uri = urlparse(uri)
    captured_value = parse_qs(parsed_uri.query)['secret'][0]
    return captured_value

def generate_qr(name):
    # name - user_id (email)

    # use otp library for that task
    secret = pyotp.random_base32()
    uri = pyotp.utils.build_uri(
        secret=secret,
        name=name,
        issuer="Alexander K.", # rename to your lastname
        digits=6,
        period=30,
    )
    qr = qrcode.QRCode()
    qr.add_data(uri)
    qr.make(fit=False)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    
    # show qrcode to user
    output = climage.convert("qrcode.png", is_unicode=True)
    print(output)

    # print secret key to user
    encoded_secret = get_secret(uri)
    print("Your secret key:", encoded_secret)

def generate_qr_manually(name):
    # name - user_id (email)

    # identically def above, but with more manually style
    qr = qrcode.QRCode()
    issuer = "McGwire" # rename to your lastname
    user_id = name


    # I tried to generate the secret key myself))

    # secret = base64.b32encode("abc".encode("ascii")).decode("utf-8")

    # alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # length = random.randint(12, 14)

    # secret = []

    # for i in range(length):
    #     secret.append(random.choice(alph))

    # secret = "".join(secret)
    # encoded_secret = base64.b32encode(secret.encode("ascii")).decode("utf-8")


    encoded_secret = pyotp.random_base32() # just use a built-in generator

    otpauth = f"otpauth://totp/{issuer}:{user_id}?secret={encoded_secret}&issuer={issuer}&algorithm=SHA1&digits=6&period=30"
    qr.add_data(otpauth)
    qr.make(fit=False)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    
    # show qrcode to user
    output = climage.convert("qrcode.png", is_unicode=True)
    print(output)

    print("Your secret key:", encoded_secret)

def get_otp():
    # filepath - path to qr code file

    while True:
        secret = input("scan or type: ")
        if secret == 'scan':
            # read qrcode file
            filepath = input("Path to qr code: ")
            uri = read_qrcode(filepath)
            secret = get_secret(uri)
            break
        elif secret == 'type':
            secret = input("Your secret key, please: ")
            break
        else:
            print(f"Your answer is incorrect: {secret}")

    totp = pyotp.TOTP(secret)
    print(totp.now())
    while True:
        print("Your 6 digit code:", totp.now())
        time.sleep(5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog = 'QR Code Checker/Generator',
                    description = 'Generate the code and check it'
    )
    
    parser.add_argument("--generate-qr", default=None)
    parser.add_argument("--get-otp", action="store_true")
    args = parser.parse_args()
    
    if args.generate_qr:
        generate_qr(args.generate_qr)
    elif args.get_otp:
        get_otp()
    else:
        print("Please choose: --generate-qr <name> or --get-otp")
