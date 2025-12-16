let result = document.getElementById("result");
let biography = document.getElementsByClassName("things");
let descriptions = {
    "coolbutton":"this button does something",
    "coolerbutton":"this button does something else"
}
for (let i = 0; i < biography.length; i++) {
    let button = biography[i];
    button.onclick = function(e) {
        //result.innerHTML = descriptions[e.target.id]
        alert("efigsdg");
    }
}