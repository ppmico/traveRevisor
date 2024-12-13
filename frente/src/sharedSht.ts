import { atom, map } from 'nanostores';
import { persistentAtom } from '@nanostores/persistent';

export const trkSegs = atom([]);
export const callApi = atom(false);
export const formStep = atom(0);

// el map dataSent es tipado para que funcionen las comprobaciones en ApiCall
interface DataSent {
    file: File | null;
    idMochilon: string | null;
    idRama: string | null;
    idsTiposCamino: number[];
  }
  
export const dataSent = map<DataSent>({
  file: null,
  idMochilon: null,
  idRama: null,
  idsTiposCamino: []
});

//firma: persistentAtom<string | undefined>(name: string, initial?: string | undefined)
export const apiResponse = persistentAtom<string>('apiResponse', 'JFKJDFSKJDFSKJDFSKJ');