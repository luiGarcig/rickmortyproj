
import { createGlobalStyle } from "styled-components";
import bgImage from "../assets/rickMorty.jpg";

export const GlobalStyle = createGlobalStyle`
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  :root {
    font-size: 62.5%;
  }

  html, body {
    min-height: 100%;
  }

  body {
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #ffffff;

    background: #000;          
    position: relative;
    overflow-x: hidden;
  }

  body::before {
    content: "";
    position: absolute;      
    top: 0;
    left: 0;
    width: 100%;
    height: 120vh;           

    background-image: url(${bgImage});
    background-repeat: no-repeat;
    background-position: top center; 
    background-size: cover;

    filter: grayscale(100%);
    z-index: -2;
    pointer-events: none;
  }

  body::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 120vh;  
    background: rgba(0,0,0,0.85);
    z-index: -1;
    pointer-events: none;
  }

  #root {
    position: relative;
    z-index: 0;
    min-height: 100vh;
  }
`;

