import { useState } from "react";

function Count() {
    const [num, setNumber]= useState(0)

    return (
      <div className="flex flex-col w-60 h-60 bg-green-800 text-white items-center justify-center rounded-lg">
        <p className="font-bold text-lg">Counter App</p>
        <p className="text-2xl">{num}</p>
        <div className="flex gap-2 mt-3">
          <button className="bg-blue-500 px-2 py-1 rounded" onClick={()=>setNumber(prev=>prev+1)}>+</button>
          <button className="bg-gray-500 px-2 py-1 rounded" onClick={()=>setNumber(0)}>Reset</button>
          <button className="bg-red-500 px-2 py-1 rounded" onClick={()=>setNumber(prev=>prev-1)}>-</button>
        </div>
      </div>
    );
  }
  
  export default Count;