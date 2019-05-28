function generateSensorReading(){
    const temperature = (Math.random()*20) -5;
    process.stdout.write(temperature + '\n');
    setTimeout(generateSensorReading,Math.random()*5000);
}

generateSensorReading();