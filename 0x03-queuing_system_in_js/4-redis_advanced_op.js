import { createClient, print } from 'redis';
import { promisify } from 'util'

const redisclient = createClient();

redisclient.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function hsetHolbertonSchools(key, data) {
  for (const [field, value] of Object.entries(data)) {
    redisclient.hset(key, field, value, print);
  }
};

const hgetallHolbertonSchools = async (schoolName) => {
  console.log(await promisify(redisclient.hgetall).bind(redisclient)(schoolName));
};

const data = {
	'Portland': 50,
	'Seattle': 80,
	'New York': 20,
	'Bogota': 20,
	'Cali': 40,
	'Paris': 2
}

async function main() {
  hsetHolbertonSchools('HolbertonSchools', data);
  await hgetallHolbertonSchools('HolbertonSchools');
}

redisclient.on('connect', async () => {
  await main();
});
