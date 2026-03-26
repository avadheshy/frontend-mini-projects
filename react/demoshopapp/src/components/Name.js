 function Name( {name,children}){

    return (
        <div>
            <h1 className="bg-green-900 text-white m-4 p-4 rounded-lg shadow-md">
                {name}
            </h1>
                {children}
        </div>
    )
 }

 export default Name