const burger = document.querySelector('[data-burger]');
const mainNavigation = document.querySelector('.main-navigation');
const menuListTitle = document.querySelectorAll('.menu-list__title');
const menuListIcon = document.querySelectorAll('.menu-list__icon');
const menuIcon = document.querySelectorAll('.menu-icon');
const logo = document.querySelector('.main-navigation-logo');

const handleBurgerClick = () => {
    burger.classList.toggle('burger--active');
    mainNavigation.classList.toggle('main-navigation--active');
    logo.classList.toggle('main-navigation-logo--active');

    menuListTitle.forEach((element) => {
        element.classList.toggle('menu-list__title--active');
    });

    menuListIcon.forEach((element) => {
        element.classList.toggle('menu-list__icon--active');
    });

    menuIcon.forEach((element) => {
        element.classList.toggle('menu-icon--active');
    });
};

const mediaQuery = window.matchMedia('(max-width: 1110px)');

const handleMediaQueryChange = (mediaQuery) => {
    if (mediaQuery.matches) {
        burger.removeEventListener('click', handleBurgerClick);
    } else {
        burger.addEventListener('click', handleBurgerClick);
    }
};

handleMediaQueryChange(mediaQuery);

mediaQuery.addEventListener('change', handleMediaQueryChange);