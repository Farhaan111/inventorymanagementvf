import { Link } from "react-router-dom";
import "./SignIn.css";

function SignIn() {
  return (
    <div className="sign-in-page">
      <div className="register-section">
        <h2 className="register-heading">Sign-In</h2>
        <form className="register-form">
          <input type="text" placeholder="username" required />
          <input type="password" placeholder="password" required />
          <div className="button-si-container">
            <button className="sign-up-button-si" type="submit">
              Sign-In
            </button>
            <Link to="/signin" className="sign-in-button-su">
              Sign-Up
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default SignIn;
