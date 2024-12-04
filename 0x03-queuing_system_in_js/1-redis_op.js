import { createClient } from 'redis';
import redis from 'redis';

export const client = await createClient({
    url: 'redis://@localhost:6379'
})

client.on('error', err => console.log('Redis client not connected to the server', err));
client.on('connect', () => {
    console.log('Redis client connected to the server')
})

export function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) console.log(err);
        redis.print(`Reply: ${reply}`);
    })
}

export function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        if (err) console.log(err);
        console.log(reply);
    });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
