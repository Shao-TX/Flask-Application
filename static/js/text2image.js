$(document).ready(function () {
    // $(".loader").hide()
    $("#text2image_button").click(function () {
        $(".loader").show()
        $("#g_img").hide()
        var g_text = $('#text2image').val()
        console.log(g_text);
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:5000/generate_image",
            data: g_text,
            success: function (response) {
                var g_img = "../static/img/" + response + ".png"
                alert(g_img)
                $(".loader").hide()
                $("#g_img").prop("src", g_img)
                $("#g_img").attr("width", 250)
                $("#g_img").show()
            }
        });
    });
});