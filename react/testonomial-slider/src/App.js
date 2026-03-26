import logo from './logo.svg';
import './App.css';
import Card  from './components/card';
import { useState } from 'react';

function App() {
  const reviews = [
    {
      id: 1,
      name: "Pranay Gupta",
      job: "Software Engineer",
      image: "https://aeccc.targettechnology.in/static/media/PranayGupta.f3c530b7630ba8efb2ab.jpg",
      text: "I have had the pleasure of working with this team on several projects, and I am consistently impressed with their technical expertise and ability to deliver quality solutions on time and within budget. They are a true partner and an asset to any project.",
    },
    {
      id: 2,
      name: "Abir Pal",
      job: "Graphic Designer",
      image: "https://aeccc.targettechnology.in/static/media/AbirPal.574a09ad7cb325853b29.jpg",
      text: "I have been working with this company for several years now, and I have always been impressed with their creativity and attention to detail. They are true professionals who take pride in their work and always go above and beyond to deliver exceptional results.",
    },
    {
      id: 3,
      name: "Soumya Banerjee",
      job: "Marketing Manager",
      image: "https://aeccc.targettechnology.in/static/media/SoumyaBanerjee.2e2521d6029842435080.jpg",
      text: "I am thrilled with the results of our recent marketing campaign, and it wouldn't have been possible without the hard work and dedication of the entire team. Thank you for your exceptional work!",
    },
    {
      id: 4,
      name: "Saikat Mukherjee",
      job: "Content Strategist",
      image: "https://aeccc.targettechnology.in/static/media/SaikatMukherjee.033310703edff52d0532.jpg",
      text: "I have worked with many content creators over the years, but none have impressed me as much as this team. They have a knack for crafting compelling and engaging content that resonates with our audience and drives real results. I highly recommend them!",
    },
    {
      id: 5,
      name: "Aritra Biswas",
      job: "Data Analyst",
      image: "https://avatars.githubusercontent.com/u/93366359?v=4",
      text: "I had the opportunity to work with this team on a data analysis project, and I was impressed with their attention to detail and their ability to work with complex datasets. They provided valuable insights that helped us make informed business decisions. It was a pleasure working with them.",
    },
  ];
  const [index,setIndex]=useState(0)
  function randomIndex(){
    let indx= Math.floor(Math.random()*reviews.length)
    setIndex(indx)
  }
  function increment() {
    setIndex((prev) => 
      prev === reviews.length - 1 ? 0 : prev + 1
    );
  }
  
  function decrement() {
    setIndex((prev) => 
      prev === 0 ? reviews.length - 1 : prev - 1
    );
  }
  
  return (
    <div className="App">
      <div className="flex justify-center items-center min-h-screen">
      <div className="w-[600px] h-[500px] gap-10 border-2 rounded-md">
        <h1 className='text-black font-bold text-3xl'>Our Testonomial</h1>
        <div>
              <Card key={reviews[index].id} name={reviews[index].name} job={reviews[index].job} image={reviews[index].image} text={reviews[index].text } />
        </div>
        <div className='flex justify-center items-center gap-10'>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6" onClick={decrement}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M15.75 19.5 8.25 12l7.5-7.5" />
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-6" onClick={increment}>
         <path stroke-linecap="round" stroke-linejoin="round" d="m8.25 4.5 7.5 7.5-7.5 7.5" />
        </svg>

        </div>
 

        <button className='bg-blue-500 p-4 rounded-md' onClick={randomIndex}>Surprise Me</button>
      </div>
      </div>
   
 
    </div>
  );
}

export default App;
