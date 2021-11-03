var request = require('request');
var EventProxy = require('eventproxy');
var settings = require('../../settings.js');
var db = require('../libs/mysql');
var logger = require('../../logs/logger');
var errMsg = require('../libs/errors');
var common = require("../libs/common");

exports.GetApi = function(_req, _res, _callback,_senderror) {
    return {
        req: _req,
        res: _res,
        cb: _callback,
        err:_senderror,
        getParam: function(param, _code) {
            var code = _code || 4041;
            if (typeof(_req.query[param]) === "undefined" && typeof(_req.body[param]) === "undefined")
                throw code;
            else if (!_req.query[param])
                return _req.body[param];
            else
                return _req.query[param];
        },
        createCase:function(){
            var Me = this;
            var custid = this.getParam("custid");
            var tokenStr = this.getParam("token");
            var uuid = this.getParam("uuid");
            var token = "";

            var secretkey = 'dwsuhfci';

            //1.查询custid是否存在，并且appkey和盐值
            // TODO: 判定账号有效性
            // TODO: 判定uuid唯一性
            //查询返回appkey和salt
            /*{
                custid:21,
                salt:'gdtb',
                appkey:'asdfghjkl',
                secretkey:'dwsuhfci'
            }*/

            if(custid != 21){
                return Me.sendError(4001,"用户有误");
            }

            //通过appkey计算token
            token = common.checkToken(tokenStr,'gdtb');

            if(token == ""){
                //TODO 修正返回结果
                return Me.sendError(4002,"token异常");
            }

            if(token.appkey != 'asdfghjkl'){
                return Me.sendError(4003,"授权错误");
            }
            //通过token计算sign是否合法。
            var sign = common.md5(token.appkey + token.registno + token.timestamp + uuid + secretkey)
            console.log(token.appkey + token.registno + token.timestamp + uuid + secretkey);
            if(sign != token.sign){
                console.log(sign,token.sign);
                return Me.sendError(4004,"签名有误");
            }

            // 判断timestamp与服务器时间是否差距过大？
            // 判断uuid是否有重复
            // 判断身份证号是否合法
            // 判断照片id是否有重复

            
            // return Me.res.send(tokenObj);

            //写数据库，返回caseno

            var imagecount = token.images ? token.images.length : 0;
            var sqlCmd = "insert into cases(uuid,custid,registno,imagecount,insurecode,insurename,uploadtime,weight) values (?,?,?,?,?,?,?,?);";
            var sqlParams = [uuid,custid,token.registno,imagecount,token.insurecode,token.insurename,token.timestamp,token.weight];
            db.query(sqlCmd,sqlParams,function(err,result){
                console.log(err,result);
                var caseno = result.insertId;
                var sqlCmd_caseinfo = "insert into caseinfo(caseno,images,zmark) values (?,?,?)";
                var sqlParams_caseinfo = [caseno,JSON.stringify(token.images),JSON.stringify(token.zmark)];
                db.query(sqlCmd_caseinfo,sqlParams_caseinfo,function(err_caseinfo,result_caseinfo){
                    console.log(err_caseinfo,result_caseinfo);
                    return Me.res.send({"code":200,"msg":"success","data":caseno});
                });
            });
        },
        test:function(){
            var Me = this;
            var token = {
                appkey:'asdfghjkl',
                images:[
                    {
                        id:'101',
                        name:'567b6bfd24d0c.jpg_e1080.jpg',
                        url:'https://am.zdmimg.com/201512/24/567b6bfd24d0c.jpg_e1080.jpg'
                    },
                    {
                        id:'102',
                        name:'56ac538d7d464.png_fo742.jpg',
                        url:'https://am.zdmimg.com/201601/30/56ac538d7d464.png_fo742.jpg'
                    }
                ],
                insurecode:'130701199310302288',
                insurename:'张三',
                registno:'XDX202007190002',
                timestamp:'2021-08-21 14:25:36',
                weight:'3',
                zmark:''
            }

            var uuid = 'ef30e1ca-9888-451d-a328-08bfc6a7d482';
            var secretkey = 'dwsuhfci';
            console.log('base',token.appkey + token.registno + token.timestamp + uuid + secretkey);
            var sign = common.md5(token.appkey + token.registno + token.timestamp + uuid + secretkey)//"123";

            console.log('sign',sign);

            token.sign = sign;
            
            var tokenStr = common.createToken(token,'gdtb');

            return Me.res.send(tokenStr);
        },

        sendError:function(code,msg){
            var Me = this;
            return Me.res.send({"code":code,"msg":msg,"data":""});
        }
    }
};