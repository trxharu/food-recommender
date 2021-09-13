import React from 'react';
import axios from 'axios';

interface AppProps {
  aprop?: string
}

export class App extends React.Component<AppProps> {

  recommendImage(file: FileList | null): void {
    if (file) {
      const formData = new FormData();
      formData.append("image", file[0]);

      axios({
        method: 'post',
        url: 'http://localhost:8000/api/recommender',
        responseType: 'json',
        data: formData
      }).then((res) => {
        console.log(res.data);
      }).catch(err => {
        console.log(err);
      });
    }
  }

  onFileUpload = (): void => {
    const fileElem = document.getElementById("imageFile")! as HTMLInputElement;

    if (fileElem) {
      fileElem.click();

      // Attatching onChange event listener to the hidden input element
      fileElem.addEventListener('change', () => {
        this.recommendImage(fileElem.files);
      });
    }
  }

  render() {
    return (
      <div className="container">
        <div className="content">
          <h1>Food Recommender App</h1>
          <input id="imageFile" type="file" capture accept="image/*" style={{ display: "none" }} />
          <button onClick={this.onFileUpload}>Capture an Image <br /> or <br /> Select an Image File</button>
          <p>*It requires camera access permissions.</p>
        </div>
      </div>
    );
  }
}
