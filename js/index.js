// alert("This works!");

function formSubmitted(){
    var cv19 = document.getElementById("2019").value;
    var cv18 = document.getElementById("2018").value;
    var cv17 = document.getElementById("2017").value;
    var cv16 = document.getElementById("2016").value;
    var cv15 = document.getElementById("2016").value;
    console.log(cv15 + " " + cv16 + " " + cv17 + " " + cv18 + " " + cv19 + "");
    
}

document.getElementById("cashForm").onsubmit = function(){formSubmitted()};


