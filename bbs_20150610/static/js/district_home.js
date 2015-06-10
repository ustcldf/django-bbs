/**
 * Created by nolan on 15-5-18.
 */




$(document).ready(function () {
    $(".panel-heading").click(function () {
        $(this).parent().find(".panel-body").slideToggle("fast");
    });


    //删除版块
    $(".btn[cmd=delForum]").on("click", function () {
        forum_id = $(this).attr("forum_id");

        alert("注意：您的操作也会级联删除该版块下的所有文章！")

        if (confirm("是否删除版块[" + $(this).attr("forum_name") + "]")) {
            var url = "/forum/deleteForum/";

            $.ajax({
                type: "POST",
                url: url,
                data: {forum_id: forum_id},
                success: function(msg){
                    window.location.reload();
                },
                error: function () {
                    alert('error');

                }
            });

        }
    });

     //删除区域
    $(".btn[cmd=delDistrict]").on("click", function () {
        district_id = $(this).attr("district_id");

        alert("注意：您的操作也会级联删除该区域下的所有版块及版块下的文章！")

        if (confirm("是否删除区域[" + $(this).attr("district_name") + "]")) {

            var url = "/district/deleteDistrict/";

            $.ajax({
                type: "POST",
                url: url,
                data: {district_id: district_id},
                success: function(msg){
                    window.location.reload();
                },
                error: function () {
                    alert('error');

                }
            });

        }
    });

});


