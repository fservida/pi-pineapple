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


$('#start-mitm').click(start_mitm);
$('#stop-mitm').click(stop_mitm);

function start_mitm() {

    console.log("Contacting backend to start MITM!");// sanity check

    $.ajax({
        url: "/api/network/mitm/on", // the endpoint
        type: "GET", // http method

        // handle a successful response
        success: function (json) {
            console.log("Successfully Started MITM");
            window.location.reload(true); // Refresh page
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            // Display Error Message
        },
    });
};

function stop_mitm() {

    console.log("Contacting backend to stop MITM!");// sanity check

    $.ajax({
        url: "/api/network/mitm/off", // the endpoint
        type: "GET", // http method

        // handle a successful response
        success: function (json) {
            console.log("Successfully Stopped MITM");
            window.location.reload(true); // Refresh page
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            // Display Error Message
        },
    });
};


$('#start-tcpdump').click(start_tcpdump);
$('#stop-tcpdump').click(stop_tcpdump);

function start_tcpdump() {

    console.log("Contacting backend to start tcpdump!");// sanity check

    $.ajax({
        url: "/api/system/services/tcpdump/on", // the endpoint
        type: "GET", // http method

        // handle a successful response
        success: function (json) {
            console.log("Successfully Started tcpdump");
            window.location.reload(true); // Refresh page
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            // Display Error Message
        },
    });
};

function stop_tcpdump() {

    console.log("Contacting backend to stop tcpdump!");// sanity check

    $.ajax({
        url: "/api/system/services/tcpdump/off", // the endpoint
        type: "GET", // http method

        // handle a successful response
        success: function (json) {
            console.log("Successfully Stopped tcpdump");
            window.location.reload(true); // Refresh page
        },

        // handle a non-successful response
        error: function (xhr, errmsg, err) {
            // Display Error Message
        },
    });
};