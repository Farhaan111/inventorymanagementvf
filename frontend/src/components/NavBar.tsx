import { NavLink } from "react-router-dom";
import { useState } from "react";
import "./NavBar.css";

function NavBar() {
  // State to track the active link
  const [activeLink, setActiveLink] = useState<string | null>(null);

  const renderNavLink = (to: string, label: string) => (
    <li className="nav-item">
      <NavLink
        to={to}
        className={({ isActive }) =>
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
      <img
        src="/images/trackify.png"
        alt="Trackify Logo"
        className="navbar-brand"
        style={{ height: "40px" }}
      />
      <ul className="nav">
        {renderNavLink("/", "Home")}
        {renderNavLink("/about", "About")}
        {renderNavLink("/contact", "Contact Us")}
        {renderNavLink("/pricing", "Pricing")}
      </ul>
    </nav>
  );
}

export default NavBar;
