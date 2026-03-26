import logo from './logo.svg';
import './App.css';

import Date from './components/Date';
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
      <Name name={response[0].itemName}> Hello Jee Main hu aapki first Item</Name>
      <Date date={response[0].itemDate} month={response[0].itemMonth } year={response[0].itemyear}/>
      <Name name={response[1].itemName}/>
      <Date date={response[1].itemDate} month={response[1].itemMonth } year={response[1].itemyear}/> 
       <Name name={response[2].itemName}/>
      <Date date={response[2].itemDate} month={response[2].itemMonth } year={response[2].itemyear}/>
      <h1>Hello Ji this is react</h1>
    </div>
  );
}

export default App;
