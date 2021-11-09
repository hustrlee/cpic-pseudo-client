const crypto = require("crypto");

const keyPlaintext = "gdtb";
const md5 = crypto.createHash("md5");
const key = md5.update(keyPlaintext).digest("hex");

// const jsonEncrypt =
//   "Rs4T2vERONt124afYt+Il/p/fsWkHQ5Gf/KP/xWt7t0/hAkvzAQcxUw4Zh3eXeT6RJbLWg6b93JLdzs7LaNJeE1haN28M2kpE5KKkBEnveTTWtguJZptCXX7yBkvWdYxOHnEZD/xa5t9rGFq6jZqyIJd2o2J8QMCKJd/qylPnyPAguKbvq56oOkwrm7QAyxrQckhSsOlc9DRAR6hdVNc0Nj/DhYYGRkU7X20Nv5CTLKR0GacRtpspIesYERODobVfMTeBqA1CGKXi6DatE5gz9kyhxup7eQ4+ThyWjzQz3ZIgjOF+5SEnqvaDmIIjUrEn1bkTAXWz/VHYQY+YZGYnW6uF64qoq8iignmn2OxwnuVBW9+zoraHzonwau+Ope2QeXDkie8M76fjc5Iz7/+dMK5OQflflZr7GAXmPjC20jYH1be5Mrg9I8pXY67vHAf3/7r6KJ8lWUnTMWJy5YbjApMqNC8gVWfu9e2jQzSdmA7DrX+TL4SxoNTGuYImWuNgeruTuS8AaM10KoQRcbdWMkzJah+0PLUQk/REBLPVXg=";
// const jsonEncrypt =
//   "hXlkhNJ+pXh2hRddTke8Z4hdFoHmeHOjMHIkBFqBnfWHPTRGsxjQeVGrRnm0GoemYtARREi7MGI+NGUt8N/ei+HGo3lKfPjQEPMoQIBUA2DlzRl56X1nYDADoehvHxwsqBGgKlwo8llwdKLIsk4gI56zQllyWoewkFXuXnXJvy9nYG5boAA7xdkraRqnmEgtZUAbBPMAYf1Wd03biZ7kuRrtNSVytJtsTZ7B33qVzvBU8I48L+qZcab5PdrML170Q2iNfx93Hb2mKagEU+EtPLYdr+ZrBNKsoFQKfhWpjXvs7dmQVKcXqRtQNxs2v2ZSn9lIae9qsHl+uEQkjqZSEudZ6ye6n49QCLIflBrPvOAmKg2Hu9UZhwUrNI6MHsasZ5A0GuBTa0jRgH9+NPdhRGuO+qCH/d6YfuJMz7fN7pJHY4aAr/otu1MwbjCXWFIMBbJKthODGm664klVfbyAGdrk01BQbqHIHPyyF71GLV/zC4PYmQXFKmw4vSMBoSMrABoF172Wx+ntsc7vmsRTrCLUrSpy5JiicTpVBYBHGfqsS4T1s/rkB2DeQsSYvmU07BI40EurLOfLoemFc4c29w==";
// const jsonEncrypt =
//   "hXlkhNJ+pXh2hRddTke8Z4hdFoHmeHOjMHIkBFqBnfWHPTRGsxjQeVGrRnm0GoemYtARREi7MGI+NGUt8N/ei+HGo3lKfPjQEPMoQIBUA2DlzRl56X1nYDADoehvHxwsqBGgKlwo8llwdKLIsk4gI56zQllyWoewkFXuXnXJvy9nYG5boAA7xdkraRqnmEgtZUAbBPMAYf1Wd03biZ7kuRrtNSVytJtsTZ7B33qVzvBU8I48L+qZcab5PdrML170Q2iNfx93Hb2mKagEU+EtPLYdr+ZrBNKsoFQKfhWpjXvs7dmQVKcXqRtQNxs2v2ZSn9lIae9qsHl+uEQkjqZSEudZ6ye6n49QCLIflBrPvOAmKg2Hu9UZhwUrNI6MHsasZ5A0GuBTa0jRgH9+NPdhRGuO+qCH/d6YfuJMz7fN7pJHY4aAr/otu1MwbjCXWFIMBbJKthODGm664klVfbyAGdrk01BQbqHIHPyyF71GLV/zC4PYmQXFKmw4vSMBoSMrABoF172Wx+ntsc7vmsRTrN4pvFNkAlQvjU0PFoQmwjqsS4T1s/rkB2DeQsSYvmU0EWIVp/rlGBNvWa5vg64MqHj3QM9SH4g4c3gk4PCYoqjeOdfaeoAU/8Vb9Gy0EV6byYTGYyxV6ukhTQcxsVt9PA==";
const jsonEncrypt =
  "uSIMxxgGa4o+O+A1MU26z82+xTiyVBXyVsSlHKsJ3j29WzpLy8NfGMvFf55GiYdM0UcCP7UvEKi2IFhvwBgxHC87Q1dbAPI4o4byihxw6oags/XKH7Uakh0meOfCeGOVUmiFuWoK8vmBycqH9PTqhxnqYqmVYKn6rUgBQGotlnoFeXt+9foiipO1PsP6affhjTZ3LpdNWQh0KfMuGkrnmiIBK3NftIXrBuHa1pTRDfg9r+t/dlCb+MR0Ae3AkMMVdzAj99fuyr78q761hixXVH2nVLsObNXNsBl4aC+5jyRptFxM+jZ46GXLycbfFbp+6JGpVGSrXIok5xHCKaaHK4CLyGK1kGakYJrA0j+kvBzB4/UhEOedF57aAH3ad73TRJSPYg2vtZlUybAtPzD6+b3aDQgBTI+vwFIFJiFbbsE137TO9WmX+h6+lS8clWNDm1cRIm4OJ433PiCg4cs+INoZPdHyyeqdLdthdYlj8bX5Nq5DZupU0R3ooyHxZsu+GiJ01XPtxh814uQuMaFBIse99UOKPCk/uqjC8fQTA5RgAkzxWm0xROzlsAJua3xdX40FXnU2jS0oFtFbPg+irUCqjCsl4B3eduYzEvBdLUo=";

const decipher = crypto.createDecipheriv("aes-256-ecb", key, "");
let jsonPlaintext = decipher.update(jsonEncrypt, "base64", "utf-8");
jsonPlaintext += decipher.final("utf-8");
console.log(JSON.parse(jsonPlaintext));
