import {
  BrowserRouter,
  Route,
  Routes,
} from "react-router-dom";
import LandingPage from "../pages/public/landingPage/LandingPage";

export const BaseRouting = () => {



  return (
    <div className="h-screen w-full">
      <BrowserRouter>
        <Routes>
          <Route>
            <Route path="/*" element={<LandingPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
};
