$(document).ready(function () {
    $("#text2summary_button").click(function () {
        var e_text = $('#text2summary').val()
        console.log(e_text);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/text_summary",
            data: e_text,
            success: function (response) {
                alert(response)
                $('#summary_state').text(response);
            }
        });
    });
});