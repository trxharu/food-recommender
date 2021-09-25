import React from 'react';
import axios from 'axios';
import { MapDetail } from './MapDetail';

import spinner from "../assets/spinner.gif";
import oops from "../assets/oops.png";

export class App extends React.Component {

  state = {
    location: { lat: 0, lng: 0 },
    data: [],
    predictions: { dish: "", accuracy: 0 },
    isLoading: false,
    isError: false,
    errorMsg: ""
  }

  homeDiv = React.createRef<HTMLDivElement>();

  recommendImage(file: FileList | null): void {
    if (file) {
      const formData = new FormData();
      formData.append("image", file[0]);
      formData.append("location", JSON.stringify(this.state.location));

      // Setting loading image and fetching results
      this.setState({ isLoading: true });
      axios({
        method: 'post',
        url: '/api/recommender',
        responseType: 'json',
        data: formData
      }).then((res) => {
        if (res.data.status === "OK") {
          if (this.homeDiv.current) {
            this.homeDiv.current.style.display = "none";
          }
          this.setState({ isLoading: false, data: res.data.data, predictions: res.data.predictions });
        } else {
          this.setState({ isLoading: false, isError: true, errorMsg: res.data.msg, predictions: res.data.predictions });
        }

      }).catch(err => {
        console.log(err);
      });
    }
  }

  onFileUpload = (): void => {
    const fileElem = document.getElementById("imageFile") as HTMLInputElement;
    this.setState({ isLoading: false, isError: false });
    // New Delhi coords { lat: 28.607921091007487, lng: 77.20631201188128 }
    // Checking for location access and getting location
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        this.setState({
          location: { lat: position.coords.latitude, lng: position.coords.longitude }
        });
      }, () => {
        alert("Error getting location.");
      });
    } else {
      alert("GeoLocation is not supported.");
    }

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
          <div ref={this.homeDiv}>
            <h2>Indian Food Recommender App</h2>
            <input id="imageFile" type="file" accept="image/*" style={{ display: "none" }} />
            <button onClick={this.onFileUpload}>Capture an Image <br /> or <br /> Select an Image File</button> <br />
            {this.state.isError && <div className="error">{`${this.state.predictions.dish} (${Math.ceil(this.state.predictions.accuracy)}% accuracy)`}</div>}
            {this.state.isLoading && <div className="spinner">Getting Results... this may take a while <img src={spinner} alt="Loading ..." /></div>}
            {this.state.isError && <div className="error">{this.state.errorMsg}<img src={oops} alt="Something went wrong" /></div>}
            <p>*It requires camera and location permissions.</p>
          </div>
          {this.state.data.length !== 0 &&
            <MapDetail data={this.state.data}
              locations={this.state.location}
              msg={`${this.state.predictions.dish} (with ${Math.ceil(this.state.predictions.accuracy)}% accuracy)`} />
          }
        </div>
      </div>
    );
  }
}
