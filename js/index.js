// alert("This works!");

function formSubmitted(){
    var xx = document.getElementById("x").value;
    var yy = document.getElementById("y").value;
    var zz = document.getElementById("z").value;
    var ww = document.getElementById("w").value;
    console.log(xx + " " + yy + " " + zz + " " + ww + " ");
    
}

document.getElementById("myForm").onsubmit = function(){formSubmitted()};


