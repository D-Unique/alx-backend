import { createClient } from 'redis';

const client = createClient({
    url: 'redis://@localhost:6379'
});
client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => {
    console.log('Redis client connected to the server');
}
);

client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
    if ((channel === 'holberton school channel') && (message === 'KILL_SERVER')) {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
}
);



