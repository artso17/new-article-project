export const truncate = (data,maxword)=>{
    const splitQs=data.split(' ')
    if (splitQs.length>maxword-1){
    const arrData=splitQs
    let newArrData=[]
    for (let i = 0; i < arrData.length; i++) {
        if (i>maxword-1){
        break;
        }
    newArrData.push(arrData[i]);
    }
    // console.log(newArrData.join(' '))
        return newArrData.join(' ')
    }
    return splitQs.join(' ')
}