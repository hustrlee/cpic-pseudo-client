const mysql = require("mysql2/promise");

const pool = mysql.createPool({
  host: "localhost",
  port: "3306",
  user: "cpic",
  password: "cpic",
  database: "cpic_db",
  charset: "utf8mb4",
});

process.on("exit", async () => {
  try {
    await pool.end();
  } catch (e) {}
});

module.exports = { pool };
