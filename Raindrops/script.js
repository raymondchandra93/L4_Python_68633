let c = document.getElementById("myCanvas");
let ctx = c.getContext("2d");

let raindrops = [];
let wind = 0;

function gameLoop() {
    // Fill canvas with white color
    ctx.fillStyle = "white";
    
    // Draw the canvas again back with white color
    ctx.rect(0, 0, c.width, c.height);

    ctx.fill();

    // Create a new raindrop
    let raindrop = {
        x: Math.random() * (c.width+2000 - (-2000)) + (-2000),
        y: -100,
        yspeed: Math.random() * (6 - 3) + 3
    }
    
    // Append raindrop
    raindrops.push(raindrop);

    // Iterate through the raindrop make the raindrop going down - in reverse way
    for(let i = raindrops.length-1; i >= 0 ; i--) {

        // Get a single raindrop
        let drop = raindrops[i];

        // Move the raindrop downward - lower the y position
        drop.y += drop.yspeed;

        // Move the raindrop left and right based on wind
        drop.x += wind;

        // If raindrop falls below canvas, remove it
        if(drop.y > c.height) {
            raindrops.splice(i, 1);
        }

        // Else, raindrop will be shown on the canvas
        else {
            ctx.beginPath();
            ctx.rect(drop.x, drop.y, 2, 4);
            
            ctx.fillStyle = "blue";
            ctx.fill();
        }
    }
}

// Call the animation
setInterval(gameLoop, 30);

document.addEventListener("keydown", keyDownHandler, false);

function keyDownHandler(e) {
    if (e.keyCode == 37 ) {
        wind--;
    } else if (e.keyCode == 39) {
        wind++;
    }
}