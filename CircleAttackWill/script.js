const PLAYER_SPEED = 10;
const PLAYER_SIZE = 20;
const ENEMY_SPEED = 30;
const ENEMY_SIZE = 15;

let playerX;
let playerY;
let score;

let aKeyPressed;
let wKeyPressed;
let sKeyPressed;
let dKeyPressed;

let enemies = []
let isPlaying = false;

let canvasObject = document.getElementById("gameCanvas");
let canvas = canvasObject.getContext('2d');

canvasObject.width = window.innerWidth;
canvasObject.height = window.innerHeight;

document.addEventListener("keydown", keyDownHandler, false);
document.addEventListener("keyup", keyUpHandler, false);

function keyDownHandler(e) {
    if(e.keyCode == 65) {
        aKeyPressed = true;
    } else if(e.keyCode == 68) {
        dKeyPressed = true;
    } else if(e.keyCode == 83) {
        wKeyPressed = true;
    } else if(e.keyCode == 87) {
        sKeyPressed = true;
    } else if(e.keyCode == 32 && isPlaying == false) {
        isPlaying = true;
        resetGame()
    }
}

function keyUpHandler(e) {
    if(e.keyCode == 65) {
        aKeyPressed = false;
    } else if(e.keyCode == 68) {
        dKeyPressed = false;
    } else if(e.keyCode == 83) {
        wKeyPressed = false;
    } else if(e.keyCode == 87) {
        sKeyPressed = false;
    }
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function resetGame() {
    playerX = PLAYER_SIZE + 10;
    playerY = canvasObject.height / 2;
    score = 0;
    updateScore();
    addEnemies(2);
}

function addEnemies(numOfEnemies) {
    for (let i = 0; i < numOfEnemies; i++) {
        enemies[i] = {
            x: getRandomInt(canvasObject.width/2, canvasObject.width),
            y: getRandomInt(ENEMY_SIZE, canvasObject.height-ENEMY_SIZE),
            size: ENEMY_SIZE

        }
    }
}

function drawPlayer() {
    canvas.beginPath();
    canvas.arc(playerX, playerY, PLAYER_SIZE, 0, Math.PI*2)
    canvas.fillStyle = 'red';
    canvas.fill()
    canvas.closePath()
    checkWalls();

    if(aKeyPressed) {
        playerX -= PLAYER_SPEED
    } if(sKeyPressed) {
        playerY -= PLAYER_SPEED
    } if(dKeyPressed) {
        playerX += PLAYER_SPEED
    } if(wKeyPressed) {
        playerY += PLAYER_SPEED
    }
}

function draw() {
    canvas.clearRect(0, 0, canvasObject.width, canvasObject.height)
    if(isPlaying) {
        drawPlayer();
        drawEnemy();
        checkCollision();

    } else {
        drawClickToPlay();
    }
}
setInterval(draw, 20)

function drawEnemy() {
    for(let i=0 ; i<enemies.length ; i++) {
        let theEnemy = enemies[i];
        theEnemy.x -= getRandomInt(10, ENEMY_SPEED);
        canvas.beginPath();
        canvas.arc(theEnemy.x, theEnemy.y, theEnemy.size, 0, Math.PI*2);
        canvas.fillStyle = 'black';
        canvas.fill();
        canvas.closePath();

        if(theEnemy.x <= 0) {
            score += 1;
            updateScore();
            theEnemy.x = canvasObject.width;
            theEnemy.y = getRandomInt(ENEMY_SIZE, canvasObject.height-ENEMY_SIZE)
            if (score%10 == 0 && score > 0) {
                addOneEnemy();
            }
        }
    }
}
function addOneEnemy() {
    enemies.push({x: getRandomInt(canvasObject.width/2, canvasObject.width),
        y: getRandomInt(ENEMY_SIZE, canvasObject.height-ENEMY_SIZE),
        size: ENEMY_SIZE})
}

function updateScore() {
    document.getElementById("footer").innerHTML = "<h2>Score: " + score + "</h2>"
}

function checkCollision() {
    let thePlayer = {
        radius: PLAYER_SIZE,
        x: playerX,
        y: playerY,
    }

    for(let i=0; i < enemies.length; i++) {
        let theEnemy = enemies[i];
        let dx = thePlayer.x - theEnemy.x;
        let dy = thePlayer.y - theEnemy.y;
        let dist = Math.sqrt(dx*dx + dy*dy)
        if(dist < thePlayer.radius+theEnemy.size) {
            isPlaying = false;
        }
    }
}

function drawClickToPlay() {
    canvas.font = "30px Arial"
    canvas.fillText("game over", canvasObject.width/2, canvasObject.height/2)
    canvas.fillText("press space to start", canvasObject.width/2 -110, canvasObject.height/2 + 50)
}

function checkWalls() {
    if(playerX < 0) playerX = 0;
    if(playerY < 0) playerY = 0;
    if(playerX > canvasObject.width) playerX = canvasObject.width;
    if(playerY > canvasObject.height) playerY = canvasObject.height;
}