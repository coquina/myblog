$(document).ready(function () {
    $(function (startTime) {
        today = new Date();
    H = today.getHours();
    m = today.getMinutes();
    s = today.getSeconds();
    m = checkTime(i);
    s = checkTime(i);
    document.getElementById('clock').innerHTML = H + ":" + m + ':' + s;
    t = setTimeout(startTime,500);
    });


    function checkTime(i) {
        if (i < 10) {i = "0" + i}  // add zero in front of numbers < 10
    return i;
    }
});


