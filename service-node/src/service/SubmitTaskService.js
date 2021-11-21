"use strict";

const { v1: uuidv1 } = require("uuid");

const sign = require("../common/sign").sign;
const pool = require("../common/db").pool;
const aesEcb = require("../common/aes-ecb");
const MQ = require("../common/mq");
const mq = new MQ();

const respondWithCode = require("../utils/writer").respondWithCode;

/**
 * 用于接收渠道推送的案件信息
 *
 * body CreateCaseDto  (optional)
 * returns CreateCaseResDto
 **/
exports.createCase = function (body) {
  return new Promise(async (resolve, reject) => {
    // 获取加密参数
    var custParam = {};
    try {
      let [rows, fields] = await pool.execute(
        "SELECT * FROM `customer` WHERE `custid` = ? LIMIT 1",
        [body.custid]
      );
      if (rows.length == 0) {
        return resolve({ code: 401, msg: "custid 或 appkey 错误。" });
      }
      custParam = rows[0];
    } catch (err) {
      console.error("\x1b[31m" + err.message);
      return resolve(
        respondWithCode(500, { message: "database failed to connect" })
      );
    }

    // 解码 token
    try {
      var caseInfo = JSON.parse(aesEcb.decrypt(custParam.salt, body.token));
    } catch (err) {
      console.error("\x1b[31m" + "AES 解码错误：" + err.message);
      return resolve({ code: 403, msg: "无效的 token。" });
    }

    // 校验客户 appkey 是否正确
    if (caseInfo.appkey != custParam.appkey) {
      return resolve({ code: 401, msg: "custid 或 appkey 错误。" });
    }

    // 校验 sign 是否正确
    var signature = sign([
      caseInfo.appkey,
      caseInfo.registno,
      caseInfo.timestamp,
      body.uuid,
      custParam.secretkey,
    ]);
    if (caseInfo.sign != signature) {
      return resolve({ code: 403, msg: "无效的 sign。" });
    }

    // 生成 caseNo
    var caseNo = uuidv1();

    // 将任务保存到数据库
    try {
      await pool.execute(
        "INSERT INTO `case` ( \
          case_no, \
          uuid, \
          appkey, \
          insure_code, \
          insure_name, \
          regist_no, \
          sign, \
          timestamp, \
          weight, \
          zmark, \
          images \
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
          caseNo,
          body.uuid,
          caseInfo.appkey,
          caseInfo.insurecode,
          caseInfo.insurename,
          caseInfo.registno,
          caseInfo.sign,
          caseInfo.timestamp,
          caseInfo.weight,
          caseInfo.zmark,
          caseInfo.images,
        ]
      );
    } catch (err) {
      console.error("\x1b[31m" + err.message);
      return resolve(
        respondWithCode(500, { message: "database failed to connect" })
      );
    }

    // 将任务推送到 MQ
    await mq.publish(JSON.stringify({ caseNo, uuid: body.uuid, caseInfo }));

    // 检查是否需要返回 caseInfo
    if (body.withCaseInfoInReturn) {
      resolve({ code: 200, data: { caseNo, caseInfo } });
    } else {
      resolve({ code: 200, data: { caseNo } });
    }
  });
};
