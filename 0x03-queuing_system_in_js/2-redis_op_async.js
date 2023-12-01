import { createClient, print } from 'redis';
import { promisify } from 'util'

const redisclient = createClient();

redisclient.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  redisclient.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(redisclient.get).bind(redisclient)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

redisclient.on('connect', async () => {
  console.log("Redis client connected to the server");
  await main();
});
