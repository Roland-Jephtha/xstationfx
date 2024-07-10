var Logg = function() {
    event.preventDefault();
    $("#failed").addClass("hidden");
    $("#L4").removeClass("hidden");
    document.getElementById("btnlogin").disabled = true;
    document.getElementById("body").style.cursor = "wait";
    var email = $("#email").val();
    var password = $("#password").val();
    var url = window.location.hostname + (window.location.port ? ':' + window.location.port : '');
    $.getJSON("LoginApi.aspx?email=" + email + "&password=" + password, function(data) {
        if (data == "1") {

            countdown();
        } else if (data == "2") {

            countdown2();
        } else {
            $("#failed").removeClass("hidden");
            $("#L4").addClass("hidden");
            document.getElementById("btnlogin").disabled = false;
            document.getElementById("body").style.cursor = "default";
        }
    });
}

var seconds = 2;

function countdown() {
    seconds = seconds - 1;

    if (seconds < 0) {
        window.location = "Users/Account.aspx";
    } else {

        window.setTimeout("countdown()", 1000);
    }
}

function countdown2() {
    seconds = seconds - 1;

    if (seconds < 0) {
        window.location = "2fa.aspx";
    } else {

        window.setTimeout("countdown2()", 1000);
    }
}

$(window).on("load", function() {
    setTimeout(function() {
        $(".bonus_area").addClass("show")
    }, 10000);
    setTimeout(showpop, 7000);
});

$(".close-btn").click(function() {
    event.preventDefault();
    $(".bonus_area").removeClass("show");
});

/////my pops
var GetPopUp = function() {
    var url = window.location.hostname + (window.location.port ? ':' + window.location.port : '');
    $.getJSON("GetPopUp.ashx", function(data) {
        $('#UserID').text(data.UserID);
        $('#type').text(data.Type);
        $('#amount').text(data.Amount);
        $('#time').text(data.Time);
        $(".mypop").addClass("show");
    });
}
var showpop = function() {
    GetPopUp();

    setTimeout(hidepop, 5000);
}
var hidepop = function() {
    $(".mypop").removeClass("show");
    setTimeout(showpop, 80000);
}

$(".mypop .close").click(function() {

    $(".mypop").removeClass("show");
    //setTimeout(showpop, 30000);
});