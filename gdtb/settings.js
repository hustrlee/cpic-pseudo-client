(function() {
    module.exports = {
        cookie_secret: 'secret_gdtb',
        serverPort: 3000,
        log4js:{
            configure:{
                appenders: { 
                    // appenders是记录的类型
                    default: { type: 'console' } 
                    ,applogger: { type: "file", filename: "./logs/applogger.log",maxLogSize: 1024*1024*10,backups:10 }//1024byte*1024*10 = 10MB

                },
                categories: { 
                     // 本例中我选择同时使用​
                    default: { appenders: ["default"], level: "info" }
                    ,applogger: { appenders: ["applogger"], level: "error" }
                }
            }
        },
        mysql: {
            database: 'gdtb',
            host: '192.168.1.205',
            user: 'root',
            password: 'ipcamera',
            port: 3307,
            multipleStatements: true
        },
        s3:{
            //s3服务器的地址配置
            server:{
                apiVersion: '2006-03-01',
                accessKeyId: "minioadmin",
                secretAccessKey: "minioadmin",
                endpoint: "192.168.1.1:9000",
                s3ForcePathStyle: true,
                signatureVersion: 'v4',
                sslEnabled: false
            },
            bucket:"s3bucket" //图片存储的桶名
        }
    };
}).call(this);