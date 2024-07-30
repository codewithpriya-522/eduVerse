// Import necessary modules
import {
  BrowserRouter,
  Route,
  Routes,
} from "react-router-dom";
import { PublicRouting } from "./public/PublicRouting";
const BaseRouting = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/*" element={<PublicRouting />} />
      </Routes>
    </BrowserRouter>
  );
};

export default BaseRouting;
