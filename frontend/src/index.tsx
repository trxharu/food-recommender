import React from 'react';
import ReactDOM from 'react-dom';
import { App } from "./components/App";
import "./theme.scss";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.querySelector("#root")
);