import { Character } from "@/types/character-data";

export class CharacterService{
	private baseUrl: string

	constructor(){
		this.baseUrl = 'http://127.0.0.1:5000/character'
	}


	async get_all_characters(name: string, page: number): Promise<Character[]>
	{
		const params = new URLSearchParams({
			name: name,
			page: page.toString()
		});
		const fetchUrl = `${this.baseUrl}/getAllCharacters?${params.toString()}`;

		try{
			const response = await fetch(fetchUrl, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if(!response.ok)
			{
				throw new Error(`Erro na requisição: ${response.status}`);
			}

			const data = await response.json();
			return data;
		} catch (error)
		{
			console.log(`falha ao buscar personagem:`, error);
			throw error
		}
	}
	
	async get_character_by_id(id: number): Promise<Character>
	{
		const fetchUrl = `${this.baseUrl}/getCharacter/${id}`;

		try
		{
			const response = await fetch(fetchUrl, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json'
				}
			});

			if(!response.ok)
			{
				throw new Error(`Erro na requisição: ${response.status}`);
			}

			const data = await response.json();
			return data;

		} 
		catch (error)
		{
			console.log(`falha ao buscar personagem:`, error);
			throw error
		}

		

	}


}
