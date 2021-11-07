import json
from urllib import request, parse
import logging

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
    "custid": 21,
    "uuid": "ef30e1ca-9888-451d-a328-08bfc6a7d482",
    "token": "uSIMxxgGa4o+O+A1MU26z82+xTiyVBXyVsSlHKsJ3j29WzpLy8NfGMvFf55GiYdM0UcCP7UvEKi2IFhvwBgxHC87Q1dbAPI4o4byihxw6oags/XKH7Uakh0meOfCeGOVUmiFuWoK8vmBycqH9PTqhxnqYqmVYKn6rUgBQGotlnoFeXt+9foiipO1PsP6affhjTZ3LpdNWQh0KfMuGkrnmiIBK3NftIXrBuHa1pTRDfg9r+t/dlCb+MR0Ae3AkMMVdzAj99fuyr78q761hixXVH2nVLsObNXNsBl4aC+5jyRptFxM+jZ46GXLycbfFbp+6JGpVGSrXIok5xHCKaaHK4CLyGK1kGakYJrA0j+kvBzB4/UhEOedF57aAH3ad73TRJSPYg2vtZlUybAtPzD6+b3aDQgBTI+vwFIFJiFbbsE137TO9WmX+h6+lS8clWNDm1cRIm4OJ433PiCg4cs+INoZPdHyyeqdLdthdYlj8bX5Nq5DZupU0R3ooyHxZsu+GiJ01XPtxh814uQuMaFBIse99UOKPCk/uqjC8fQTA5RgAkzxWm0xROzlsAJua3xdX40FXnU2jS0oFtFbPg+irUCqjCsl4B3eduYzEvBdLUo="
})
req = request.Request(
    url="http://localhost:3000/api/createCase?" + params
)

try:
    res = request.urlopen(req)
    print(res.read().decode("utf-8"))
except Exception as e:
    logging.error(e)
