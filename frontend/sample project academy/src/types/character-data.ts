import { UserProps } from './user-data';

export interface Character {
    id: number;
    name: string;
    status: string;
    species: string;
    type: string;
    gender: string;
    image: string;
    originIds?: number[];
    locationIds?: number[];
}

