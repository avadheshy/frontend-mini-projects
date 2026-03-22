var passwordLength=0
const specialChars = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/"
const passwordLengthChanger = document.querySelector('.password-length')
const slider = document.getElementById("myRange");
const showPassword = document.getElementById('myInput')
const buttonElemments = document.querySelectorAll('.box')
const generatePassword = document.querySelector('.generate-password')
const passwordStrength = document.querySelector('.pswd-threnght')
const passwordCopy = document.querySelector('.fa-copy')
var specialCounter=0
var functionArray=[]
slider.addEventListener("input",function fun() {
    passwordLength=Number(slider.value)
    passwordLengthChanger.innerHTML=passwordLength
})


const getUpperCaseLetter = () =>
    String.fromCharCode(Math.floor(Math.random() * 26) + 65);

const getLowerCaseLetter = () =>
    String.fromCharCode(Math.floor(Math.random() * 26) + 97);

const getNumber = () =>
    Math.floor(Math.random() * 10);

const getSpecialCharacter = () =>
    specialChars[Math.floor(Math.random() * specialChars.length)];



buttonElemments.forEach(element => {
    element.addEventListener('click', () => {
        if (element.id === 'upper') {
            functionArray.push(getUpperCaseLetter);
            specialCounter+=1
        }

        if (element.id === 'lower') {
            functionArray.push(getLowerCaseLetter);
            specialCounter+=1
        }

        if (element.id === 'number') {
            functionArray.push(getNumber);
            specialCounter+=1
        }

        if (element.id === 'symbol') {
            functionArray.push(getSpecialCharacter);
            specialCounter+=1
        }
    });
});

function checkPasswordStrength(password,passArray){
    if (password.length>12 & passArray.length==4){
        return "green"
    }
    if (passArray.length>2 & password.length>7)
    {
        return 'yellow'
    }
    return 'red'
}
generatePassword.addEventListener('click',()=>{

    if (passwordLength<specialCounter)
    {
        passwordLength=specialCounter
    }
    pass=[]
    var i=0

    for(i=0;i<specialCounter;i++){
        pass.push(functionArray[i]())
    }
    for(i=specialCounter ;i<passwordLength;i++){
        index=Math.floor(Math.random()*functionArray.length)
        pass.push(functionArray[index]())
    }
    pass=pass.join("")
    showPassword.value=pass
    passwordStrength.style.backgroundColor = checkPasswordStrength(pass, functionArray);

})

passwordCopy.addEventListener('click',()=>{
    copiedPassowrd=showPassword.value
    passwordCopy.innerHTML="coppied"
    passwordCopy.style.backgroundColor='red'
})