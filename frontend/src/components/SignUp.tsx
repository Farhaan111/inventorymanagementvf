import { Link } from "react-router-dom";
import "./SignUp.css";

function SignUpPage() {
  return (
    <div className="sign-in-page">
      <div className="register-section">
        <h2 className="register-heading">Register</h2>
        <form className="register-form">
          <input type="text" placeholder="username" required />
          <input type="email" placeholder="e-mail@email.com" required />
          <input type="password" placeholder="password" required />
          <input type="password" placeholder="confirm password" required />
          <div className="button-su-container">
            <button className="sign-up-button-su" type="submit">
              Sign-Up
            </button>
            <Link to="/signup" className="sign-in-button-su">
              Sign-In
            </Link>
          </div>
        </form>
      </div>
    </div>
  );
}

export default SignUpPage;
