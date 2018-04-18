function genSquare() {
    var c = document.getElementById("myCanvas");
    var ctx = c.getContext("2d");
    var lastY = -45;

    for (var i = 0; i < 9; i++) {
        var y = lastY + 80;

        if (i % 3 == 0 && i != 0) {
            y = lastY + 100;
        }

        lastY = y;
        drawMore(y);
    }
}

function drawMore(y) {
    var lastX = -45;
    var c = document.getElementById("myCanvas");
    var ctx = c.getContext("2d");

    for (var i = 0; i < 9; i++) {
        var x = lastX + 80;

        if (i % 3 == 0 && i != 0) {
            x = lastX + 100;
        }

        lastX = x;
        ctx.rect(x, y, 50, 50);
        ctx.stroke();
    }
}

function test() {
    genSquare();

    lastY = 38;

    for (var i = 0; i < 9; i++) {
        var y = lastY + 80;

        if (i % 3 == 0 && i != 0) {
            y = lastY + 100;
        }

        var button = document.createElement("button");
        button.className += "button";
        button.innerHTML = "";
        button.style.position = 'absolute';

        if (i == 0) {
            button.style.top = y;
            button.style.left = '587px';
        }

        var body = document.getElementsByTagName("body")[0];
        body.appendChild(button);
    }
}

//button.addEventListener ("click", function() {
//  alert("did something");
//});
