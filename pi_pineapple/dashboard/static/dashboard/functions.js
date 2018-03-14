/*
	All Pages
*/

window.setInterval(function () {
    $("#alert").fadeTo(500, 0).slideUp(500, function () {
        $(this).remove();
    });
}, 10000);

// WPS Progress Bar
var actual_progress = 0;
var progress_interval = null;
var progress_timeout = null;
$('#start-wps').click(start_wps);

function start_wps() {

    console.log("Contacting backend to start WPS!");// sanity check

    $.ajax({
        url: "/api/network/wireless/hostapd/wps", // the endpoint
        type: "GET", // http method

        // handle a successful response
        success: function (json) {
            progress_bar();
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            // Display Error Message
        },
    });
};



function progress_bar() {
    // Stop all ongoing timers
    window.clearInterval(progress_interval);
    window.clearTimeout(progress_timeout);

    // Restart timer
    actual_progress = 0;
    progress_interval = window.setInterval(function () {
        var progressbar = $("#wps-progress");
        progressbar.attr('aria-valuenow', actual_progress);
        progressbar.attr('aria-valuemax', 100);
        progressbar.css('width', actual_progress + '%');
        actual_progress += 1;
    }, 1200);
    progress_timeout = setTimeout(function() {
        window.clearInterval(progress_interval)
    }, 120000);
};

