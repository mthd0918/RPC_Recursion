const net = require('net');
const readline = require('readline');
const serverAddress = '/tmp/socket_file';

const client = new net.Socket();

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const requests = [
    {
        "method": "floor",
        "params": [3.54],
        "param_types": ["double"],
        "id": 0
    },
    {
        "method": "nroot",
        "params": [2, 8],
        "param_types": ["int", "int"],
        "id": 1
    },
    {
        "method": "reverse",
        "params": ["yahoo"],
        "param_types": ["string"],
        "id": 2
    },
    {
        "method": "validAnagram",
        "params": ["abcba", "abcba"],
        "param_types": ["string", "string"],
        "id": 3
    },
    {
        "method": "sort",
        "params": ["dcba"],
        "param_types": ["string", "string"],
        "id": 4
    }
];

client.connect(serverAddress, () => {
    console.log('Connected to server');
    userInput();
});

function userInput() {
    rl.question('Please enter id (0 - 4) or type exit: ', (input) => {
        if (input === 'exit') {
            rl.close();
            client.end();
        } else if (requests[input]) {
            const message = requests[input];
            console.log('Sending message:', JSON.stringify(message, null, 2));
            client.write(JSON.stringify(message));
            userInput();
        } else {
            console.log('Invalid input. Please enter a number between 0 and 4.');
            userInput();
        }
    });
}

client.on('close', () => {
    console.log('connection closed');
})

client.on('error', (error) => {
    console.error('Socket error:', error);
});