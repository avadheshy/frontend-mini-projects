import Cards from './components/Cards'
import Nav from './components/Nav'
import Header from './components/Header'
import { filterData, apiUrl } from './data';
import React, { useState, useEffect } from 'react';

function App() {
  const [dataIsLoaded, setDataIsLoaded] = useState(false)
  const [items, setItems] = useState([])
  const [category, setCategory] = useState('All')


  useEffect(() => {
    async function fetchData() { 
      try {
        let res = await fetch(apiUrl)
        let output = await res.json() 
        setItems(output.data) 
        setDataIsLoaded(true);
      }
      catch (error) {
        console.error('failed to fetch data', error)
      }
    }
    fetchData(); // You must call the function inside useEffect
  }, []);

  function LoaderHandler() {
    return (
      <div>
        <p>Please wait, data is loading...</p>
      </div>
    );
  }
  function getFilterdata(){
    if (category=='All'){
      return Object.values(items).flat()
    }
    return items[category];

  }
  return (
    <div className="bg-blue-300 w-screen min-h-screen text-center pb-10">
      <Header />
      <Nav 
        filterData={filterData} 
        category={category} 
        setCategory={setCategory} 
      />
      
      <div className="flex flex-col justify-between items-center gap-10">
      {!dataIsLoaded ? (
        <LoaderHandler /> 
      ) : (
        <Cards data={getFilterdata()} /> 
      )}
      </div>
   
    </div>
  );
}

export default App;
