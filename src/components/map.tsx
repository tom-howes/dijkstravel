import { MapContainer, TileLayer, Marker, Popup, useMap, GeoJSON } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import cities from '../assets/cities.json';
import City from './city'
import cityIcon from './cityIcon';
import '../assets/images/chicago.png';

const startPos: [number, number] = [39.833, -98.583];

const bigCities = cities.filter(city => Number(city['population']) > 1000000);

let finalCities: City[];

finalCities = bigCities.map(x => new City(x['city'], Number(x['latitude']), Number(x['longitude']), `../assets/images/${x['city']}.png`))


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
                        <Marker position={city.coordinates} key={city.name} icon={cityIcon(city)}>
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