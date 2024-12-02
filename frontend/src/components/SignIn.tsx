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
          <button type="submit">Sign-Up</button>
        </form>
        <a href="/signin" className="sign-in-link">
          Sign-In
        </a>
      </div>
    </div>
  );
}

export default SignInPage;
