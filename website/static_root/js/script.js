const activeMenu=()=>{
    const elem=document.querySelector('.active')
    const navLink=document.querySelectorAll('.nav-link')
    let scrollPos=window.scrollY


    if(window.innerWidth>992 && scrollPos <400){
        navLink[0].classList.add('active')
        navLink[1].classList.remove('active')
    }else if(window.innerWidth>992 && scrollPos <1438){
        navLink[0].classList.remove('active')
        navLink[1].classList.add('active')
        navLink[2].classList.remove('active')
    }else if(window.innerWidth>992 && scrollPos <2443){
        navLink[1].classList.remove('active')
        navLink[2].classList.add('active')
        navLink[3].classList.remove('active')
    }else if(window.innerWidth>992 && scrollPos <3204){
        navLink[2].classList.remove('active')
        navLink[3].classList.add('active')
        navLink[4].classList.remove('active')
    }else if(window.innerWidth>992 && scrollPos <4000){
        navLink[3].classList.remove('active')
        navLink[4].classList.add('active')
        
    }
}
window.addEventListener('scroll',activeMenu)
