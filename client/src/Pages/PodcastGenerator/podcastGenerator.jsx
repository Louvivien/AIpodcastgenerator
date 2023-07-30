import React from "react";
import mic from "../../Assets/mic.png";
function PodcastGenerator() {
  return (
    <>
      <div id="podcastGenerator" className="container">
        <div className="row">
          <div className="col-1"></div>
          <div className="col-10">
            {/* Row 1 */}
            <div className="row row1">
              <div className="col-sm-12 col-md-4 img">
                <img src={mic} alt="" />
              </div>
              <div className="col-sm-12 col-md-8 ">
                <h3>
                  Collab<span style={{ color: "#F54748" }}>Talk.ai</span>
                </h3>
                <h1>
                  <span style={{ color: "#F54748" }}>Get</span> Started
                </h1>
              </div>
            </div>
            {/* Row 2 */}
            <div className="row">
              <div className="col">
                <div class="input-group flex-nowrap">
                  <textarea
                    type="text"
                    class="form-control"
                    placeholder="Your Script"
                    aria-label="yourscript"
                    aria-describedby="addon-wrapping"
                    style={{ backgroundColor: "#FDECEC" }}
                    rows="8"
                    cols="40"
                    // value="Your Script"
                  />
                </div>
              </div>
            </div>
            {/* Row 3 */}
            <div className="row row3 my-4">
              <div className="col or">OR</div>
            </div>
            {/* Row 4 */}
            <div className="row row4 mb-5">
              <div className="col-sm-12 col-md-8 rd">
                <div className="row">
                  <div className="col-2"></div>
                  <div className="col-8 ">
                    <div class="input-group flex-nowrap my-3">
                      <input
                        type="text"
                        class="form-control"
                        placeholder="Your Link"
                        aria-label="yourlink"
                        aria-describedby="addon-wrapping"
                        style={{ backgroundColor: "#FDECEC" }}
                      />
                    </div>
                    <div className="col or">OR</div>
                    <div class="input-group flex-nowrap my-3">
                      <input
                        type="text"
                        class="form-control"
                        placeholder="Your Topic"
                        aria-label="yourtopic"
                        aria-describedby="addon-wrapping"
                        style={{ backgroundColor: "#FDECEC" }}
                      />
                    </div>
                  </div>
                  <div className="col-2"></div>
                </div>
              </div>
              <div className="col-sm-12 col-md-4 mt-sm-4 mt-md-0">
                <div className="row">
                  <div className="col-2"></div>
                  <div className="col-8">
                    <div class="mb-3">
                      <label for="minutes" class="form-label">
                        Length of your podcast
                      </label>
                      <input
                        type="email"
                        class="form-control"
                        id="minutes"
                        placeholder="minutes"
                        style={{ backgroundColor: "#FDECEC" }}
                      />
                    </div>
                  </div>
                  <div className="col-2"></div>
                </div>
              </div>
            </div>
            {/* Row 5 */}
            <div className="row my-5 py-4">
              <div className="col">
                <div className="row">
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="speaker1" class="form-label">
                            Speaker 1
                          </label>
                          <input
                            type="email"
                            class="form-control"
                            id="speaker1"
                            placeholder="Name"
                            style={{ backgroundColor: "#FDECEC" }}
                          />
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="speaker2" class="form-label">
                            Speaker 2
                          </label>
                          <input
                            type="email"
                            class="form-control"
                            id="speaker2"
                            placeholder="Name"
                            style={{ backgroundColor: "#FDECEC" }}
                          />
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="speaker3" class="form-label">
                            Speaker 3 (Optional)
                          </label>
                          <input
                            type="email"
                            class="form-control"
                            id="speaker3"
                            placeholder="Name"
                            style={{ backgroundColor: "#FDECEC" }}
                          />
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="gender1" class="form-label">
                            Gender (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="gender1"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              male
                            </option>
                            <option value="2">female</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="gender2" class="form-label">
                            Gender (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="gender2"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              male
                            </option>
                            <option value="2">female</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="gender3" class="form-label">
                            Gender (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="gender3"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              male
                            </option>
                            <option value="2">female</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="age1" class="form-label">
                            Age (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="age1"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              young
                            </option>
                            <option value="2">old</option>
                            <option value="3">middle aged</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="age2" class="form-label">
                            Age (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="age2"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              young
                            </option>
                            <option value="2">old</option>
                            <option value="3">middle aged</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="age3" class="form-label">
                            Age (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="age3"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              young
                            </option>
                            <option value="2">old</option>
                            <option value="3">middle aged</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="accent1" class="form-label">
                            Accent (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="accent1"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              american
                            </option>
                            <option value="2">british</option>
                            <option value="3">australian</option>
                            <option value="4">indian</option>
                            <option value="5">african</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="accent2" class="form-label">
                            Accent (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="accent2"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              american
                            </option>
                            <option value="2">british</option>
                            <option value="3">australian</option>
                            <option value="4">indian</option>
                            <option value="5">african</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                  <div className="col-sm-12 col-md-4">
                    <div className="row">
                      <div className="col-2"></div>
                      <div className="col-8">
                        <div class="mb-3">
                          <label for="accent3" class="form-label">
                            Accent (Optional)
                          </label>
                          <select
                            class="form-select"
                            aria-label="Default select example"
                            id="accent3"
                            style={{ backgroundColor: "#FDECEC" }}
                          >
                            <option value="1" selected>
                              american
                            </option>
                            <option value="2">british</option>
                            <option value="3">australian</option>
                            <option value="4">indian</option>
                            <option value="5">african</option>
                          </select>
                        </div>
                      </div>
                      <div className="col-2"></div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            {/* Row 6 */}
            <div className="row row6">
              <div className="col">
                <div className="row">
                  <div className="col-3"></div>
                  <div className="col-6">
                    <p>
                      Generate Conversational podcasts using your favorite
                      medium articles or simply by giving a topic.{" "}
                    </p>
                  </div>
                  <div className="col-3"></div>
                </div>
                <div className="row my-4 pb-5">
                  <div className="col" style={{ textAlign: "center" }}>
                    <a
                      className="btn btn-lg py-3 px-5"
                      style={{ backgroundColor: "#F54748", color: "white" }}
                    >
                      Generate
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="col-1"></div>
        </div>
      </div>
    </>
  );
}

export default PodcastGenerator;
