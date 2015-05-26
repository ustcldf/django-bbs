/**
 * Created by nolan on 15-5-18.
 */




$(document).ready(function () {
    $(".panel-heading").click(function () {
        $(this).parent().find(".panel-body").slideToggle("fast");
    })
});
