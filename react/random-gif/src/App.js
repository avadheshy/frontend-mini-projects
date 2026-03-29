import Random from "./components/Random"
import Tag from "./components/Tag";

export default function App() {
  return (

    <div className="w-full h-screen flex flex-col background relative overflow-x-hidden items-center bg-[radial-gradient(#ffffff_2.5px,transparent_2.5px),radial-gradient(#ffffff_2.5px,transparent_2.5px)] 
            bg-[length:36px_36px] 
            bg-[position:0_0,18px_18px] 
            bg-[#b1d2ff]">
      <h1 className=" bg-white m-10 p-2 text-3xl font-bold w-11/12 rounded-md text-center">
      RANDOM GIFS</h1>
      <div className="flex flex-col h-full justify-evenly   w-6/12 items-center gap-10">
        <Random />
        <Tag />
      </div>
    </div>

  );
}