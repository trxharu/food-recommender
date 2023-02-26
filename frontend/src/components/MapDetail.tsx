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
  locations: { lat: number; lng: number };
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
      center: [this.props.locations.lng, this.props.locations.lat],
      zoom: 12
    });

    new Marker({ color: "#035efc" })
      .setLngLat([this.props.locations.lng, this.props.locations.lat])
      .setPopup(new Popup()
        .setHTML(`<h1>You</h1>`))
      .addTo(map);

    // Adding Markers to map
    this.props.data.forEach(feature => {
      if (feature.properties.name) {
        new Marker({ color: "#03fc52" })
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