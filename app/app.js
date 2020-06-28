canvas = document.getElementById('canvas');
context = canvas.getContext("2d");

drawing = false;
startsX = [];
startsY = [];
moves = [];

$('#canvas').mousedown(onMouseDown);
$('#canvas').mousemove(onMouseMove);
$('#canvas').mouseup(onMouseUp);
$('#js-export-sketch').click(onExportSketch);

function onMouseDown(event){
    let target = event.currentTarget;
    drawing = true;
    onMouseClick(event.pageX - target.offsetLeft, event.pageY - target.offsetTop);
    sketch();
}

function onMouseMove(event){
    let target = event.currentTarget;
    if (drawing) {
        onMouseClick(event.pageX - target.offsetLeft, event.pageY - target.offsetTop, true);
        sketch();
    }
}

function onMouseUp(event){
    drawing = false;
}

function onMouseClick(startX, startY, move) {
  startsX.push(startX);
  startsY.push(startY);
  moves.push(move);
}

function sketch(){
    context.clearRect(0, 0, context.canvas.width, context.canvas.height);
    context.lineWidth = 2;
    context.lineJoin = "round";
    context.strokeStyle = "#0000000";

    $.each(startsX, function(idx, value) {
        context.beginPath();

        if (moves[idx] && idx) {
            context.moveTo(startsX[idx - 1], startsY[idx - 1]);
        } else{
            context.moveTo(startsX[idx] - 1, startsY[idx]);
        }

        context.lineTo(startsX[idx], startsY[idx]);
        context.closePath();
        context.stroke();
    });
}

function onExportSketch() {
    let dataBase64 = canvas.toDataURL();
    let resultContainer = $('#renderContainer');

    $.post( "handlePost", { datas: dataBase64 }, function( data ) {
        var image = new Image();
        image.src = data;
        resultContainer.empty();
        resultContainer.append(image);
        console.log(data);
    });
}