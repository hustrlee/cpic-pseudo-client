const fs = require("fs");
const path = require("path");
const Minio = require("minio");
const { v1: uuidv1 } = require("uuid");

// 检查输入参数是否正确
let args = process.argv.slice(2);
if (args.length < 2) {
  console.log("Usage: node index.js <data directory> <minio server url>");
  process.exit(0);
}

// 检查 data directory 是否存在
try {
  let stat = fs.statSync(args[0]);
  if (stat.isDirectory()) {
    console.log("参数正确");
  } else {
    console.log("'%s' 不是目录。", args[0]);
  }
} catch (err) {
  console.log("目录 '%s' 不存在。", args[0]);
}

// 检查 minio server url 是否存在
const minioClient = new Minio.Client({
  endPoint: args[1],
  port: 9000,
  useSSL: false,
  accessKey: "minio",
  secretKey: "minio123",
});

(async () => {
  try {
    let res = await minioClient.bucketExists("cpic");
    if (!res) {
      await minioClient.makeBucket("cpic");
    }
  } catch (err) {
    console.log("无法连接 minio server。");
  }
})();
