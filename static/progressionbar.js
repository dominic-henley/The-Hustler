
function move() {
    var elem = document.getElementById("myBar");
    var width = 10;
    var id = setInterval(frame, 10);

    elem.style.width = width + "%";
    elem.innerHTML = width + "%";


    function frame() {
        width = 100;
        elem.style.width = width + "%";
        elem.innerHTML = width + "%";
        clearInterval(id);

    }
}