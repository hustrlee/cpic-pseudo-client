const aesEcb = require("aes-ecb");

// key_plaintext = "1234"
// msg_plaintext = "Ryan，你好！"
plaintext = aesEcb.decrypt(
  "81dc9bdb52d04dc20036dbd8313ed055",
  "E7chJzwwyUY4E0xjys0J3aNqrGDW7D2VG7pVVbLROgQ="
);

console.log(plaintext);
