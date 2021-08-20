const pk=window.location.pathname.split("/")[3]
const btn =document.getElementsByClassName('btn')
const likeBtn=document.getElementsByClassName('like')
const csrf=document.getElementsByName('csrfmiddlewaretoken')[0].value
const numLikes=document.getElementsByClassName('num-likes')[0]
const commentInput=document.getElementById('comment')
const commentCont=document.getElementsByClassName('comment-container')[0]
const title=document.getElementsByTagName('h2')[0].innerHTML
const socialShare=document.getElementsByClassName('social-share')
const posttitle= encodeURIComponent(`"${title}" Ingin tahu kelanjutannya? Cek selengkapnya di Artsodevalog: `)
const postUrl=encodeURIComponent(window.location.href)
// console.log(posttitle)
import * as modul from './module.js'

socialShare['facebook_share'].setAttribute('href',`https://www.facebook.com/sharer.php?u=${postUrl}`)
socialShare['whatsapp_share'].setAttribute('href',`https://api.whatsapp.com/send?text=${posttitle} ${postUrl}`)
socialShare['linkedin_share'].setAttribute('href',`https://www.linkedin.com/shareArticle?mini=true&url=${postUrl}&title=${posttitle}`)
if (btn['show_more']!= undefined) btn['show_more'].addEventListener('click',e=>modul.showMoreComm(csrf,pk,e.target,commentCont,e.target.parentNode,btn['show_less'].parentNode))

btn['show_less'].addEventListener('click',e=>{
    const commentContain=document.getElementsByClassName('comment-container')[0]
    const btn =document.getElementsByClassName('btn')
    modul.showLessComm(commentContain,btn['show_more'],e.target)
})

if (likeBtn['like']!=undefined) likeBtn['like'].addEventListener('click',()=>modul.sendData(likeBtn['like'],csrf,numLikes))

if (btn['comment_btn'!=undefined]) btn['comment_btn'].addEventListener('click',()=>modul.sendComment(commentInput,pk,csrf,commentCont))