var log4js = require('log4js');
var settings = require("../settings.js");
log4js.configure(settings.log4js.configure);

var logger = {}
for (let key in settings.log4js.configure.categories) {
    logger[key] = log4js.getLogger(key)
}
 
/**
 * 返回一个log4js.logger，可直接用于写入log信息
 * @param {string} categories
 * @returns {object} logger
 */
exports.get = function(categories){ // categories
    if(typeof (settings.log4js.configure.categories[categories]) == "undefined")
        return logger["default"];
    return logger[categories];
};

exports.use = function(app) {
    for (let key in settings.log4js.configure.categories) {
        app.use(log4js.connectLogger(logger[key]));
    }
}