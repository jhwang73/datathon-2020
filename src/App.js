import React from 'react';
import './App.css';
import BarChart from "./components/BarChart";
import DiscreteSlider from "./components/Slider";

function App() {
  return (
    <div className="App">
      <BarChart></BarChart>
      <DiscreteSlider></DiscreteSlider>
    </div>
  );
}

export default App;
