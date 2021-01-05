import React from "react";
import { Counter } from "./components/counter/Counter";
import YabrApp from "./components/YabrApp/YabrApp";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Counter />
        <p>
          Edit <code>src/App.js</code> and save to reload.
          whats up
        </p>
      </header>
    </div>
  );
}

export default App;
