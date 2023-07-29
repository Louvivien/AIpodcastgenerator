import React from "react";

export default function NoPage() {
  return (
    <div className="py-5">
      <div className="container">
        <div className="row">
          <div className="col text-center text-danger mt-5">
            <h1 className="text-center mt-5">ERROR 404!</h1>
            <h2 className="text-center mb-0">Page Not Found</h2>
          </div>
        </div>
      </div>
    </div>
  );
}
