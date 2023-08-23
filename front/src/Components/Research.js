import React, { useState } from 'react';
import axios from 'axios';
import "../Styles/Research.css"

// Define the size of the image we want to manipulate
const SIZE = 3 * 1024 * 1024; 

const Research = () => {

  const [selectedImage, setSelectedImage] = useState(null);
  const [detectionResult, setDetectionResult] = useState(null);
  const [imageSent, setImageSent] = useState(null)
  const [error, setError] = useState(null);

  const handleImageUpload = async () => {
    const file = selectedImage;

    const formData = new FormData();
    formData.append('image', file);

    const serverURL = 'http://localhost:5000/image';

    try {
      // We send the request to the server
      const response = await axios.post(serverURL, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      console.log(response)
      setImageSent(1)
      setError(null);
    } catch (error) {
      console.error(error);
      setError('Error met when uploading the image');
    }
};

const getImageUpdate = async () => {

  try {
    // We send the request to the server to get image update
    const response = await axios.get(`http://localhost:5000/image`);
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
    const allowedTypes = ['image/png', 'image/tiff'];
    if (!allowedTypes.includes(file.type)) {
      setError('Invalid file, you must use a .tif or .png');
      return;
    }

    setSelectedImage(file);
    setError('')
  };

  const removeImage = () => {
    setSelectedImage(null);
    setDetectionResult(null);
    setError(null);
  };

  
  return (
    <div className='DivResearch'>
      <h1 className='Title'>Text detector</h1>
      <input type="file" accept="image/*" onChange={handleFileChange} />
      {error && <p>{error}</p>}
      {selectedImage && !imageSent && (
        <>
          <button onClick={handleImageUpload}>Upload image</button>
          <button onClick={removeImage}>Delete image</button>
        </>
      )}
      {imageSent && (
        <>
          <button onClick={getImageUpdate}>GetUpadte</button>
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