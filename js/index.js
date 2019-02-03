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
    console.log("Form data is: ");
    console.log(formdata);
    $.post({
        url: "http://localhost:5000/npv",
        beforeSend: function(request) {
            request.setRequestHeader("Access-Control-Allow-Origin", "*");
        },
        data: JSON.stringify(formdata),
        contentType: "application/json",
        dataType: "json",
        success: function(response) {
            if (response["success"] == true) {
                console.log("Communication!");
                console.log(response["npv"]);
                var npvVal = response["npv"];
                $("span").append("hello");
                $("#cashSubmit").show();
                $("#tagscloud span").text(npvVal);
            }
        }
    });
    e.preventDefault();
});