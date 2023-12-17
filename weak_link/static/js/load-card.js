const loadCardNumber = document.querySelector('.card-person__percent')
const loadBgCart = document.querySelector('.card-person__load-bg')

const loadNum = parseInt(loadCardNumber.textContent)

if (loadNum >= 50) {
    loadCardNumber.style.color = '#FF7455'
    loadBgCart.style.background = '#FF7455';
} else if (loadNum <= 50) {
    loadCardNumber.style.color = '#48BB78'
    loadBgCart.style.background = '#48BB78';
}

const numValue = loadCardNumber.innerText.replace('%', '');
loadBgCart.style.width = `${numValue}%`
