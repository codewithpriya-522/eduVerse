import {
    Route,
    Routes,
} from "react-router-dom";

import Login from "../../pages/public/login/Login";
import LandingPage from "../../pages/public/landingPage/LandingPage";
import Registration from "../../pages/public/registration/Registration";

export const PublicRouting = () => {
    return (
        <div className="h-screen w-full">
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/login" element={<Login />} />
                <Route path="/registration" element={<Registration />} />
            </Routes>
        </div>
    );
};
