
import { useState } from "react";
function Card(props){
    const { id, name, info, image, price, removePlaceFromList } = props;
    const [read, setRead] = useState(true);
  
    return (
      <div className="w-[300px] bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition duration-300">
        
        <img 
          src={image} 
          className="w-full h-[200px] object-cover"
        />
  
        <div className="p-4">
          
          <p className="text-green-600 font-bold text-lg">₹ {price}</p>
          <h1 className="font-bold text-xl mt-1">{name}</h1>
  
          <p className="text-gray-600 text-sm mt-2">
            {read ? info.substring(0, 100) + "..." : info}
  
            <span 
              onClick={() => setRead(!read)} 
              className="text-blue-500 cursor-pointer ml-2 font-semibold"
            >
              {read ? "Read More" : "Show Less"}
            </span>
          </p>
  
          <button 
            className="mt-4 w-full border-2 border-red-500 text-red-500 py-2 rounded-md hover:bg-red-500 hover:text-white transition"
            onClick={() => removePlaceFromList(id)}
          >
            Not Interested
          </button>
  
        </div>
      </div>
    );
  }

export default Card