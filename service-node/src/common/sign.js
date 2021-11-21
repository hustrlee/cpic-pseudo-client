const Crypto = require("crypto");

const sign = (seq) => {
  const md5 = Crypto.createHash("md5");

  seq.forEach((val, index) => {
    md5.update(val);
  });
  return md5.digest("hex");
};

module.exports = { sign };
