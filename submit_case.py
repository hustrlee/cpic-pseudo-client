import logging
from urllib import request, parse
import json
import time
from aes_ecb import AESCipher
from hashlib import md5

# 分配给广东太保的用户参数
gdtb = {
    "custid": 21,
    "appkey": "asdfghjkl",
    "secretkey": "dwsuhfci",
    "salt": "gdtb",
}

# Payload
token = {
    "appkey": gdtb["appkey"],
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
    # "timestamp": "2021-08-21 14:25:36",
    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    "weight": "3",
    "zmark": "",
}

# 测试时，uuid 固定为 ef30e1ca-9888-451d-a328-08bfc6a7d482
uuid = "ef30e1ca-9888-451d-a328-08bfc6a7d482"

# 生成签名 sign
sign_md5 = md5()
sign_md5.update(token["appkey"].encode("utf-8"))
sign_md5.update(token["registno"].encode("utf-8"))
sign_md5.update(token["timestamp"].encode("utf-8"))
sign_md5.update(uuid.encode("utf-8"))
sign_md5.update(gdtb["secretkey"].encode("utf-8"))
token["sign"] = sign_md5.hexdigest()

# 对 Payload 进行加密
token_cipher = AESCipher(gdtb["salt"]).encrypt(json.dumps(token))

# POST /api/createCase
# request_body = json.dumps({
#     "custid": 21,
#     "uuid": "ef30e1ca-9888-451d-a328-08bfc6a7d482",
#     "token": "uSIMxxgGa4o+O+A1MU26z82+xTiyVBXyVsSlHKsJ3j29WzpLy8NfGMvFf55GiYdM0UcCP7UvEKi2IFhvwBgxHC87Q1dbAPI4o4byihxw6oags/XKH7Uakh0meOfCeGOVUmiFuWoK8vmBycqH9PTqhxnqYqmVYKn6rUgBQGotlnoFeXt+9foiipO1PsP6affhjTZ3LpdNWQh0KfMuGkrnmiIBK3NftIXrBuHa1pTRDfg9r+t/dlCb+MR0Ae3AkMMVdzAj99fuyr78q761hixXVH2nVLsObNXNsBl4aC+5jyRptFxM+jZ46GXLycbfFbp+6JGpVGSrXIok5xHCKaaHK4CLyGK1kGakYJrA0j+kvBzB4/UhEOedF57aAH3ad73TRJSPYg2vtZlUybAtPzD6+b3aDQgBTI+vwFIFJiFbbsE137TO9WmX+h6+lS8clWNDm1cRIm4OJ433PiCg4cs+INoZPdHyyeqdLdthdYlj8bX5Nq5DZupU0R3ooyHxZsu+GiJ01XPtxh814uQuMaFBIse99UOKPCk/uqjC8fQTA5RgAkzxWm0xROzlsAJua3xdX40FXnU2jS0oFtFbPg+irUCqjCsl4B3eduYzEvBdLUo="
# })
# headers = {"content-type": "application/json"}
# req = request.Request(
#     url="http://localhost:3000/createCase",
#     headers=headers,
#     data=request_body.encode("utf-8")
# )

# GET /api/createCase
params = parse.urlencode({
    "custid": gdtb["custid"],
    "uuid": uuid,
    "token": token_cipher
})
req = request.Request(
    url="http://localhost:3000/api/createCase?" + params
)

try:
    res = request.urlopen(req)
    print(res.read().decode("utf-8"))
except Exception as e:
    logging.error(e)
