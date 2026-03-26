import logo from './logo.svg';
import './App.css';

import ItemDate from './components/Date';
import Name from './components/Name';

function App() {
  const response = [
    {
      itemName:"Nirma",
      itemDate: "20",
      itemMonth: "June",
      itemyear:"1998"
    },
    {
      itemName:"Nirma2",
      itemDate: "202",
      itemMonth: "June2",
      itemyear:"19982"
    },
    {
      itemName:"Nirma3",
      itemDate: "203",
      itemMonth: "June3",
      itemyear:"19983"
    }
  ];
  return (
    <div className="App">
        {  response.map((item,index)=>(
            <div key={index}>
                <Name name={item.itemName}>{index==0 && "Hello Jee Main hu aapki first Item"}</Name>
                <ItemDate date={item.itemDate} month={item.itemMonth} year={item.itemyear} ></ItemDate>
            </div>

        ))}
      <h1>Hello Ji this is react</h1>
    </div>
  )};

export default App;
