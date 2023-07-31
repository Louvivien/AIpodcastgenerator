import React from "react";
function PodcastDownloader() {
  const podcastDownloadHanler = () => {};
  return (
    <>
      <div id="podcastDownloader" className="container pb-5 mb-5">
        <div className="row">
          <div className="col">
            <h1 style={{ color: "#F54748" }}>It’s Here!</h1>
            <p>Your Podcast is ready. Download now.</p>
            <div>
              {" "}
              <a
                className="btn btn-lg py-3 px-5"
                style={{ backgroundColor: "#F54748", color: "white" }}
                onClick={podcastDownloadHanler}
              >
                Downloader
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default PodcastDownloader;
