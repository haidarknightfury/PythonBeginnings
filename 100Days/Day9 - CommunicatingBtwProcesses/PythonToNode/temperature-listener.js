const {spawn} = require('child_process');
const temperature = [];

const sensor = spawn('python', ['sensor.py']);
sensor.stdout.on('data', (data) => {
    temperature.push(parseFloat(data));
    console.log(temperature);
});