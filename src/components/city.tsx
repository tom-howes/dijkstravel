

export default class City {
    name: string;
    coordinates: [number, number];
    image: string;

    constructor(name: string, lat: number, long: number, imgUrl: string) {
        this.name = name;
        this.coordinates = [lat, long];
        this.image = imgUrl;
    }
}