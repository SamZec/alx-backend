import { createClient } from "redis";
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
