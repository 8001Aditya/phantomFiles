const registrationForm = document.getElementById('registrationForm');
const loginForm = document.getElementById('loginForm');
const uploadForm = document.getElementById('uploadForm');
const fileList = document.getElementById('fileList');

registrationForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(registrationForm);
  const response = await fetch('/register', {
    method: 'POST',
    body: formData
  });

  // Handle response
});

loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(loginForm);
  const response = await fetch('/login', {
    method: 'POST',
    body: formData
  });

  // Handle response
  if (response.status === 200) {
    // Show the file upload form and file list
    uploadForm.style.display = 'block';
    fileList.style.display = 'block';
  }
});

uploadForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const formData = new FormData(uploadForm);
  const response = await fetch('/upload', {
    method: 'POST',
    body: formData
  });

  // Handle response
});

fetch('/files')
  .then(response => response.json())
  .then(files => {
    files.forEach(file => {
      const downloadLink = document.createElement('a');
      downloadLink.href = `/download/${file.filename}`;
      downloadLink.innerText = file.filename;
      fileList.appendChild(downloadLink);
    });
  });
