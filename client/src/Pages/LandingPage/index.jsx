import React from "react";
import Header from "../../Components/Header";
import LandingPage from "./landingPage";
function index() {
  return (
    <div className="d-flex flex-column">
      <Header />
      <main>
        <LandingPage />
      </main>
    </div>
  );
}

export default index;
