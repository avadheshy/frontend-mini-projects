


import { useDispatch, useSelector } from "react-redux";
import { addToCart, removeFromCart } from "../redux/slice/StoreSlice";

function Product({post}){

    const dispatch = useDispatch();
    const cartItems = useSelector(state => state.cart.items);

const itemInCart = cartItems.find(item => item.id === post.id);
    return(
        <div className="w-[232px] h-[343px] border-2 border-black p-[16px] rounded-xl hover:scale-[1.12] hover:shadow-xl transition-all duration-500 cursor-pointer">
            <div className="font-bold">
            <p>
                    {post.title.length <= 15
                    ? post.title
                    : post.title.slice(0, 15) + "..."}
            </p>
            </div>
            <div className="text-sm">
                {post.description.length<=50?post.description:post.description.slice(0,50) +"..."}
            </div>
            <div>
                <img className="w-[116px] h-[180px]" src={post.image}/>
            </div>
            <div className="flex justify-between">
                <div>{post.price}</div>
                <div>
                <button
                    onClick={() =>
                        itemInCart
                        ? dispatch(removeFromCart(post.id))
                        : dispatch(addToCart(post))
                    }
                    >
                    {itemInCart ? "Remove Item" : "Add to Cart"}
                </button>
                </div>
                
            </div>
        </div>
    )
}

export default Product