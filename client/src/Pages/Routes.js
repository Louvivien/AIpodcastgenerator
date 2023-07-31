import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./LandingPage/index";
import Login from "./Authentication/Login";
import SignUp from "./Authentication/SignUp";
import PodcastDownloader from "./podcastDownloader/index";
import PodcastGenerator from "./PodcastGenerator/index";
import NoPage from "./NoPage";

function CustomRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/podcastGenerator" element={<PodcastGenerator />} />
        <Route path="/podcastDownloader" element={<PodcastDownloader />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signUp" element={<SignUp />} />
        <Route path="*" element={<NoPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default CustomRoutes;
