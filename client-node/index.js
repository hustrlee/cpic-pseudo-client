const fs = require("fs");
const path = require("path");
const Minio = require("minio");
const { v1: uuidv1 } = require("uuid");

// 检查输入参数是否正确
let args = process.argv.slice(2);
if (args.length < 2) {
  console.log("Usage: node index.js <data directory> <minio server url>");
  process.exit(-1);
}

// 检查 data directory 是否存在
try {
  let stat = fs.statSync(args[0]);
  if (!stat.isDirectory()) {
    console.log("'%s' 不是目录。", args[0]);
    process.exit(-1);
  }
} catch (err) {
  console.log("目录 '%s' 不存在。", args[0]);
  process.exit(-1);
}

const walkdir = (dir) => {
  const IMG_FILE_EXT = ["jpg", "jpeg", "png"];
  let images = [];

  for (f of fs.readdirSync(dir, { withFileTypes: true })) {
    if ()
  }
};

(async () => {
  // 检查 minio server url 是否有效，并创建桶
  const minioClient = new Minio.Client({
    endPoint: args[1],
    port: 9000,
    useSSL: false,
    accessKey: "minio",
    secretKey: "minio123",
  });

  try {
    let res = await minioClient.bucketExists("cpic");
    if (!res) {
      await minioClient.makeBucket("cpic");
    }
  } catch (err) {
    console.log("无法连接 minio server。");
    process.exit(-1);
  }

  // 列出 <data directory> 下的一级子目录
  let subdirs = [];
  fs.readdirSync(args[0], { withFileTypes: true }).forEach((val) => {
    if (val.isDirectory()) {
      subdirs.push(val.name);
    }
  });

  // 遍历每个子目录下的所有图像文件
  for (let dir of subdirs) {
  }
})();
