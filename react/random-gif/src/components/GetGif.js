import { useState,useEffect } from "react";
import axios from "axios";

const API_KEY = process.env.REACT_APP_GIPHY_API_KEY;
const url = `https://api.giphy.com/v1/gifs/random?api_key=${API_KEY}`;



const useGif=(tag)=>{


    const [image, setImage] = useState(null);
    const [loading, setLoading] = useState(true);
  
    const fetchGif = async (tag) => {

        try {
          setLoading(true);
          let tes=tag?url+`&tag=${tag}`:url
          const response = await axios.get(tag?url+`&tag=${tag}`:url);
          const image_url =
          response.data.data.images.downsized_large.url;
          console.log(image_url)
    
          setImage(image_url);
        } catch (err) {
          
        } finally {
          setLoading(false);
        }
      };
    
      useEffect(() => {
        fetchGif('car');
      }, []);
      return {image,loading,fetchGif}
    }

export default useGif