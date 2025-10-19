let information = document.getElementById("info");
let timelines = document.getElementsByClassName("timeline");

let descriptions = { 
    "instructor":"Raymond becoming a coding instructor starting with Level M", 
    "portfolio":"Raymond made a Web Portfolio project", 
    "study":"Raymond graduated from the university", 
    "learn":"Raymond started to learn Software Engineering"
}

for (var i = 0; i < timelines.length; i++) {
    var timeline = timelines[i];
    timeline.onclick = function(event) {
        information.innerHTML = descriptions[event.target.id];
    }
}