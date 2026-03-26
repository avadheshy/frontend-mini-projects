
import { FcLike,FcLikePlaceholder } from "react-icons/fc";


function Card(props){
    const card=props.card
    const [like,setLike]=
    return(
        <div className="w-[300px] h-[450px] bg-neutral-900 text-white rounded-sm">
            <div className="relative">
               <img src={card.image?.url} className="bg-cover"/>
               <FcLike className="absolute"/>
            </div>


            <div>
                <h2>{card.title}</h2>
                <p>{card.description}</p>
            </div>
        </div>
    )

}

export default Card