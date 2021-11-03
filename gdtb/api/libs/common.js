(function() {
    var common;
    var crypto = require('crypto');

    var aesutil = module.exports = {};

    /**
     * aes加密
     * @param data 待加密内容
     * @param key 必须为32位私钥
     * @returns {string}
     */
    aesutil.encryption = function (data, key, iv) {
        iv = iv || "";
        var clearEncoding = 'utf8';
        var cipherEncoding = 'base64';
        var cipherChunks = [];
        var cipher = crypto.createCipheriv('aes-256-ecb', key, iv);
        cipher.setAutoPadding(true);
        cipherChunks.push(cipher.update(data, clearEncoding, cipherEncoding));
        cipherChunks.push(cipher.final(cipherEncoding));
        return cipherChunks.join('');
    }

    /**
     * aes解密
     * @param data 待解密内容
     * @param key 必须为32位私钥
     * @returns {string}
     */
    aesutil.decryption = function (data, key, iv) {
        if (!data) {
            return "";
        }
        iv = iv || "";
        var clearEncoding = 'utf8';
        var cipherEncoding = 'base64';
        var cipherChunks = [];
        var decipher = crypto.createDecipheriv('aes-256-ecb', key, iv);
        decipher.setAutoPadding(true);
        cipherChunks.push(decipher.update(data, cipherEncoding, clearEncoding));
        cipherChunks.push(decipher.final(clearEncoding));
        return cipherChunks.join('');
    }

    common = {
        checkToken:function(token,salt){
            var jsonStr = aesutil.decryption(token,crypto.createHash('md5').update(salt).digest("hex"),"");
            try{
                return JSON.parse(jsonStr);
            } catch (err){
                console.log('checkToken err');
                return "";
            }
        },
        createToken:function(token,salt){
            return aesutil.encryption(JSON.stringify(token),crypto.createHash('md5').update(salt).digest("hex"),"");
        },
        aesutil:aesutil,
        md5:function(str){
            return crypto.createHash('md5').update(str).digest("hex");
        }
    };

    module.exports = common;

}).call(this);
