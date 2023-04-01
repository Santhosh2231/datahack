import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from './screens/Home';
import ItemRecom from './screens/ItemRecom';
import Client from './screens/Client';
import Recom from './screens/Recom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
function App() {
  return (
    <BrowserRouter>
    <div className='fixed z-10 md:w-full'>
    <Navbar />
    </div>
     <Routes>
       <Route path="/" element={<Home />} />
       <Route path="/clients" element={<Client />} />
       <Route path="/menuitems" element={<ItemRecom />} />
       <Route path="/offers" element={<Recom />} />
     </Routes>
     <Footer />
    </BrowserRouter>
  );
}

export default App;
