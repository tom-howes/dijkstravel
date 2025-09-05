import React from 'react';
import { Marker } from 'react-leaflet';
import './map'
import L from 'leaflet';
import City from './city';
import chicago from '../assets/images/chicago.png';

const cityIcon = (city: City) => {
    return L.icon({
        iconUrl: city.image,
        iconSize: [30, 30],
        iconAnchor: [30 / 2, 30 / 2]
    })
}

export default cityIcon;
