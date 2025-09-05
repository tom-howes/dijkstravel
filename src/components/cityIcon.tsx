import React from 'react';
import { Marker } from 'react-leaflet';
import './map'
import L from 'leaflet';
import City from './city';
import chicagoImg from '../assets/images/Chicago.png';
import nyImg from '../assets/images/new york.png';
import laImg from '../assets/images/los angeles.png';
import phillyImg from '../assets/images/philadelphia.png';
import sanAntonioImg from '../assets/images/san antonio.png';

const cityImages: { [key: string]: string } = {
    'Chicago': chicagoImg,
    'New York': nyImg,
    'Los Angeles': laImg,
    'Philadelphia': phillyImg,
    'San Antonio': sanAntonioImg
}

const cityIcon = (city: City) => {
    return L.icon({
        iconUrl: cityImages[city.name] || city.image,
        iconSize: [30, 30],
        iconAnchor: [30 / 2, 30 / 2]
    })
}

export default cityIcon;
