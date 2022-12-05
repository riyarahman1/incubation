var nameError = document.getElementById('name-error');
var companynameError = document.getElementById('companyname-error');
var addressError = document.getElementById('address-error');
var emailError = document.getElementById('email-error');
var websiteError = document.getElementById('website-error');
var phoneError = document.getElementById('phone-error');
var submitError = document.getElementById('submit-error');



function validateName() {
    var name = document.getElementById('contact-name').value;
    if (name == "") {
        nameError.innerHTML = "Please enter a name";
        return false;
    }
    if (!name.match(/^[a-za-z]*\s{1}[A-Za-z]*$/)) {
        nameError.innerHTML = "Please enter a valid name";
        return false;
    }
    nameError.innerHTML = 'valid';
    return true;
}
