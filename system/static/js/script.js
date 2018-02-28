
$(window).on('load',function () {
    $('#toogleButton').on('click',function () {
        navbar = $('.navbar-top')[0];

       if(navbar.classList.contains('responsive')){
           navbar.classList.remove('responsive');
       }
       else { navbar.classList.add('responsive'); }
    })
})


