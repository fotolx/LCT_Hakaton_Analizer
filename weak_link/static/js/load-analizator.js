const btn = document.getElementById('analizator-btn');

const analizator = document.querySelector('.analizator');
const loadAnalizator = document.querySelector('.load-analizator');
const loadAnalizatorText = document.querySelector('.load-analizator__text');
const loadAnalizatorSubText = document.querySelector('.load-analizator__subtext');
const formAnalizator = document.querySelector('.analizator-form');
const saveAnalizator = document.querySelector('.save-analizator');
const wrapperTable = document.querySelector('.wrapper-table--block');
const imgPlus = document.querySelector('.analizator-form__img--load');
const imgLoad = document.querySelector('.analizator-form__img--save');
const label = document.querySelector('.analizator-form__label')


if (wrapperTable) {
    btn.innerText = 'Обновить'
    btn.style.marginTop = '20px'

    analizator.classList.add('analizator--save');
    loadAnalizator.classList.add('load-analizator--save');
    loadAnalizatorText.classList.add('load-analizator__text--save');
    loadAnalizatorSubText.classList.add('load-analizator__subtext--save');
    formAnalizator.classList.add('analizator-form--save');
    saveAnalizator.classList.add('save-analizator--send');
    tablePeople.classList.remove('table-people--save')
    imgPlus.style.display = 'none';
    imgLoad.style.display ='block';
    label.classList.add('analizator-form__label--save')
}
