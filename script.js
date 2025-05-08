const form = document.getElementById('uploadForm');
const responseMessage = document.getElementById('responseMessage');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const file = formData.get('document');

  if (!file) {
    responseMessage.innerHTML = 'No document selected.';
    return;
  }

  console.log('Submitting file:', file.name); // Debug log

  try {
    const response = await fetch('http://localhost:5000/api/verify', { // ✅ Fixed endpoint
      method: 'POST',
      body: formData
    });

    const result = await response.json();

    if (response.ok) {
      responseMessage.innerHTML = `
        <h3>Document Verified Successfully!</h3>
        <p><strong>Extracted Text:</strong></p>
        <pre>${result.extracted_text}</pre>
      `;
    } else {
      responseMessage.innerHTML = `
        <h3>Error: ${result.message}</h3>
      `;
    }
  } catch (error) {
    responseMessage.innerHTML = `An error occurred: ${error.message}`;
  }
});
