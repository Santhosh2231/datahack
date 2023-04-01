
import { createElement, useEffect,useState } from "react";
import Typewriter from "typewriter-effect";
import { Link } from "react-router-dom";
import hero from "../assets/hero.jpg"


const Home = () => {
  const [count, setCount] = useState(1);

  useEffect(() => {
    // document.title = `You clicked ${count} times`;

    setCount(1);
  }, [count]);

  return (
    <>
    <section id="home" className="overflow-hidden max-w-full min-h-screen bg-black"
        style={{backgroundImage:`url(${hero})`}}
    >
      <div className="pt-10 relative flex md:flex-row flex-col-reverse md:items-end justify-center items-center">

        <div className="pb-16 px-6 pt-40" data-aos="fade-down">
        <h1 className="name text-white font-bold text-5xl md:my-10">
           {"Hi there!!"}
            {/* <span className="text-dark_primary flex-wrap">{hero.LastName}</span> */}
          </h1>
          <h6 className="text-dark_primary text-5xl font-extrabold text-white font-Inria flex-wrap">{"Super Healthy Meals"}</h6>
          <br />
         

          <div className="flex flex-row flex-wrap justify-center mt-24">
          <button className='border-4 rounded-lg text-white bg-orange-600 p-2 ' ><h4 className='text-2xl font-Inria text-white'>
          <Link to="/menuitems" >Menu Items</Link>
          </h4></button>
         
          </div>
          
        </div>

      </div>
    </section>
    {/* <About /> */}
    </>
  );
};

export default Home;
