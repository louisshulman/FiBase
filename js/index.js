// Thanks David and ACM Website - https://github.com/UA-ACM-Student-Chapter/UA-ACM-Student-Chapter.github.io/blob/master/js/acm-1.0.1.js
var getFormData = function($form) {
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};
    $.map(unindexed_array, function(n, i) {
        indexed_array[n["name"]] = n["value"];
    });
    return indexed_array;
}

// Thanks David and ACM Website - https://github.com/UA-ACM-Student-Chapter/UA-ACM-Student-Chapter.github.io/blob/master/js/acm-1.0.1.js
$("#cashSubmit").click(function(e){
    var $forma = $("#cashForm");
    var formdata = getFormData($forma);
    $("#cashSubmit").hide();
    $.post({
        url: "http://1270.0.0.1:5000/npv",
        data: JSON.stringify(formdata),
        contentType: "application/json",
        dataType: "json",
        function(response) {
            console.log("Communication!");
            $("span").append("hello");
            $("#cashSubmit").show();
            $("#tagscloud span").text("Your text here");
        }
    });
    e.preventDefault();
});