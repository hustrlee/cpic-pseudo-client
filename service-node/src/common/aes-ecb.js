const Crypto = require("crypto");

const encrypt = (key, msg) => {
  const md5 = Crypto.createHash("md5");
  const k = md5.update(key).digest("hex");

  const cipher = Crypto.createCipheriv("aes-256-ecb", k, "");
  let c = cipher.update(msg, "utf-8", "base64");
  c += cipher.final("base64");

  return c;
};

const decrypt = (key, cipher) => {
  const md5 = Crypto.createHash("md5");
  const k = md5.update(key).digest("hex");

  const decipher = Crypto.createDecipheriv("aes-256-ecb", k, "");
  let m = decipher.update(cipher, "base64", "utf-8");
  m += decipher.final("utf-8");

  return m;
};

module.exports = {
  encrypt,
  decrypt,
};
