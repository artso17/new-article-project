const url =window.location
const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value
const searchInput=document.getElementsByClassName('search-input')
const tableBody=document.getElementsByClassName('table-body')
const detailUrl=tableBody[0].querySelector('a.nav-link')['href'].split('/')[3]
//  console.log(detailUrl) 

import { sendSearchData } from "./module.js"

    for (let i = 0; i < searchInput.length; i++) {
        searchInput[i].addEventListener('keyup',e=>{
            sendSearchData(e.target.value,searchInput[i],tableBody[i],tableBody,csrf,detailUrl)
        });
    }

