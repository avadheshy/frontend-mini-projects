 function Name( props){
    const name =props.name
    return (
        <div>
            <h1 className="bg-green-900 m-[25px] p-[10px]">
                {name}
            </h1>
                {props.children}
        </div>
    )
 }

 export default Name