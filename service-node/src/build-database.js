const pool = require("./common/db").pool;

(async () => {
  try {
    // 如果数据库存在，则先删除它，然后完全重建
    await pool.execute("DROP DATABASE IF EXISTS cpic_db");
    await pool.execute("CREATE DATABASE cpic_db");

    // 创建 customer 数据表
    await pool.execute(
      "CREATE TABLE `cpic_db`.`customer` \
      ( \
        `id` int NOT NULL AUTO_INCREMENT, \
        `custid` varchar(20) NOT NULL COMMENT '渠道用户代码', \
        `name` varchar(255) NOT NULL COMMENT '渠道用户名称', \
        `salt` varchar(255) NOT NULL COMMENT '加密密钥明文', \
        `appkey` varchar(255) NOT NULL COMMENT '渠道用户授权码', \
        `secretkey` varchar(255) NOT NULL COMMENT '渠道用户授权密钥', \
        PRIMARY KEY (`id`) \
      )"
    );

    // 插入广东太保的用户信息
    await pool.execute(
      "INSERT INTO `cpic_db`.`customer` (`custid`, `name`, `salt`, `appkey`, `secretkey`) VALUES (?, ?, ?, ?, ?)",
      ["21", "广东太保", "gdtb", "asdfghjkl", "dwsuhfci"]
    );

    // 创建 case 数据表
    await pool.execute(
      "CREATE TABLE `cpic_db`.`case` \
      ( \
        `case_no` varchar(255) NOT NULL COMMENT '案件号，由服务端生成，用于在识别流程中唯一标识该案件。', \
        `uuid` varchar(255) NOT NULL COMMENT '案件ID，由客户端生成，用于客户端唯一标识该案件', \
        `appkey` varchar(255) NOT NULL COMMENT '渠道用户授权码', \
        `insure_code` varchar(255) NULL COMMENT '被保险人身份证号', \
        `insure_name` varchar(255) NULL COMMENT '被保险人姓名', \
        `regist_no` varchar(255) NULL COMMENT '报案号', \
        `sign` varchar(255) NOT NULL COMMENT '签名，用于验证数据完整性', \
        `timestamp` datetime NOT NULL COMMENT '案件提交时间', \
        `weight` int NOT NULL DEFAULT 3 COMMENT '优先级，默认为3', \
        `zmark` varchar(255) NULL COMMENT '备注', \
        `images` json NULL COMMENT '原始图像列表', \
        PRIMARY KEY (`case_no`) \
      )"
    );
  } catch (err) {
    console.error(err.message);
  } finally {
    if (pool) {
      await pool.end();
    }
  }
})();
