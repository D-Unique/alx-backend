import { createClient } from 'redis';
import redis from 'redis';

const client = await createClient({
    url: 'redis://@localhost:6379'
})

client.on('error', err => console.log('Redis client not connected to the server', err));
client.on('connect', () => {
    console.log('Redis client connected to the server')
})
const data = {
    'Portland': '50',
    'Seattle': '80',
    'New York': '20',
    'Bogota': '20',
    'Cali': '40',
    'Paris': '2'
};
client.del('HolbertonSchools');
for (const [key, value] of Object.entries(data)) {
    client.hset('HolbertonSchools', key, value, (err, reply) => {
        if (err) redis.print(err);
        redis.print(`Reply: ${reply}`);
    });
}
client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) redis.print(err);
    console.log(reply);
   
});


