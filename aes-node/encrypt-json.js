const crypto = require("crypto");

const keyPlaintext = "hcxw";
const md5 = crypto.createHash("md5");
const key = md5.update(keyPlaintext).digest("hex");

const json = {
  appkey: "asdfghjkl",
  images: [
    {
      id: "101",
      name: "567b6bfd24d0c.jpg_e1080.jpg",
      url: "https://am.zdmimg.com/201512/24/567b6bfd24d0c.jpg_e1080.jpg",
    },
    {
      id: "102",
      name: "56ac538d7d464.png_fo742.jpg",
      url: "https://am.zdmimg.com/201601/30/56ac538d7d464.png_fo742.jpg",
    },
  ],
  insurecode: "130701199310302288",
  insurename: "张三",
  registno: "XDX202007190002",
  timestamp: "2021-08-21 14:25:36",
  weight: "3",
  zmark: "",
};
console.log(JSON.stringify(json));

const cipher = crypto.createCipheriv("aes-256-ecb", key, "");
let ciphertext = cipher.update(JSON.stringify(json), "utf-8", "base64");
ciphertext += cipher.final("base64");

console.log(ciphertext);
