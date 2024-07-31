document.getElementById('subjectButton').addEventListener('click', function() {
    document.getElementById('subjectList').classList.toggle('hidden');
});

document.querySelectorAll('.subject').forEach(function(button) {
    button.addEventListener('click', function() {
        const subject = this.getAttribute('data-subject');
        fetch(`/select_folder?subject=${subject}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    window.location.href = '/folder_uploaded'
                }
            });
    });
});
