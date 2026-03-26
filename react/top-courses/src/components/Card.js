import { FcLike, FcLikePlaceholder } from "react-icons/fc";
import { toast } from "react-toastify";
import { useState } from "react";

function Card(props){
  const card = props.card;
  const [liked, setLiked] = useState(false);

  function clickHandler() {
    if (liked) {
      setLiked(false);
      toast.error("Like removed ❌");
    } else {
      setLiked(true);
      toast.success("Liked ❤️");
    }
  }

  return(
    <div className="w-[300px] h-[450px] bg-neutral-900 text-white rounded-md overflow-hidden shadow-md">
    <div className="relative">
    
    <img 
        src={card.image?.url} 
        className="w-full h-[200px] object-cover"
    />

    <div 
        className="absolute top-2 right-2 bg-white rounded-full p-1 shadow-md cursor-pointer text-xl"
        onClick={clickHandler}
    >
        {liked ? <FcLike /> : <FcLikePlaceholder />}
    </div>

    </div>

      <div className="p-3">
        <h2 className="font-bold text-lg">{card.title}</h2>
        <p className="text-sm text-gray-300 mt-2">
          {card.description}
        </p>
      </div>

    </div>
  );
}

export default Card;