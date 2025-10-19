
// --- Phase 2A ---

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

let enemies = [];
let isPlaying = false;

let canvasObject = document.getElementById("gameCanvas");
let canvas = canvasObject.getContext("2d");

canvasObject.width = window.innerWidth;
canvasObject.height = window.innerHeight;

// --- Phase 2B ---

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
    } else if(e.keyCode ==  32 && isPlaying == false) {
        isPlaying = true;
        resetGame()
    }
}

// --- Phase 2C ---

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

// --- Phase 2D ---

function resetGame() {
    playerX = PLAYER_SIZE + 10;
    playerY = canvasObject.height / 2;
    score = 0;

    updateScore()
    addEnemies(2);
}

function addEnemies(numOfEnemies) {
    for (let i = 0; i < numOfEnemies; i++) {
        enemies[i] = {
            x: getRandomInt(canvasObject.width/2, canvasObject.width),
            y: getRandomInt(ENEMY_SIZE, canvasObject.height-ENEMY_SIZE),
            size: ENEMY_SIZE
        };
    }
}

// --- Phase 2E ---

function drawPlayer() {
    canvas.beginPath();
    canvas.arc(playerX, playerY, PLAYER_SIZE, 0, Math.PI*2);
    canvas.fillStyle = "red";
    canvas.fill();
    canvas.closePath();
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

// --- Phase 2F ---

function draw() {
    canvas.clearRect(0, 0, canvasObject.width, canvasObject.height);
    if(isPlaying) {
        drawPlayer();
        drawEnemy();
        checkCollision();
    } else {
        drawClickToPlay();
    }
}

setInterval(draw, 30)

// -- Phase 2G --

function drawEnemy() {
    for(let i=0; i<enemies.length; i++) {
        // Get the enemy and move it
        let theEnemy = enemies[i];
        theEnemy.x -= getRandomInt(10, ENEMY_SPEED);
        
        // Draw the enemy
        canvas.beginPath();
        canvas.arc(theEnemy.x, theEnemy.y, theEnemy.size, 0, Math.PI*2);
        canvas.fillStyle = "blue";
        canvas.fill();
        canvas.closePath();

        // Update the score
        if(theEnemy.x <= 0) {
            score += 1;
            updateScore();

            theEnemy.x = canvasObject.width;
            theEnemy.y = getRandomInt(ENEMY_SIZE, canvasObject.height-ENEMY_SIZE);

            if (score%10 == 0 && score > 0) {
                addOneEnemy();
            }
        }
    }
}

function addOneEnemy() {
    enemies.push({
        x: getRandomInt(canvasObject.width/2, canvasObject.width),
        y: getRandomInt(ENEMY_SIZE, canvasObject.height-ENEMY_SIZE),
        size: ENEMY_SIZE
    });
}

// -- Phase 2H --

function updateScore() {
    document.getElementById("footer").innerHTML = "<h2>Score: " + score + "</h2>";
}

function checkCollision() {
    // Locate the player
    let thePlayer = {
        radius: PLAYER_SIZE,
        x: playerX,
        y: playerY
    };

    for(let i=0; i < enemies.length; i++) {
        let theEnemy = enemies[i];
        let dx = thePlayer.x - theEnemy.x;
        let dy = thePlayer.y - theEnemy.y;
        let dist = Math.sqrt(dx**2 + dy**2);    // This needs to be x*x or x**2
        
        // Check the dist agains sum of radius
        if(dist < thePlayer.radius+theEnemy.size) {
            isPlaying = false;
        }
    }
}

// -- Phase 2I

function drawClickToPlay() {
    canvas.font = "30px Arial";
    if(score > 0) {
        canvas.fillText("Game Over!!", canvasObject.width/2, canvasObject.height/2);
    }
    
    canvas.fillText("Press 'space' to start!!", canvasObject.width/2 -110, canvasObject.height/2 + 50)
}

// -- Phase 2J

function checkWalls() {
    if (playerX < 0) playerX = 0;
    if (playerY < 0) playerY = 0;
    if (playerX > canvasObject.width) playerX = canvasObject.width;
    if (playerY > canvasObject.height) playerY = canvasObject.height;
}