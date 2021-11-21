const amqp = require("amqplib");

var RabbitMQ = function () {
  this.connection = null;
  this.channel = null;
};

RabbitMQ.prototype.init = async function () {
  try {
    this.connection = await amqp.connect("amqp://localhost");
    this.channel = await this.connection.createChannel();
    await this.channel.assertExchange("case_exchange", "fanout", {
      durable: true,
    });
    await this.channel.assertQueue("case_queue", { durable: true });
    await this.channel.bindQueue("case_queue", "case_exchange", "");
  } catch (err) {
    this.connection = null;
    this.channel = null;
    console.error("\x1b[31m%s\x1b[0m", err.message);
  }
};

RabbitMQ.prototype._publish = async function (msg) {
  await this.channel.publish("case_exchange", "", Buffer.from(msg), {
    persistent: true,
  });
};

RabbitMQ.prototype.publish = async function (msg) {
  try {
    await this._publish(msg);
  } catch (err) {
    await this.init();
    if (this.channel) {
      await this._publish(msg);
    }
  }
};

RabbitMQ.prototype.destroy = async function () {
  if (this.connection) {
    // 关闭连接前，延时 500ms
    await new Promise((resolve) => {
      setTimeout(() => {
        resolve();
      }, 500);
    });
    await this.connection.close();
  }
};

module.exports = RabbitMQ;
