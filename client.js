const net = require('net');
const readline = require('readline');
const serverAddress = '/tmp/socket_file';

const client = new net.Socket();

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

client.connect(serverAddress, () => {
    console.log('Connected to server');
    userInput();
});

function userInput(question) {
    rl.question('Please enter message: ', (input) => {
        if (input === 'exit') {
            rl.close();
        } else {
            const message = input;
            console.log(`Sended massage: ` + input);
            client.write(JSON.stringify(message))
            userInput();
        }
    });
}

userInput()

client.on('error', (error) => {
    console.error('Socket error:', error);
});

process.on('SIGINT', () => {
    console.log('Closing client...');
    client.end();
    process.exit();
});