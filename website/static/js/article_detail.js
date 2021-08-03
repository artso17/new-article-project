const btn =document.getElementsByClassName('btn')[1]
const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value
const numLikes=document.getElementsByClassName('num-likes')[0]
const metaDesc=document.getElementsByName('description')[0]
const articleIsi=document.getElementsByTagName('article')[0].firstElementChild.innerHTML
console.log(articleIsi)

import {truncate} from './module.js'
// console.log(truncate)

const sendData=(data)=>{
    $.ajax(
        {
            type:'POST',
            url:'/likes/',
            data:{
                'csrfmiddlewaretoken':csrf,
                'data':data,
    
            },
            success:(res)=>{
                console.log(res.data[0]['liked']) 
                numLikes.innerHTML=`${res.data[0]['num_likes']}`
                if (res.data[0]['liked'] == false){
                btn.innerHTML=`like`
                btn.classList.add('btn-outline-primary')
                btn.classList.remove('btn-secondary')
                }else{
                btn.innerHTML=`unlike`
                btn.classList.add('btn-secondary')
                btn.classList.remove('btn-outline-primary')
                }
            },
            error:(err)=>{
            console.log(err)
            }
    
        }
    )
        
}

btn.addEventListener('click',e=>{
    sendData(e.value)
})

metaDesc['content']=truncate(articleIsi,100)