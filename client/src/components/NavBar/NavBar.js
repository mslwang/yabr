import React from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faBell, faCog, faUserCircle } from '@fortawesome/free-solid-svg-icons'
import "./NavBar.css";

const NavBar = () => {
    return (
        <nav class="navbar">
            <h1 class="logo">yabr</h1>
            <ul class="main-nav" id="js-menu">
                <li>
                    <FontAwesomeIcon icon={faBell} color="grey" />
                </li>
                <li>
                    <FontAwesomeIcon icon={faCog} color="grey" />
                </li>
                <li>
                    <FontAwesomeIcon icon={faUserCircle} color="grey" />
                </li>
            </ul>
        </nav>
    );
};

export default NavBar;
