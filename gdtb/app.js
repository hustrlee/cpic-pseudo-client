(function() {
    var app, cluster, express, session, http, i, numCPUs, path, routes, settings, os, _i, ipaddress,logger,applogger;
    express = require('express');
    session = require('express-session');
    routes = require('./routes/routes');
    http = require('http');
    path = require('path');
    cluster = require('cluster');
    settings = require('./settings.js');
    numCPUs = 1;//require('os').cpus().length;
    logger = require('./logs/logger'); // 新增logger引入

    // https
    /*
    var https = require('https');
    var fs = require('fs');
    //同步读取密钥和签名证书
    var options = {
        key:fs.readFileSync('./keys/server.key'),
        cert:fs.readFileSync('./keys/server.crt')
    }

    */
    
    if (cluster.isMaster) {
        console.log('master');
        for (i = _i = 0; 0 <= numCPUs ? _i < numCPUs : _i > numCPUs; i = 0 <= numCPUs ? ++_i : --_i) {
            cluster.fork();
        }
        cluster.on('exit', function(worker) {
            console.log('Worker ' + worker.id + ' died :(');
            return cluster.fork();
        });
    } else {
        app = express();
        app.set('port', settings.serverPort);
        app.set('views', __dirname + '/views');
        app.set('view engine', 'html');

        var bodyParser = require('body-parser');
        var cookieParser = require('cookie-parser');
        app.use(bodyParser.json({limit: '50mb'}));
        app.use(bodyParser.urlencoded({limit: '50mb', extended: true, parameterLimit:50000}));
        app.use(cookieParser());
        app.use(express["static"](path.join(__dirname, 'web')));
        app.use(session({ secret: settings.cookie_secret }));
        
        logger.use(app);
        routes(app);

        function errorHandler(err, req, res, next) {
            // console.log(req.protocol + '://' + req.get('host') + req.originalUrl);
            if(err){
                console.error(err.stack);
                applogger = logger.get("applogger");
                applogger.error({name:"10000",url:req.originalUrl,message:err.stack});//记录接口调用记录
                return res.send("接口异常");
            } else {
                next();
            }
        }
            
        app.use(errorHandler);

        http.createServer(app).setTimeout(0).listen(app.get('port'), function() {
            var consoleDay = new Date();
            var consoleDayStr = consoleDay.getFullYear() + '-' + (consoleDay.getMonth() + 1) + '-' +
                consoleDay.getDate() + ' ' + consoleDay.getHours() + ":" +
                consoleDay.getMinutes() + ":" + consoleDay.getSeconds();
            return console.log('Http服务器启动 - 端口:[' + app.get('port') + '] 时间:[' + consoleDayStr + ']');
        });

        // https
        /*
        https.createServer(options,app).setTimeout(0).listen(443, function() {
            var consoleDay = new Date();
            var consoleDayStr = consoleDay.getFullYear() + '-' + (consoleDay.getMonth() + 1) + '-' +
                consoleDay.getDate() + ' ' + consoleDay.getHours() + ":" +
                consoleDay.getMinutes() + ":" + consoleDay.getSeconds();
            return console.log('Https服务器启动 - 端口:[' + 443 + '] 时间:[' + consoleDayStr + ']');
        });
        */
    }
}).call(this);