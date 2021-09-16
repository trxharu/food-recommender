import React from 'react';
import { LngLatLike, Map, Marker, Popup } from 'mapbox-gl';

// Definition for a Feature object that represent things on Map
interface Feature {
  type: string;
  id: number;
  geometry: { type: string; coordinates: number[] };
  properties: { amenity: string; cuisine: string; name: string }
}

// Definition for Props that this component will receive
interface MapProps {
  data: Feature[];
  msg: string;
}

export class MapDetail extends React.Component<MapProps> {
  // getting reference for map container
  mapContainer = React.createRef<HTMLDivElement>();

  componentDidMount() {
    // Creating a new map instance
    const map = new Map({
      accessToken: process.env.REACT_APP_MAPBOX_KEY,
      container: this.mapContainer.current as HTMLElement,
      style: 'mapbox://styles/mapbox/streets-v11',
      center: this.props.data[0].geometry.coordinates as LngLatLike,
      zoom: 12
    });

    // Adding Markers to map
    this.props.data.forEach(feature => {
      if (feature.properties.name) {
        new Marker()
          .setLngLat(feature.geometry.coordinates as LngLatLike)
          .setPopup(new Popup()
            .setHTML(`<h1>${feature.properties.name}</h1><p>${feature.properties.cuisine}</p>`))
          .addTo(map);
      }
    });
  }

  render() {
    return (
      <div>
        <h2>Results for {this.props.msg}.</h2>
        <div className="mapbox-container" ref={this.mapContainer}></div>
      </div>
    );
  }
}