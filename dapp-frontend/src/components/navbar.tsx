import React, { useState } from 'react';
import Asset from './Asset';
import Requests from './requests';
import Revoke from './revoke';

function NavBar() {
    const [activeLink, setActiveLink] = useState<string>('home');

    const handleNavLinkClick = (link: string) => {
      setActiveLink(link);
    };
  return (
    <div className="container">
    <nav className="navbar navbar-expand-lg bg-body-tertiary">
      <div className="container-fluid">
        <a className="navbar-brand" href="#">
          Navbar
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className={`nav-item ${activeLink === 'home' ? 'active' : ''}`}>
              <a
                className="nav-link"
                href="#"
                onClick={() => handleNavLinkClick('home')}
              >
                Home
              </a>
            </li>
            <li className={`nav-item ${activeLink === 'features' ? 'active' : ''}`}>
              <a
                className="nav-link"
                href="#"
                onClick={() => handleNavLinkClick('features')}
              >
                Features
              </a>
            </li>
            <li className={`nav-item ${activeLink === 'pricing' ? 'active' : ''}`}>
              <a
                className="nav-link"
                href="#"
                onClick={() => handleNavLinkClick('pricing')}
              >
                Pricing
              </a>
            </li>
          </ul>
        </div>
      </div>
      </nav>
      
      <div className="row justify-content-center">
        <div className="col-md-8">
          {activeLink === 'home' && <Asset />}
          {activeLink === 'features' && <Requests />}
          {activeLink === 'pricing' && <Revoke />}
        </div>
      </div>
    </div>
    
    
  );
}

export default NavBar;
