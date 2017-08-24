window.onpageshow = function () {
    var request = $.ajax({
        type: 'GET',
        url: '/get_countries',
        contentType: "application/json; charset=utf-8"
    });
    request.done(function (data) {
        console.log(data);
        var option_list = [["", "--- Select One ---"]].concat(data);
        // Check data content...
        //console.log(option_list);
        //console.log(data[0]['country_name']);
        $("#country").empty();
        for (var i = 0; i < data.length; i++) {
            var x = document.getElementById("country");
            var option = document.createElement("option");
            option.text = data[i]['country_name'];
            x.add(option);
        }
    });
};