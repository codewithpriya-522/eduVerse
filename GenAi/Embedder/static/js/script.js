document.getElementById("selectUserTypeButton").addEventListener("click", function () {
    const popup = document.getElementById("userTypePopup");
    // Toggle visibility by adding/removing the "hidden" class
    popup.classList.toggle("hidden");
    popup.style.display = popup.classList.contains("hidden") ? "none" : "block";
});

function showLoginSignup(userType) {
    const popup = document.getElementById("userTypePopup");

    // Hide the popup
    popup.classList.add("hidden");
    popup.style.display = "none";

    // Redirect to the login/signup page based on user type
    switch (userType) {
        case "student":
            window.location.href = "/student";
            break;
        case "teacher":
            window.location.href = "/teacher";
            break;
        case "admin":
            window.location.href = "/admin";
            break;
        default:
            alert("Invalid selection");
            break;
    }
}
