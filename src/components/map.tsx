import { MapContainer, TileLayer, Marker, Popup, useMap, GeoJSON } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import cities from '../assets/cities.json';

const startPos: [number, number] = [39.833, -98.583];

const bigCities = cities.filter(city => Number(city['population']) > 500000);

class City {
    name: string;
    coordinates: [number, number];

    constructor(name: string, lat: number, long: number) {
        this.name = name;
        this.coordinates = [lat, long];
    }
}



let finalCities: City[];

finalCities = bigCities.map(x => new City(x['city'], Number(x['latitude']), Number(x['longitude'])))

function Map() {
    return (
        <>
            < MapContainer center={startPos} zoom={4} scrollWheelZoom={false} >
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                {
                    finalCities.map((city) => (
                        <Marker position={city.coordinates} key={city.name}>
                            <Popup>
                                {city.name}
                            </Popup>
                        </Marker>
                    )
                    )
                }
            </MapContainer >
        </>
    )
}

export default Map;