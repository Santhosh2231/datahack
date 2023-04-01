import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
// import logo from "../assets/logo.jpg"

function Navbar() {
  const [navOpen, setNavOpen] = useState(false)
  const [isOpen,setIsOpen] = useState(false);

  useEffect(() => {
    const toggleButton = document.querySelector('.toggle-button')
    toggleButton.addEventListener('click', () => {
      setNavOpen(!navOpen)
    })
  }, [navOpen])

  function toggleDropdown(event){
    setIsOpen(!event.target.value);

  }

  return (
    <nav className=" flex items-center bg-transparent bg-slate-700 p-4">
      
      <div className="flex items-center flex-shrink-0 text-white mr-6">
      {/* <img
            src={}
            data-aos="slide-up"
            alt="..."
            className="object-cover h-96 w-80 rounded-full"
          /> */}
        <span className="font-semibold text-xl tracking-tight text-white space-x-10 md:pl-24 "><h6 className='text-white text-2xl'>AOTT Foods</h6></span>

      </div>
      <div className="block lg:hidden">
        <button className="flex items-center px-3 py-2 border rounded text-teal-200 border-teal-400 hover:text-white hover:border-white toggle-button">
          <svg className="fill-current h-3 w-3" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z"/></svg>
        </button>
      </div>
      <div className={`w-full block flex-grow justify-end lg:flex lg:items-center lg:w-auto ${navOpen ? 'block' : 'hidden'}`}>
        <div className="text-sm sm:flex lg:flex-grow justify-end md:pr-48 md:space-x-5">
          <Link to="/" className="block mt-4 lg:inline-block lg:mt-0  hover:text-white mr-4">
            <h6 className='text-white font-Merriweather md:text-2xl'>Home</h6>
          </Link>
          <Link to="/menuitems" className="block mt-4 lg:inline-block lg:mt-0  hover:text-white mr-4">
            <h6 className='text-white font-Merriweather md:text-2xl'>Menu Items</h6>
          </Link>
          <Link to="/offers" className="block mt-4 lg:inline-block lg:mt-0  hover:text-white mr-4">
            <h6 className='text-white  font-Merriweather md:text-2xl'>Recommendations</h6>
          </Link>
          
          <Link to="/clients" className="block mt-4 lg:inline-block lg:mt-0  hover:text-white">
            <h6 className='text-white font-Merriweather md:text-2xl'>Clients</h6>
          </Link>
        </div>
      </div>
    </nav>
    
  )
}
export default Navbar