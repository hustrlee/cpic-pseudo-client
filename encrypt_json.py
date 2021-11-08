from aes_ecb import AESCipher
import json

if __name__ == "__main__":
    token = {
        "appkey": "asdfghjkl",
        "images": [
            {
                "id": "101",
                "name": "567b6bfd24d0c.jpg_e1080.jpg",
                "url": "https://am.zdmimg.com/201512/24/567b6bfd24d0c.jpg_e1080.jpg",
            },
            {
                "id": "102",
                "name": "56ac538d7d464.png_fo742.jpg",
                "url": "https://am.zdmimg.com/201601/30/56ac538d7d464.png_fo742.jpg",
            },
        ],
        "insurecode": "130701199310302288",
        "insurename": "张三",
        "registno": "XDX202007190002",
        "timestamp": "2021-08-21 14:25:36",
        "weight": "3",
        "zmark": "",
    }
    print(json.dumps(token))
    print(AESCipher("hcxw").encrypt(json.dumps(token)))
