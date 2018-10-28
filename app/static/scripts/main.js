$('document').ready(function () {
    let toggle = $('.combo-field-toggle');
    let passwordField = $('.combo-field.password-field');

    toggle.on('click', function () {
        if (passwordField.attr('type') === 'password') {
            passwordField.attr('type', 'text');
            toggle.children().addClass('fa-eye').removeClass('fa-eye-slash');
        } else {
            passwordField.attr('type', 'password');
            toggle.children().addClass('fa-eye-slash').removeClass('fa-eye');
        }
    })
});
