import logo from './logo.svg';
import './App.css';
import ItemName from './components/ItemName';
import ItemDate from './components/ItemDate';
import { useState } from 'react';

function App() {
  const products = [
    {
      id: 'p1',
      title: 'Nirma',
      amount: 100,
      date: new Date(2021, 8, 10),
    },
    { 
      id: 'p2', 
      title: 'Sirf Excel', 
      amount: 200, 
      date: new Date(2021, 2, 2) },
    {
      id: 'p3',
      title: 'Tide',
      amount: 130,
      date: new Date(2021, 11, 28),
    },
    {
      id: 'p4',
      title: 'Maggi',
      amount: 450,
      date: new Date(2021, 5, 5),
    },
  ];
  const [productsList,setProducts]=useState(products)
  const [title, setTitle] = useState("");
  const [date, setDate] = useState("");
  const addProduct = () => {
    if (!title || !date) return;
    const newProduct = {
      id: Math.random().toString(),
      title: title,
      date: new Date(date),
    };
  
    setProducts(prev => [...prev, newProduct]);
  
    // reset inputs
    setTitle("");
    setDate("");
  };
  const clickHandler = (id) => {
    setProducts(prevProducts =>
      prevProducts.map(product =>
        product.id === id
          ? { ...product, title: "Popcorn" }
          : product
      )
    );
  };
  return (
    <div className="App">
      <div className="bg-white p-4 rounded-md flex flex-col gap-3 w-[300px]">
      
      <input
        type="text"
        placeholder="Enter title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="border p-2 rounded"
      />

      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
        className="border p-2 rounded"
      />

      <button
        onClick={addProduct}
        className="bg-black text-white p-2 rounded"
      >
        Add Product
      </button>

    </div>
      <div className='flex justify-center items-center  h-screen w-screen'>
        <div className='flex flex-col justify-around items-center w-[500px] h-[500px] bg-amber-300 rounded-md'>
          {productsList.map((product) => (
            <div key={product.id} className='flex justify-around items-center w-full'>
              <div className="bg-black text-white" > 
              <ItemDate date={product.date} />
              </div>
              <div className='flex justify-around gap-5'>
              <ItemName name={product.title} />
              <button onClick={() => clickHandler(product.id)} className='bg-white m-1 p-2 rounded-md border-2 border-black'>Add to Card</button>
              </div>
            </div>
          ))}
        </div>
    </div>

      </div>
  
  );
}

export default App;
