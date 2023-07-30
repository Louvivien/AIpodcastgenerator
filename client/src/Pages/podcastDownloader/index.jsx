import React from "react";
import Header from "../../Components/Header";
import PodcastDownloader from "./podcastDownloader";
// import plane from "../../Assets/plane2.png";
import arrow2 from "../../Assets/arrow.png";
import cartoon2 from "../../Assets/cartoon2.png";
function index() {
  return (
    <div className="container-fluid">
      <Header />
      <img src={arrow2} alt="arrow2" className="arrow2" />
      <img src={cartoon2} alt="cartoon2" className="cartoon2" />
      <main>
        <PodcastDownloader />
      </main>
    </div>
  );
}

export default index;
