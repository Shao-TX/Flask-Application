$(document).ready(function () {
    $("#text2emotion_button").click(function () {
        var e_text = $('#text2emotion').val()
        console.log(e_text);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/text_emotion",
            data: e_text,
            success: function (data) {
                alert(data)
                $('#emotion_state').text("Text Emotion : " + data);
            }
        });
    });
});