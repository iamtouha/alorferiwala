function stickyNav() {
    const scrollPos = window.scrollY
    const element = document.querySelector('#nav')
    const otherElement = document.querySelector('header')
    const elementPos = otherElement.clientHeight

    if (scrollPos > (elementPos - 50)) {
        element.classList.add("fixed")
        otherElement.classList.add("marginBottom")
    } 
    else {
        element.classList.remove("fixed")
        otherElement.classList.remove("marginBottom")
    }
}
stickyNav()
window.addEventListener('scroll', stickyNav)
$(document).ready(function(){
    setTimeout(function() {
        $('#message').fadeOut('slow')
    }, 4000)
})