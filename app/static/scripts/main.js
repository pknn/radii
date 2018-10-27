$('document').ready(function () {
    console.log('Hi');
})

$("#toggleButton").on("click", function() {
    if ($("#password-input").attr('type') === 'password'){
        $("#password-input").attr('type', 'text');
        $("#toggleButton").html('<i class="fas fa-eye"></i>');

    }else {
        $("#password-input").attr('type', 'password');
        $("#toggleButton").html('<i class="fas fa-eye-slash"></i>');
    }
});