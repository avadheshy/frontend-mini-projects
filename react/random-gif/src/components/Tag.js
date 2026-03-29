import { useEffect, useState } from "react";

import useGif from "./GetGif";



function Tag(){
  
    const [tag, setTag] = useState('car');
    const {image, loading, fetchGif} = useGif(tag);


 
    if (loading) {
        return (
          <div className="flex justify-center items-center h-screen">
            <p className="text-xl font-semibold">Loading...</p>
          </div>
        );
      }
    return(
        <div className="w-full h-full bg-blue-950 border-2 border-black rounded-lg flex flex-col justify-around items-center gap-10 mb-10">
                <div>RANDOM GIF</div>
                <div><img src={image}/></div>
                <input type="text"  className="w-8/12 text-center rounded-md h-10" onChange={(event)=>{setTag(event.target.value)}}  />
                <div  onClick={()=>fetchGif(tag)} className="bg-yellow-600 w-8/12 p-2 text-center rounded-md">Generate</div>
        </div>
    )
}
export default Tag