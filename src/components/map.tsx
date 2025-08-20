import { MapContainer, TileLayer, Marker, Popup, useMap, GeoJSON } from 'react-leaflet';
import L from 'leaflet';
import marker from '../assets/boston.svg';
import mapData from '../assets/countries.json'
import 'leaflet/dist/leaflet.css';
import '../components/map.css'
type json = typeof import('../assets/countries.json')
const startPos: [number, number] = [39.833, -98.583];
var CityIcon = new L.Icon({
    iconUrl: marker,
    iconRetinaUrl: marker,
    iconAnchor: [16, 22],
    iconSize: [32, 45]
}
);

let countryStyle = {
    fillColor: "blue",
    fillOpacity: 0.1
}

function Map() {
    return (
        <MapContainer style={{ height: "90vh" }} zoom={4} center={startPos}>
            <GeoJSON style={countryStyle} data={(mapData as json).features} />
        </MapContainer>
    )

}

export default Map;
// Light no writing map
//     return (<MapContainer center={position} zoom={4} scrollWheelZoom={false}>
//     <TileLayer
//         attribution='&copy; <a href="https://carto.com/">Carto</a>'
//         url="http://a.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png"
//     />
//     <Marker position={position} icon={CityIcon}>
//         <Popup>
//             This is a popup that will say the city name
//         </Popup>
//     </Marker>
// </MapContainer>