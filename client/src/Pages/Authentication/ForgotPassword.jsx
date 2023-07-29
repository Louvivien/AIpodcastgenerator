import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useNavigate } from "react-router-dom";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleClick = (e) => {
    e.preventDefault();
    console.log(email);
  };

  return (
    <div className="mvh-100 ForgotPasswordPage d-flex justify-content-center align-items-center">
      <div className="container ">
        <div className="row">
          <div className="col">
            <Link className="btn btn-home" to="/">
              <i className="fa-solid fa-arrow-left"></i>
            </Link>
          </div>
        </div>
        <div className="row">
          <div className="col-12 col-md-8 offset-md-2 col-lg-6 offset-lg-3">
            <div className="card ForgotPasswordCard w-100">
              <div className="div card-body">
                <h3>Forgot Password</h3>
                <form>
                  <label for="exampleInputEmail1" className="form-label">
                    Email
                  </label>
                  <div className="input-group flex-nowrap">
                    <input
                      type="email"
                      className="form-control"
                      id="exampleInputEmail1"
                      placeholder="Email"
                      name="email"
                      aria-label="Email"
                      required
                      onChange={(e) => setEmail(e.target.value)}
                    />
                  </div>
                  <div className="text-center">
                    <button
                      type="submit"
                      disabled={isLoading}
                      className="btn  loginButton mt-2 mb-2"
                      onClick={handleClick}
                    >
                      {!isLoading ? (
                        "Send Email"
                      ) : (
                        <div className="spinner-border spinner-border-sm"></div>
                      )}
                    </button>
                  </div>
                </form>
                <div style={{ position: "relative" }}>
                  <span className="OR">
                    <i className="fa-solid fa-o"></i>
                    <i className="fa-solid fa-r"></i>
                  </span>
                  <hr />
                </div>
                <div className="text-center">
                  Already a user?{" "}
                  <span>
                    <Link to="/login">Login</Link>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ForgotPassword;
