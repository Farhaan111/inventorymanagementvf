import "./SignIn.css";

function SignInPage() {
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
            <a href="/signin" className="sign-in-button-su">
              Sign-In
            </a>
          </div>
        </form>
      </div>
    </div>
  );
}

export default SignInPage;
