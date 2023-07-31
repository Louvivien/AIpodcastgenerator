import React, { useState } from "react";
import { AiOutlineEyeInvisible, AiOutlineEye } from "react-icons/ai";
import { BiArrowBack } from "react-icons/bi";
import { Link, useNavigate } from "react-router-dom";

const initialState = { email: "", password: "", confirmPassword: "" };
function SignUp() {
  const [state, setState] = useState(initialState);
  const [isPasswordShow, setIsPasswordShow] = useState(false);
  const [isConfirmPasswordShow, setIsConfirmPasswordShow] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    e.preventDefault();
    setState({ ...state, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsLoading(true);
    // console.log(state)

    const { email, password, confirmPassword } = state;
    console.log(state);
    setIsLoading(false);
  };

  return (
    <div className="mvh-100 SignUpPage d-flex justify-content-center align-items-center">
      <div className="container ">
        <div className="row">
          <div className="col">
            <Link className="btn btn-home" to="/" style={{ color: "#F54748" }}>
              <BiArrowBack />
            </Link>
          </div>
        </div>
        <div className="row">
          <div className="col-12 col-md-8 offset-md-2 col-lg-6 offset-lg-3">
            <div className="card SignUpCard w-100">
              <div className="div card-body">
                <h3 style={{ color: "#F54748" }}>Sign Up</h3>
                <form onSubmit={handleSubmit}>
                  <label for="exampleInputEmail1" className="form-label">
                    Email
                  </label>
                  <br />
                  <div className="input-group flex-nowrap">
                    <input
                      type="email"
                      className="form-control"
                      id="exampleInputEmail1"
                      placeholder="Email"
                      aria-label="email"
                      name="email"
                      required
                      onChange={handleChange}
                      style={{ backgroundColor: "#FDECEC" }}
                    />
                  </div>
                  <label for="password" className="form-label">
                    Password
                  </label>
                  <div className="input-group flex-nowrap">
                    <input
                      type={isPasswordShow ? "text" : "password"}
                      className="form-control"
                      id="password"
                      placeholder="Password"
                      name="password"
                      aria-label="password"
                      aria-describedby="addon-wrapping"
                      required
                      onChange={handleChange}
                      style={{ backgroundColor: "#FDECEC" }}
                    />
                    <button
                      type="button"
                      className="input-group-text"
                      onClick={() => {
                        setIsPasswordShow(!isPasswordShow);
                      }}
                    >
                      {isPasswordShow ? (
                        <AiOutlineEye />
                      ) : (
                        <AiOutlineEyeInvisible />
                      )}
                    </button>
                  </div>
                  <label for="confirmPassword" className="form-label">
                    Confirm Password
                  </label>
                  <div className="input-group flex-nowrap">
                    <input
                      type={isConfirmPasswordShow ? "text" : "password"}
                      className="form-control"
                      id="confirmPassword"
                      placeholder="Confirm Password"
                      name="confirmPassword"
                      aria-label="confirmPassword"
                      aria-describedby="addon-wrapping"
                      required
                      onChange={handleChange}
                      style={{ backgroundColor: "#FDECEC" }}
                    />
                    <button
                      type="button"
                      className="input-group-text"
                      onClick={() => {
                        setIsConfirmPasswordShow(!isConfirmPasswordShow);
                      }}
                    >
                      {isConfirmPasswordShow ? (
                        <AiOutlineEye />
                      ) : (
                        <AiOutlineEyeInvisible />
                      )}
                    </button>
                  </div>
                  <div className="text-center">
                    <button
                      type="submit"
                      disabled={isLoading}
                      className="btn signUpButton mt-2 mb-2"
                    >
                      {!isLoading ? (
                        "Sign Up"
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
                {/* //icons */}
                <div className="text-center">
                  Already a user?{" "}
                  <span>
                    <Link to="/login" style={{ color: "#F54748" }}>
                      Login
                    </Link>
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

export default SignUp;
