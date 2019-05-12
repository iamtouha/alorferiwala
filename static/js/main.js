function stickyNav() {
    const scrollPos = window.scrollY
    const element = document.querySelector('#nav')
    const otherElement = document.querySelector('header')
    const elementPos = otherElement.clientHeight

    if (scrollPos > (elementPos - 50)) {
        element.classList.add("fixed")
        otherElement.classList.add("marginBottom")
    } else {
        element.classList.remove("fixed")
        otherElement.classList.remove("marginBottom")
    }
}
stickyNav()
window.addEventListener('scroll', stickyNav)

function validateRegisterForm(event) {
    let name = document.forms['registerForm']['full_name'].value
    let username = document.forms['registerForm']['username'].value
    let phone_no = document.forms['registerForm']['phone_no'].value
    let password = document.forms['registerForm']['password'].value
    let repeatPassword = document.forms['registerForm']['repeat_password'].value
    fullname = name.split(" ")
    username = username.split(' ')
    phone = parseInt(phone_no)
    if (!fullname[1]) {
        document.querySelector('#errorMsg').innerHTML = "please enter first and last name separated by space"
        return false
    } else if (fullname[1]) {
        if (!fullname[1].trim()) {
            document.querySelector('#errorMsg').innerHTML = "please enter first and last name separated by space"
            event.preventDefault()
            return false
        }
    }
    if (username[1]) {
        event.preventDefault()
        document.querySelector('#errorMsg').innerHTML = "Username should be one single word"
        return false
    }
    if (!phone) {
        document.querySelector('#errorMsg').innerHTML = "Error: phone no. format: 01700000000"
        event.preventDefault()
        return false
    }
    if (phone_no.length > 11) {
        event.preventDefault()
        document.querySelector('#errorMsg').innerHTML = "Error: phone no. format: 01700000000"
        return false
    }
    if (password != repeatPassword) {
        document.querySelector('#errorMsg').innerHTML = "Passwords don't match"
        event.preventDefault()
        return false
    }

    return true
}

$(document).ready(function () {
    setTimeout(function () {
        $('#message').fadeOut('slow')
    }, 4000);
    $('.category-button, .category-list').hover(function () {
            setTimeout(function () {
                $('.category-list').css('display', 'block');
            }, 100);
        },
        function () {
            setTimeout(function () {
                $('.category-list').css('display', 'none');
            }, 100);
        })
})