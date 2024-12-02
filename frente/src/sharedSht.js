import { atom, map } from 'nanostores';

export const trkSegs = atom([]);
export const formStep = atom(0);
export const dataSent = map({
    file: null,
    idMochilon: null,
    idRama: null,
    idsTiposCamino: []
});