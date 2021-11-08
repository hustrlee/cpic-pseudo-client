const crypto = require("crypto");

const keyPlaintext = "1234";
const msg = "Ryan，你好！";

const md5 = crypto.createHash("md5");
const key = md5.update(keyPlaintext).digest("hex");
console.log("key:", key);

const cipher = crypto.createCipheriv("aes-256-ecb", key, "");
let ciphertext = cipher.update(msg, "utf-8", "base64");
ciphertext = ciphertext + cipher.final("base64");

console.log("ciphertext:", ciphertext);
