import { createClient } from "redis";
const redis = require("redis")
const redisclient = createClient();

(async () => {
  try {
    await redisclient.connect();
  } catch (err) {}
})();

redisclient.on("ready", () => {
    console.log("Redis client connected to the server");
});

redisclient.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  redisclient.on('ready', () => {
    redisclient.set(schoolName, value, redis.print);
  });
};

function displaySchoolValue(schoolName) {
  redisclient.on('ready', () => {
    redisclient.get(schoolName, (err, value) => {
      console.log(value);
    });
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
