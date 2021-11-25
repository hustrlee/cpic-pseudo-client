const amqp = require("amqplib");
const axios = require("axios");
const Minio = require("minio");

const minioClient = new Minio.Client({
  endPoint: "localhost",
  port: 9000,
  useSSL: false,
  accessKey: "minio",
  secretKey: "minio123",
});

(async () => {
  if (!minioClient.bucketExists("cases")) {
    minioClient.makeBucket("cases");
  }

  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertQueue("case_queue", { durable: true });
  await channel.prefetch(1);

  await channel.consume(
    "case_queue",
    async (msg) => {
      // 获取案件信息
      let caseDetail = JSON.parse(msg.content.toString());

      // 将图片上传到 cases 桶
      for (image of caseDetail.caseInfo.images) {
        let imageStream = await axios({
          method: "get",
          url: image.url,
          responseType: "stream",
        });

        await minioClient.putObject(
          "cases",
          `${caseDetail.caseNo}/${image.name}`,
          imageStream.data
        );

        // 更新 URL
        image.url = await minioClient.presignedUrl(
          "GET",
          "cases",
          `${caseDetail.caseNo}/${image.name}`
        );
      }

      // 启动 camunda process
      console.log(caseDetail);

      // 向 MQ 确认本消息已经处理完毕
      channel.ack(msg);
    },
    { noAck: false }
  );
})();
