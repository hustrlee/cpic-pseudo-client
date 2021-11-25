const axios = require("axios");
const Minio = require("minio");

(async () => {
  const minioClient = new Minio.Client({
    endPoint: "localhost",
    port: 9000,
    useSSL: false,
    accessKey: "minio",
    secretKey: "minio123",
  });

  if (!(await minioClient.bucketExists("cases"))) {
    await minioClient.makeBucket("cases", "us-ease-1");
  }

  let res = await axios({
    method: "get",
    url: "http://localhost:9000/temp/57b3ffb4-4c65-11ec-8c96-da1069ae0616/IMG_001.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20211123%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20211123T135748Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=533ad8aee3c4979142d0233bd85188a741adc4891e7dac262deaa0ac513040ac",
    responseType: "stream",
  });

  await minioClient.putObject("cases", "1.jpg", res.data);
})();
