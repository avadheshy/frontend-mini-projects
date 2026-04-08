import { useNavigate } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";


function Header(){
    const navigate = useNavigate()
    const totalItems = useSelector(state =>
        state.cart.items.reduce((acc, item) => acc + item.quantity, 0)
      );
    return(
        <div className="flex justify-around h-10 bg-slate-900 items-center text-white w-full">
            <div>
            <p>ECOMZY</p>
            </div>
            <div className="flex justify-around gap-8">
                <p onClick={()=>(navigate('/'))}>Home</p>
                <p onClick={()=>(navigate('/cart'))}>Cart <span>{totalItems}</span></p>
            </div>
        </div>
    )
}

export default Header