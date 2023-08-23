import React, { useState } from 'react';
import axios from 'axios';
import "../Styles/Research.css"

// Define the size of the image we want to manipulate
const SIZE = 3 * 1024 * 1024; 

const Research = () => {

  const [selectedImage, setSelectedImage] = useState(null);
  const [detectionResult, setDetectionResult] = useState(null);
  const [error, setError] = useState(null);

  const handleImageUpload = async () => {
    const file = selectedImage;

    const formData = new FormData();
    formData.append('image', file);

    try {
      // We send the request to the server
      const response = await axios.post(`http://localhost:5000/api/detect`, formData);
      setDetectionResult(response.data);
      setError(null);
    } catch (error) {
      console.error(error);
      setError('Error met when uploading the image');
    }
  };

  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (!file) {
      setError('Choose an image');
      return;
    }

    // We check if the image is not too big
    if (file.size > SIZE) {
      setError('Your file is too big, please choose one under ' + (SIZE/(1024 * 1024)).toString() + 'mb');
      return;
    }

    // Different image types accepted by our server
    const allowedTypes = ['image/png', 'image/tif'];
    if (!allowedTypes.includes(file.type)) {
      setError('Invalid file, you must use a .tif or .png');
      return;
    }

    setSelectedImage(file);
    setError('')
  };

  const removeImage = () => {
    setSelectedImage('');
    setDetectionResult('');
    setError('');
  };

  
  return (
    <div className='DivResearch'>
      <h1 className='Title'>Text detector</h1>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      {error && <p>{error}</p>}
      {selectedImage && (
        <>
          <button onClick={handleImageUpload}>Upload image</button>
          <button onClick={removeImage}>Delete image</button>
        </>
      )}
      {detectionResult && (
        <div>
          <h2>Text Detected (output.txt available on the app code):</h2>
          <p>{detectionResult}</p>
        </div>
      )}
    </div>
  );
};

export default Research;