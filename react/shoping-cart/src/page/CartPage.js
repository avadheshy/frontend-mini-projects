import { useSelector, useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import {  removeFromCart } from "../redux/slice/StoreSlice";


function CartPage() {
  const cartItems = useSelector((state) => state.cart.items);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  // total items
  const totalItems = cartItems.reduce(
    (acc, item) => acc + item.quantity,
    0
  );

  // total price
  const totalPrice = cartItems.reduce(
    (acc, item) => acc + item.price * item.quantity,
    0
  );

  // ✅ Empty Cart UI
  if (cartItems.length === 0) {
    return (
      <div className="flex justify-center items-center gap-10  h-screen">
        <h1 className="">Your Cart is Empty</h1>
        <button
          onClick={() => navigate("/")}
          className=" border-2 p-2 border-red-500 rounded-md hover:bg-amber-100"
        >
          Shop Now
        </button>
      </div>
    );
  }

  // ✅ Cart with items
  return (
    <div className="flex justify-around items-start mt-9">

      {/* LEFT: Items */}
      <div className="flex flex-col gap-10">
        {cartItems.map((item) => (
          <div
            key={item.id}
            className="border-2 p-5 border-black"
          >
            {/* Image */}
            <img
              src={item.image}
              alt={item.title}
              className="w-[200px] h-[200px]"
            />
            <h2 className="">
            {item.title.slice(0, 40)}...
            </h2>
            <div className="flex gap-4">
                <p className="">₹ {item.price}</p>
                <p>Qty: {item.quantity}</p>

                <button onClick={() => dispatch(removeFromCart(item.id))} className="border-2 p-1 rounded border-red-800">Remove</button>
            </div>
          </div>
        ))}
      </div>

      {/* RIGHT: Summary */}
      <div className="flex flex-col gap-5">
        <h2 className="">Summary</h2>

        <p className="">Total Items: {totalItems}</p>
        <p className="">
          Total Price: ₹ {totalPrice.toFixed(2)}
        </p>

        <button className="">
          Checkout
        </button>
      </div>
    </div>
  );
}

export default CartPage;