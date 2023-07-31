import React, { useState, useEffect } from "react";
import { AiOutlineEyeInvisible, AiOutlineEye } from "react-icons/ai";
import { BiArrowBack } from "react-icons/bi";
import { Link, useNavigate } from "react-router-dom";
const initialState = { email: "", password: "" };

function Login() {
  const [state, setState] = useState(initialState);
  const [isPasswordShow, setIsPasswordShow] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleChange = (e) => {
    setState({ ...state, [e.target.name]: e.target.value });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(state);

    const { email, password } = state;

    console.log(state);
  };

  return (
    <div className="mvh-100 loginPage d-flex justify-content-center align-items-center">
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
            <div className="card  w-100">
              <div className="div card-body">
                <h3 style={{ color: "#F54748" }}>LOGIN</h3>
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
                      aria-label="Email"
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
                      name="password"
                      placeholder="Password"
                      aria-label="Password"
                      aria-describedby="addon-wrapping"
                      required
                      onChange={handleChange}
                      style={{ backgroundColor: "#FDECEC" }}
                    />
                    <button
                      type="button"
                      className="input-group-text"
                      id="addon-wrapping"
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
                  <div className="mb-3 mt-1 m form-check">
                    <input
                      type="checkbox"
                      className="form-check-input"
                      id="exampleCheck1"
                    />
                    <label className="form-check-label" for="exampleCheck1">
                      Remember me
                    </label>
                  </div>
                  <div className="text-center">
                    <button
                      type="submit"
                      disabled={isLoading}
                      className="btn  loginButton"
                    >
                      {!isLoading ? (
                        "Login"
                      ) : (
                        <div className="spinner-border spinner-border-sm"></div>
                      )}
                    </button>
                  </div>
                </form>
                <div style={{ position: "relative" }} className="pt-2">
                  <span className="OR text-center">
                    <i className="fa-solid fa-o"></i>
                    <i className="fa-solid fa-r"></i>
                  </span>
                  <hr />
                </div>
                <div className="text-center">
                  Need an account?{" "}
                  <span>
                    <Link to="/signUp" style={{ color: "#F54748" }}>
                      SIGNUP
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

export default Login;
