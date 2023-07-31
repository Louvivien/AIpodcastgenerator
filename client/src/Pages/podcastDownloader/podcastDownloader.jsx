import React from "react";
import axios from "axios";
function PodcastDownloader() {
  const handleDownload = () => {
    const audioUrl = "download_audio";
    // const audioUrl = process.env.REACT_APP_BASE_URL + 'download_audio';

    axios({
      url: audioUrl,
      method: "GET",
      responseType: "blob", // Set the response type to 'blob' to handle binary data (audio file)
    })
      .then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "podcast_audio.mp3"); // Set the desired file name and extension
        document.body.appendChild(link);
        link.click();
      })
      .catch((error) => {
        console.error("Error downloading podcast audio:", error);
      });
  };
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
                onClick={handleDownload}
              >
                Download
              </a>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default PodcastDownloader;
