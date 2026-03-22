const player = document.querySelector('.player')
const restart = document.querySelector('.restart')
const boxes = document.querySelectorAll('.box')
var turn ='X'
let gameOver = false;
var table =[['','',''],['','',''],['','','']]
function begin(){
    turn ='X'
    gameOver=false
    table =[['','',''],['','',''],['','','']]
    player.innerHTML=`player ${turn}`
      boxes.forEach(box=>{
                box.innerHTML=''
                box.style.backgroundColor=''
            })

}
begin()
function checkWinner(){
    for(let i=0;i<3;i+=1)
        {
        // this is for col checking
        var count=0
        for(let j=0;j<3;j+=1)
        {
            if (table[i][j]==turn)
            count+=1
        }
        if (count==3){
            boxes.forEach((box,index)=>{
                row=Math.floor(index/3)
                if (row==i){
                    box.style.backgroundColor='green'
                }
            })
            return true
        }
        count=0
        // this os for col checking
        for(let j=0;j<3;j+=1){
            if (table[j][i]==turn){
                count+=1
            }
        }
        if (count==3){
            boxes.forEach((box,index)=>{
                col=index%3
                if (col==i){
                    box.style.backgroundColor='green'
                }
            })
            return true
        }
    }
    // this is for diagonal
    count=0
    for (let i=0;i<3;i+=1)
        if (table[i][i]==turn){
            count+=1
        }
    if (count==3){
        boxes.forEach((box, index) => {
            const row = Math.floor(index / 3); 
            const col = index % 3;
        
            if (row === col) {
                box.style.backgroundColor = 'green';
            }
        });
        return true
    }
    count=0
    for(let i=0;i<3;i++){
        if(table[i][3-i-1]==turn){
            count+=1
        }
    }
    if (count==3){
        boxes.forEach((box, index) => {
            const row = Math.floor(index / 3); 
            const col = index % 3;
            if ((row == 0 && col == 2) || (row == 1 && col == 1) || (row == 2 && col == 0)) {
                box.style.backgroundColor = 'green';
            }
        });
        return true
    }
    return false
}

function checkTie(){
    let count=0
    for(let i=0;i<3;i++){
        for(let j=0;j<3;j++){
            if (table[i][j]!=''){
                count+=1
            }
        }
    }
    if (count==9){
        return true
    }
    return false
}
boxes.forEach((box,index)=>{
    box.addEventListener('click',()=>{
        if (box.innerText !== '') return;
        if (gameOver) return;
        box.innerText=turn
        const row = Math.floor(index / 3);
        const col = index % 3;
        table[row][col] = turn;
        if(checkWinner()){
            player.innerHTML=`player ${turn} is winner`
          
            restart.innerHTML='Restart Game'
            gameOver=true
            return
        }
        if (checkTie()){
            player.innerHTML='Game is Tie'
            restart.innerHTML='Restart Game'
            return
        }

        if (turn=='X'){
            turn='O'
        }
        else{
            turn="X"
        }
        player.innerHTML=`player ${turn}`
        console.log(table)
    })
})

restart.addEventListener('click',()=>{
    begin()
})