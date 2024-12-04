import { createClient } from 'redis';
import redis from 'redis';
import util from 'util';

const client = createClient({
    url: 'redis://@localhost:6379'
})

client.on('error', err => console.log('Redis client not connected to the server', err));
client.on('connect', () => {
console.log('Redis client connected to the server')
})

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) console.log(err);
        redis.print(`Reply: ${reply}`);
    })
}
const asyncRedisGet = util.promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
    try {
        const value = await asyncRedisGet(schoolName);
        console.log(value);
    }
    catch (error) {
        console.log(error);
    }
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
