const burgerMemu = document.querySelector('[data-burger]');
const mainNavigationMobile = document.querySelector('.main-navigation');

burgerMemu.addEventListener('click', () => {
    mainNavigationMobile.classList.toggle('mainNavigation--mobile')
})