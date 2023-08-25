import React from "react";
import axios from "axios";
import "../Styles/NavBar.css"


const NavBar = () => {

    const sendRequest = async () => {
        // Test function to see if the server is answering
        try {
          const response = await axios.get(`http://localhost:5000/test`);
          console.log(response)
        } catch (error) {
          console.log(error)
        }
      };

    return (
        <div className="DivNavBar">
            <p>Optical Character Recognition</p>
            <button onClick={sendRequest}>Test</button>
        </div>
    )

}
export default NavBar