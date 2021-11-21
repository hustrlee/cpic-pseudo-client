const MQ = require("./mq");

(async () => {
  const mq = new MQ();
  // await mq.init();
  await mq.publish("Hello World!!! Again!!");
  await mq.destroy();
  console.log("end");
})();
