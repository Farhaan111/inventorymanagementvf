interface SignInProps {
  onSignIn: () => void; // Function to be called when the user signs in
}

const SignIn = ({ onSignIn }: SignInProps) => {
  const handleSignIn = () => {
    // Simulate sign-in process and call the onSignIn function
    onSignIn();
  };

  return (
    <div className="signin-page">
      <h1>Sign In</h1>
      <p>Enter your credentials to sign in.</p>
      <button onClick={handleSignIn} className="btn btn-primary">
        Sign In
      </button>
    </div>
  );
};

export default SignIn;
