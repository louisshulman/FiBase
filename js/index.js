// alert("This works!");

// function formSubmitted(){
//     var cv19 = document.getElementById("2019").value;
//     var cv18 = document.getElementById("2018").value;
//     var cv17 = document.getElementById("2017").value;
//     var cv16 = document.getElementById("2016").value;
//     var cv15 = document.getElementById("2016").value;
//     console.log(cv15 + " " + cv16 + " " + cv17 + " " + cv18 + " " + cv19 + "");
    
// }

// document.getElementById("cashForm").onsubmit = function(){formSubmitted()};




$("#cashSubmit").click(function(e){
    var $forma = $("#cashForm");
    // Thanks David and ACM Website - https://github.com/UA-ACM-Student-Chapter/UA-ACM-Student-Chapter.github.io/blob/master/js/acm-1.0.1.js
    var $forma = $("#cashForm");
    var data = getFormData($forma);
    var jsonnn = JSON.stringify(data);
    alert(jsonnn);
    e.preventDefault();
});