const loadBack=document.getElementsByClassName('loading-background')[0]
console.log(loadBack)
window.addEventListener('load',()=>loadBack.classList.add('fade-out'))