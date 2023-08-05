import React from "react";
import lock from "../../Assets/lock.png";
import hand from "../../Assets/hand.png";
import subtract1 from "../../Assets/subtract1.png";
import subtract2 from "../../Assets/subtract2.png";
import car from "../../Assets/car.png";
function MidSection() {
  return (
    <>
      <div id="midSection" className="container-fluid pb-5 mb-5">
        <div className="row headings">
          <div className="col mt-5 pt-5">
            <p>How it works</p>
            <h1>One Click Conversation</h1>
            <h1>Podcasts</h1>
          </div>
        </div>
        <div className="container">
          <div className="row">
            <div className="col-lg-4 col-md-4 col-sm-12 mb-5  ">
              <div class="card card1">
                <div className="mt-4">
                  <img src={lock} class="card-img-top lock" alt="lock" />
                  <img src={hand} class="card-img-top hand" alt="hand" />
                </div>
                <div class="card-body">
                  <h1>Upload URL</h1>
                  <p>
                    Don't have your script? no worries. Give us a news article
                    URL or simply a topic name
                  </p>
                </div>
              </div>
            </div>
            <div className="col-lg-4 col-md-4 col-sm-12 mb-5 ">
              <div class="card card2">
                <div className="mt-4">
                  <img
                    src={subtract2}
                    class="card-img-top subtract2"
                    alt="subtract2"
                  />
                  <img
                    src={subtract1}
                    class="card-img-top subtract1"
                    alt="subtract1"
                  />
                </div>
                <div class="card-body">
                  <h1>Add Speakers</h1>
                  <p>
                    Add details about the Speakers, their gender and personality
                  </p>
                </div>
              </div>
            </div>
            <div className="col-lg-4 col-md-4 col-sm-12 mb-5 ">
              <div class="card card3">
                <div className="mt-4">
                  <img src={car} class="card-img-top car" alt="car" />
                </div>
                <div class="card-body">
                  <div class="card-body">
                    <h1>Download</h1>
                    <p>Generate your podcast and download it</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default MidSection;
