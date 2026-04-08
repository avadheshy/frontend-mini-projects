import logo from './logo.svg';
import './App.css';
import { Routes,Route } from 'react-router-dom';
import CartPage from './page/CartPage';
import HomePage from './page/HomePage';
import Header from './components/Header';

function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path='/' element={<HomePage/>}/>
        <Route path='/cart' element={<CartPage/>}/>
        <Route/>
      </Routes>

    </div>
  );
}

export default App;
