import React from "react";
import plane from "../Assets/plane.png";
function Header2() {
  return (
    <>
      <div id="header" className="container">
        <nav class="navbar ">
          <div class="container-fluid">
            <a class="navbar-brand">
              <span>
                <img src={plane} className={{ width: "100px" }} />
              </span>
              <span style={{ marginLeft: "-52px" }}>
                <b>Collab</b>
                <b style={{ color: "#F54748" }}>Talk.ai</b>
              </span>
            </a>
            <div class="d-flex">
              <a
                className="me-3"
                style={{
                  cursor: "pointer",
                  textDecoration: "none",
                  color: "#F54748",
                  fontFamily: "Poppins, sans-serif",
                  fontWeight: 500,
                  fontSize: "16px",
                  lineHeight: "24px",
                  textAlign: "center",
                }}
              >
                Signup
              </a>
              <a
                className="me-3"
                style={{
                  cursor: "pointer",
                  textDecoration: "none",
                  color: "#4D4D4D",
                  fontFamily: "Poppins, sans-serif",
                  fontWeight: 500,
                  fontSize: "16px",
                  lineHeight: "24px",
                  textAlign: "center",
                }}
              >
                About
              </a>
              <a
                // className="me-3"
                style={{
                  cursor: "pointer",
                  textDecoration: "none",
                  color: "#4D4D4D",
                  fontFamily: "Poppins, sans-serif",
                  fontWeight: 500,
                  fontSize: "16px",
                  lineHeight: "24px",
                  textAlign: "center",
                }}
              >
                Contact
              </a>
            </div>
          </div>
        </nav>
      </div>
    </>
  );
}

export default Header2;
