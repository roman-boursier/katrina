const http = require('http');
const path = require("path");
const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const {spawn} = require('child_process');

var server = http.Server(app);

app.use(bodyParser.urlencoded({ extended: true }));


app.get('/index', (req, res) => {
    res.sendFile(__dirname + '/index.html');
})

app.get('/app.js',function(req,res){
    res.sendFile(path.join(__dirname + '/app.js'));
});

app.post('/handlePost',function(request,response) {
    base64Img = request.body.datas
    const python = spawn('python3', ['katrina.py', base64Img]);

    python.stdout.on('data', function (data) {
        console.log('Pipe data from python script ...');
        dataToSend = data.toString();
    });

    python.on('close', (code) => {
        console.log(`child process close all stdio with code ${code}`);
        response.send(dataToSend);
    });
});


server.listen(8080, () => {
    console.log('Express lancé')
})
