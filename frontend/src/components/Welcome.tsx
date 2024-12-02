import { Link } from "react-router-dom";
import "./Welcome.css";

function WelcomePage() {
  return (
    <div className="welcome-page">
      <img
        src="/images/inventorybg.png"
        alt="Inventory Background"
        className="bg-image"
      />
      <div className="welcome">
        <h1 className="welcome-text">WELCOME</h1>
        <p>to a better inventory experience</p>
      </div>
      <div className="button-container">
        <Link to="/signin" className="sign-up-button">
          Sign-Up
        </Link>
        <Link to="/signup" className="sign-in-button">
          Sign-In
        </Link>
      </div>
    </div>
  );
}

export default WelcomePage;
