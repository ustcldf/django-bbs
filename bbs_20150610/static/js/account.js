/**
 * Created by nolan on 15-5-18.
 */




$(document).ready(function () {
    $(".panel-heading").click(function () {
        $(this).parent().find(".panel-body").slideToggle("fast");
    });


    //删除用户按钮
    $(".btn[cmd=delUser]").on("click", function () {
        user_id = $(this).attr("user_id");

        alert(user_id)

        if (confirm("是否删除用户[" + $(this).attr("user_name") + "]")) {
            var url = "/account/deleteUser/";

            $.ajax({
                type: "POST",
                url: url,
                data: {user_id: user_id},
                success: function(msg){
                    window.location.reload();
                },
                error: function () {
                    alert('error');

                }
            });

        }
    });
    //编辑按钮
    $(".btn[cmd=edit]").on("click", function () {
        alert("Hello")
        window.location.reload();
    });
});


