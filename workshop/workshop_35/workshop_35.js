//This is Comment

function concat(str1,str2){
    return `${str1} ${str2}`
}

function check_long_str(string){
    if (string.length > 10){
        return true
    }
    else{
        return false
    }
}


if (check_long_str(concat('Happy1','Hacking1'))){
    console.log('LONG STRING')//콘솔창에 출력
    document.write('LONG STRING')//브라우저창에 출력
}
else{
    console.log('SHORT STRING')
    document.write('SHORT STRING')
}