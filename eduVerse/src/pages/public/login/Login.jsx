/* eslint-disable no-unused-vars */
import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { FaEye, FaEyeSlash } from 'react-icons/fa';

const Login = () => {
    const navigate = useNavigate();
    const [showPassword, setShowPassword] = useState(false);

    const togglePasswordVisibility = () => {
        setShowPassword(!showPassword);
    };

    return (
        <div>
            <main>
                <section className="p-0 d-flex align-items-center position-relative overflow-hidden">
                    <div className="container-fluid">
                        <div className="row">
                            {/* left */}
                            <div className="col-12 col-lg-6 d-md-flex align-items-center justify-content-center bg-primary bg-opacity-10 vh-lg-100">
                                <div className="p-3 p-lg-5">
                                    {/* Title */}
                                    <div className="text-center">
                                        <h2 className="fw-bold">Welcome to our largest community</h2>
                                        <p className="mb-0 h6 fw-light">Let's learn something new today!</p>
                                    </div>
                                    {/* SVG Image */}
                                    <img src=".../../src/assets/images/element/02.svg" className="mt-5" alt="" />
                                    {/* Info */}
                                    <div className="d-sm-flex mt-5 align-items-center justify-content-center">
                                        {/* Avatar group */}
                                        <ul className="avatar-group mb-2 mb-sm-0">
                                            <li className="avatar avatar-sm">
                                                <img className="avatar-img rounded-circle" src=".../../src/assets/images/avatar/01.jpg" alt="avatar" />
                                            </li>
                                            <li className="avatar avatar-sm">
                                                <img className="avatar-img rounded-circle" src=".../../src/assets/images/avatar/02.jpg" alt="avatar" />
                                            </li>
                                            <li className="avatar avatar-sm">
                                                <img className="avatar-img rounded-circle" src=".../../src/assets/images/avatar/03.jpg" alt="avatar" />
                                            </li>
                                            <li className="avatar avatar-sm">
                                                <img className="avatar-img rounded-circle" src=".../../src/assets/images/avatar/04.jpg" alt="avatar" />
                                            </li>
                                        </ul>
                                        {/* Content */}
                                        <p className="mb-0 h6 fw-light ms-0 ms-sm-3">4k+ Students joined us, now it's your turn.</p>
                                    </div>
                                </div>
                            </div>
                            {/* Right */}
                            <div className="col-12 col-lg-6 m-auto">
                                <div className="row my-5">
                                    <div className="col-sm-10 col-xl-8 m-auto">
                                        {/* Title */}
                                        <span className="mb-0 fs-1">👋</span>
                                        <h1 className="fs-2">Login into Eduport!</h1>
                                        <p className="lead mb-4">Nice to see you! Please log in with your account.</p>
                                        {/* Form START */}
                                        <form>
                                            {/* Email */}
                                            <div className="mb-4">
                                                <label htmlFor="exampleInputEmail1" className="form-label">Email address *</label>
                                                <div className="input-group input-group-lg">
                                                    <span className="input-group-text bg-light rounded-start border-0 text-secondary px-3"><i className="bi bi-envelope-fill" /></span>
                                                    <input type="email" className="form-control border-0 bg-light rounded-end ps-1" placeholder="E-mail" id="exampleInputEmail1" />
                                                </div>
                                            </div>
                                            {/* Password */}
                                            <div className="mb-4">
                                                <label htmlFor="inputPassword5" className="form-label">Password *</label>
                                                <div className="input-group input-group-lg">
                                                    <span className="input-group-text bg-light rounded-start border-0 text-secondary px-3"><i className="fas fa-lock" /></span>
                                                    <input type="password" className="form-control border-0 bg-light rounded-end ps-1" placeholder="password" id="inputPassword5" />
                                                </div>
                                                <div id="passwordHelpBlock" className="form-text">
                                                    Your password must be 8 characters at least
                                                </div>
                                            </div>
                                            {/* Check box */}
                                            <div className="mb-4 d-flex justify-content-between mb-4">
                                                <div className="form-check">
                                                    <input type="checkbox" className="form-check-input" id="exampleCheck1" />
                                                    <label className="form-check-label" htmlFor="exampleCheck1">Remember me</label>
                                                </div>
                                                <div className="text-primary-hover">
                                                    <Link to="/forgot-password" className="text-secondary">
                                                        <u>Forgot password?</u>
                                                    </Link>
                                                </div>
                                            </div>
                                            {/* Button */}
                                            <div className="align-items-center mt-0">
                                                <div className="d-grid">
                                                    <button className="btn btn-primary mb-0" type="button">Login</button>
                                                </div>
                                            </div>
                                        </form>
                                        {/* Form END */}
                                        {/* Social buttons and divider */}
                                        <div className="row">
                                            {/* Divider with text */}
                                            <div className="position-relative my-4">
                                                <hr />
                                                <p className="small position-absolute top-50 start-50 translate-middle bg-body px-5">Or</p>
                                            </div>
                                            {/* Social btn */}
                                            <div className="col-xxl-6 d-grid">
                                                <a href="#" className="btn bg-google mb-2 mb-xxl-0"><i className="fab fa-fw fa-google text-white me-2" />Login with Google</a>
                                            </div>
                                            {/* Social btn */}
                                            <div className="col-xxl-6 d-grid">
                                                <a href="#" className="btn bg-facebook mb-0"><i className="fab fa-fw fa-facebook-f me-2" />Login with Facebook</a>
                                            </div>
                                        </div>
                                        {/* Sign up link */}
                                        <div className="mt-4 text-center">
                                            <span>Don't have an account? <Link to="/registration">
                                                Sign up here
                                            </Link></span>
                                        </div>
                                    </div>
                                </div> {/* Row END */}
                            </div>
                        </div> {/* Row END */}
                    </div>
                </section>
            </main>

        </div>
    );
}

export default Login;
