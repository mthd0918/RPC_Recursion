const net = require('net');

const serverAddress = '/tmp/socket_file';

console.log(`Connecting to ${serverAddress}`);

const client = net.createConnection({ path: serverAddress }, () => {
    console.log('Connected to server');

    const message = Buffer.from('Sending a message to the server side');
    client.write(message);
});

client.on('data', (data) => {
    console.log('Server response: ' + data.toString());
});

client.on('end', () => {
    console.log('Disconnected from server');
});

client.on('error', (err) => {
    console.error('Error: ', err.message);

});

setTimeout(() => {
    console.log('Socket time out, ending listeninig for server message');
    client.end();
}, 2000);

process.on('SGINT', () => {
    console.log('Closing socket');
    client.end();
    process.exit(0);
});