const net = require('net');
const readline = require('readline');
const serverAddress = '/tmp/socket_file';

const client = new net.Socket();

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

requests = [
    {
        "method": "floor",
        "params": 3.54,
        "param_types": "double",
        "id": 1
    }, {
        "method": "nroot",
        "params": [2, 8],
        "param_types": "int",
        "id": 2
    },
    , {
        "method": "reverse",
        "params": "yahoo",
        "param_types": "string",
        "id": 3
    },
    , {
        "method": "validAnagram",
        "params": "[]",
        "param_types": "[string, string]",
        "id": 4
    },
    , {
        "method": "sort",
        "params": "[anagram, nagaram]",
        "param_types": "[string, string]",
        "id": 5
    },
];

client.connect(serverAddress, () => {
    console.log('Connected to server');
    userInput();
});

function userInput() {
    rl.question('Please enter id (1 - 6): ', (input) => {
        if (input === 'exit') {
            rl.close();
        } else {
            const message = requests[input];
            console.log(`Sended massage: ` + input);
            client.write(JSON.stringify(message))
            userInput();
        }
    });
}

userInput();


client.on('close', () => {
    console.log('connection closed');
})

client.on('error', (error) => {
    console.error('Socket error:', error);
});