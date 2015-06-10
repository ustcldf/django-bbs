/**
 * Created by root on 15-4-16.
 */
$(function () {
    $("#profile_form").on('ajax.success', function (e, data) {
        location.reload();
    }).on('ajax.error', function (e, data) {
    });
})