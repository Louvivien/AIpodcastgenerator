import React from "react";
import person from "../../Assets/person.png";
import orderProcess from "../../Assets/OrderProcess.png";
function HeroSection() {
  return (
    <>
      <div
        id="heroSection"
        className="container-fluid"
        style={{ marginTop: "-15px" }}
      >
        <div className="row">
          <div className="col-6 ">
            <div className="row">
              <div className="col-1 "></div>
              <div className="col-11">
                <div className="mt-4">
                  <span
                    style={{
                      color: "#F54748",
                      fontFamily: "Poppins, sans-serif",
                      fontWeight: 500,
                      fontSize: "16px",
                      lineHeight: "24px",
                      backgroundColor: "#FDECEC",
                      borderRadius: "30px",
                      padding: "11px",
                    }}
                  >
                    Faster and Better
                  </span>
                </div>
                <div className="mt-3">
                  <b>Dialauge </b> <br />
                  <b>Podcasts </b> <br />
                  <div>
                    <b>Generated </b>{" "}
                    <span id="ai" style={{ color: "#F54748" }}>
                      {" "}
                      by AI{" "}
                    </span>
                  </div>
                </div>
                <p>
                  Generate Conventional podcasts using your favourite medium
                  articles or simply by giving a topic.
                </p>
                <a
                  className="btn btn-lg py-3 px-5"
                  style={{ backgroundColor: "#F54748", color: "4D4D4D" }}
                >
                  Try Now
                </a>
                <a className="pt-2">
                  <img
                    src={orderProcess}
                    style={{ cursor: "pointer", marginBottom: "-40px" }}
                  />
                </a>
              </div>
            </div>
          </div>
          <div className="col-6">
            <img
              src={person}
              alt=""
              style={{ width: "100%" }}
              className="pb-2"
            />
          </div>
        </div>
      </div>
    </>
  );
}

export default HeroSection;
