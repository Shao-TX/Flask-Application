// 語法為 $（對象）. 行為（參數/任務）
$(document).ready(function () {
    $("#arduino_button").click(function () {
        // var check_button = $(this).val();
        if ($("#arduino_button").prop("checked")) {
            console.log("Arduino Turn On");
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/control_arduino",
                data: "On",
                success: function (response) {
                    $('#arduino_state').text("Arduino : " + response);
                }
            });
        }
        else {
            console.log("Arduino Turn Off");
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/control_arduino",
                data: "Off",
                success: function (response) {
                    $('#arduino_state').text("Arduino : " + response);
                }
            })
        }
    });
});