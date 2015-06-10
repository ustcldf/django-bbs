/**
 * Created by root on 15-4-16.
 */

$(function () {
    $("#create_district_form").on('ajax.success', function (e, data) {
        location.reload();
    }).on('ajax.error', function (e, data) {
    });
})