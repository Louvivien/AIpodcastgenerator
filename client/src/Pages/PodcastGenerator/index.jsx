import React from "react";
import Header from "../../Components/Header";
import PodcastGenerator from "./podcastGenerator";
import plane from "../../Assets/plane2.png";
import arrow from "../../Assets/arrow.png";
import cartoon from "../../Assets/cartoon.png";
function index() {
  return (
    <div className="container-fluid">
      <Header />
      <img src={plane} alt="plane" className="plane2" />
      <img src={arrow} alt="arrow" className="arrow" />
      <img src={cartoon} alt="cartoon" className="cartoon" />
      <main>
        <PodcastGenerator />
      </main>
    </div>
  );
}

export default index;
