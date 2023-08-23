import React from "react";
import Research from "../Components/Research";
import Footer from "../Components/Footer";
import NavBar from "../Components/NavBar";

const Home = () => {

    return{
        renderHome:(
            <div>
                <NavBar></NavBar>
                <Research></Research>
                <Footer></Footer>
            </div>
        )
    } 
}
export default Home