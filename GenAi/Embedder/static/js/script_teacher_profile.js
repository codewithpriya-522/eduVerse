document.getElementById('profileButton').addEventListener('click', function() {
    fetch('/profileTeacher/1')
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                document.getElementById('name').innerText = data.name;
                document.getElementById('email').innerText = data.email;
                document.getElementById('password').innerText = data.password;
                document.getElementById('subject').innerText = data.subject;
                document.getElementById('address').innerText = data.address;
                document.getElementById('mobile').innerText = data.mobile;
                document.getElementById('pin').innerText = data.pin;
                document.getElementById('profileDetails').classList.remove('hidden');
            }
        })
        .catch(error => console.error('Error:', error));
});

// document.getElementById('question providel').addEventListener('click', function() {
//     window.location.href = '/choose_subject';
// });

// document.getElementById('answer analysis').addEventListener('click', function() {
//     alert('answer analysis');
// });

// document.getElementById('collegeExam').addEventListener('click', function() {
//     alert('College Exam clicked');
// });
