interface CharacterData {
  name: string;
  species: string;
  status: string;
  gender: string;
  type?: string | null;
  last_episode?: {
    air_date: string;
  };
}

const getPronoun = (gender: string): string => {
  const g = gender.toLowerCase();
  if (g === 'male') return 'He';
  if (g === 'female') return 'She';
  return 'It';
};

export const buildCharacterDescription = (char: CharacterData): string => {
  const status = char.status.toLowerCase();
  const gender = char.gender.toLowerCase();
  const pronoun = getPronoun(char.gender);
  
  const verb = status === 'dead' ? 'was' : 'is';

  const typePart = char.type ? ` (${char.type})` : '';
  const identity = `${char.name} ${verb} a ${char.gender} ${char.species}${typePart}.`;

  let statusText = '';
  if (status === 'alive') {
    statusText = `${pronoun} is alive and well.`;
  } else if (status === 'dead') {
    statusText = `${pronoun} is dead.`;
  } else {
    statusText = `It can't be told if ${pronoun.toLowerCase()} is alive or dead.`;
  }

  const lastSeenDate = char.last_episode?.air_date || 'unknown date';
  const dateText = `Last seen in ${lastSeenDate}.`;

  return `${identity} ${statusText} ${dateText}`;
};
