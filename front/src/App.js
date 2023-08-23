import React from 'react';
import {Route, Routes} from 'react-router-dom'
import Home from './Pages/Home';

function App() {

  const {renderHome} = Home()

  return (
      <Routes>
          <Route exact path="*" element={renderHome}/>
      </Routes>
  );
}

export default App;
