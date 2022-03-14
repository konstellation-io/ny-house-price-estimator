import React from "react";
import "./MapWrapper.scss";
import { Map, Marker, TileLayer, ZoomControl } from "react-leaflet";
import { LatLngTuple } from "leaflet";
import L from "leaflet";
import icon from "leaflet/dist/images/marker-icon.png";
import iconShadow from "leaflet/dist/images/marker-shadow.png";

import "leaflet/dist/leaflet.css";

let DefaultIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow,
  iconAnchor: [14, 34],
});

L.Marker.prototype.options.icon = DefaultIcon;

function MapWrapper({
  latitude,
  longitude,
  draggable,
  setMarkerPosition,
}: any) {
  const defaultLatLng: LatLngTuple = [latitude, longitude];

  const handleMarkerPosition = (event: any) => {
    const { lat: latitude, lng: longitude } = event.target._latlng;
    setMarkerPosition({ latitude, longitude });
  };

  return (
    <Map id="mapId" center={defaultLatLng} zoom={13} zoomControl={false}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
      />
      <ZoomControl position="topright" />
      <Marker
        customIcon={DefaultIcon}
        iconAnchor={[30, 37]}
        position={defaultLatLng}
        draggable={draggable}
        onDragend={handleMarkerPosition}
      />
    </Map>
  );
}

export default MapWrapper;
