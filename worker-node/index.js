const amqp = require("amqplib");

(async () => {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertQueue("case_queue", { durable: true });
  await channel.prefetch(1);

  await channel.consume(
    "case_queue",
    (msg) => {
      let caseDetail = JSON.parse(msg.content.toString());
      console.log(caseDetail.caseInfo.images);
      channel.ack(msg);
    },
    { noAck: false }
  );
})();
