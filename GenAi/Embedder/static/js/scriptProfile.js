document.getElementById('profileButton').addEventListener('click', function() {
    fetch('/profile/1')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                document.getElementById('name').innerText = data.name;
                document.getElementById('email').innerText = data.email;
                document.getElementById('password').innerText = data.password;
                document.getElementById('s_class').innerText = data.s_class;
                document.getElementById('address').innerText = data.address;
                document.getElementById('mobile').innerText = data.mobile;
                document.getElementById('pin').innerText = data.pin;
                document.getElementById('profileDetails').classList.remove('hidden');
            }
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('studyMaterial').addEventListener('click', function() {
    alert('Study Material clicked');
});

document.getElementById('practiceSet').addEventListener('click', function() {
    alert('Practice Set clicked');
});

document.getElementById('collegeExam').addEventListener('click', function() {
    alert('College Exam clicked');
});
