const cleanData = (args)=>{
    let output = []
    let listName = {}
    let like = require(`./${args}.json`)
    Object.keys(like['collectors']).map((name,idx)=>{
        listName[idx] = name
        if(arg == 'reaction'){
            like['collectors'][name].map((data)=>{
                output.push([idx,data['date'],data['info']['shares_count'],data['info']['comments_count']
                ,data['info']['reactions']['wow'],data['info']['reactions']['sad'],data['info']['reactions']['love']
                ,data['info']['reactions']['like'],data['info']['reactions']['haha'],data['info']['reactions']['angry']]) 
                
            })    
        }else{
            for(let i = 0 ; i < 18 ; i++){
                let result = like['collectors'][name][i+1]['number'] - like['collectors'][name][i]['number']
                output.push([idx,result])
            }
        }
    })
    return output
}
const initDate = (day,month,endDay,endMonth)=>{
    let date = []
    let curMonth = month 
    for(let i = day ; curMonth < endMonth || i <= endDay;i++){
        if(curMonth == '01' || curMonth == '03'|| curMonth == '05'|| curMonth == '07' || curMonth == '08' || curMonth == '10' || curMonth == '12'){
            if(i > 31) {
                i = 1
                curMonth += 1
            }
        }else if( curMonth == '02'){
            if(i > 28) {
                i = 1
                curMonth += 1
            }
        }else{
            if(i > 30) {
                i = 1
                curMonth += 1
            }
        }
        if(i < 10){
            i = `0${i}`
        }
        date[(`2018-0${curMonth}-${i}`)] = []
    }
    return date
}
const exported = (frame,args)=>{
    var json = JSON.stringify(frame)
    var fs = require('fs')
    fs.writeFile(`${args}_Cleaned.json`, json, 'utf8')    
}
const combine =(date,data)=>{
    for(let i = 0 ; i < Object.keys(data).length ; i++){
        if(data[i+1]){
            if(data[i][0] == data[i+1][0] && data[i][1] == data[i+1][1]){
                data[i+1][2] += data[i][2]
                data[i+1][3] += data[i][3]
                data[i+1][4] += data[i][4]
                data[i+1][5] += data[i][5]
                data[i+1][6] += data[i][6]
                data[i+1][7] += data[i][7]
                data[i+1][8] += data[i][8]
                data[i+1][9] += data[i][9]
                data[i] = null
            }
        }
    }
    let temp = []
    let arr = []
    for (let i = 0; i < 26; i++) {
        arr[i] = Object.keys(date)
    }
    for(let i = 0 ; i < Object.keys(data).length ; i++){
        if(data[i]){
            let index = data[i][0]
            let day = data[i][1]
            arr[index][day] = data[i]
        }
    }
    for (let i = 0; i < 26; i++) {
        Object.keys(date).map((v)=>{
            if(arr[i][v]){
            }else{
                arr[i][v] = [i,v,0,0,0,0,0,0,0,0]
            }
        })
    }
    let sum = 0 
    for (let i = 0; i < 26; i++) {
        Object.keys(date).map((v)=>{
            temp[sum] = arr[i][v]
            sum += 1
        })
    } 
    return temp
    
}
const arg = 'reaction'

if(arg == 'growth'){
    let data = cleanData(arg)
    exported(data,arg)    
}
else if(arg == 'reaction'){
    let data = cleanData(arg)
    let date = initDate(14,03,31,03)
    let data1 = combine(date,data)
    exported(data1,`${arg}`)
}
