import { useState,useEffect } from "react";
import axios from "axios";


import useGif from "./GetGif";




function Random(){

  
    const {image, loading, fetchGif} = useGif();
  

    if (loading) {
        return (
          <div className="flex justify-center items-center h-screen">
            <p className="text-xl font-semibold">Loading...</p>
          </div>
        );
      }


    return (
        <div className="w-full h-full bg-green-950 border-2 border-black rounded-lg gap-10 flex flex-col justify-around items-center">
            <div>A RANDOM GIF</div>
            <div><img src={image}/></div>
            <div onClick={()=>fetchGif()} className="bg-yellow-600 w-8/12 p-2 text-center rounded-md">Generate</div>
        </div>
    )
}

export default Random