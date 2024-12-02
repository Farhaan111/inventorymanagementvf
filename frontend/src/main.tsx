import ReactDOM from "react-dom/client"; // for React 18
import App from "./App";
import { BrowserRouter } from "react-router-dom"; // Import BrowserRouter
import "./main.css";

// Creating the root element for React 18
const root = ReactDOM.createRoot(document.getElementById("root")!);

root.render(
  <BrowserRouter>
    {" "}
    {/* Wrap the App in BrowserRouter */}
    <App />
  </BrowserRouter>
);
