import { Link, NavLink } from "react-router-dom";
import { useState } from "react";
import "./NavBar.css";

function NavBar() {
  // State to track the active link
  const [activeLink, setActiveLink] = useState<string | null>(null);

  const renderNavLink = (to: string, label: string) => (
    <li className="nav-item">
      <NavLink
        to={to}
        className={() =>
          `nav-link ${activeLink === to ? "nav-underline active" : ""}`
        }
        onClick={() => setActiveLink(to)} // Update active link on click
      >
        {label}
      </NavLink>
    </li>
  );

  return (
    <nav className="navbar d-flex justify-content-between align-items-center p-2">
      <Link to="/" className="navbar-brand">
        <img
          src="/images/trackify.png"
          alt="Trackify Logo"
          style={{ height: "40px" }}
        />
      </Link>
      <ul className="nav">
        {renderNavLink("/", "home")}
        {renderNavLink("/about", "about")}
        {renderNavLink("/contact", "contact us")}
        {renderNavLink("/pricing", "pricing")}
      </ul>
    </nav>
  );
}

export default NavBar;
