import React, { useState, useEffect } from "react";
import { Button } from "../../components/Button";
import { SearchInput } from "../../components/SearchInput";
import { Card } from "../../components/Card";
import { CharacterModal } from "../../components/CharacterModal";
import { Pagination } from "../../components/Pagination";
import { LoadingCard } from "../../components/LoadingCard";
import Logo from "../../assets/logo.png";
import { CharacterService } from "../../services/character-service";
import { 
  Container, 
  HomeLogo, 
  SearchArea, 
  ResultGrid, 
  PaginationWrapper, 
  LoadingOverlay 
} from "./styles";

type CharacterSummary = {
  id: number;
  image: string;
  name: string;
  species: string;
};

type CharacterDetail = {
  id: number;
  name: string;
  status: string;
  species: string;
  gender: string;
  type?: string;
  last_episode?: string;
  image: string;
  origin: {
    name: string;
    dimension: string;
    residents_count: number;
  };
  location: {
    name: string;
    dimension: string;
    residents_count: number;
  };
};

export const Home: React.FC = () => {
  const [selected, setSelected] = useState<CharacterDetail | null>(null);
  const [totalPages, setTotalPages] = useState(1);
  const [page, setPage] = useState(1);
  const [characters, setCharacters] = useState<CharacterSummary[]>([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [loading, setLoading] = useState(false);

  const service = new CharacterService();

  const fetchData = async () => {
    try {
      setLoading(true);

      await new Promise((resolve) => setTimeout(resolve, 2000));

      const data: any = await service.get_all_characters(searchTerm, page);

      setTotalPages(data.data.total_pages);
      setCharacters(data.data.items);
    } catch (error) {
      console.error("Erro ao carregar lista:", error);
      setCharacters([]);
    } finally {
      setLoading(false);
    }
  };

  const handleCharacterClick = async (id: number) => {
    try {
      const response: any = await service.get_character_by_id(id);
      console.log("Detalhes recebidos:", response);

      if (response.success && response.data) {
        setSelected(response.data);
      }
    } catch (error) {
      console.error("Erro ao buscar detalhes:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, [page]);

  const handleSearch = () => {
    if (page === 1) fetchData();
    else setPage(1);
  };

  return (
    <>
      <Container>
        <HomeLogo src={Logo} alt="Rick and Morty" />
        
        <SearchArea>
          <SearchInput
            placeholder="Search characters"
            value={searchTerm}
            onChange={(e: any) => setSearchTerm(e.target.value)}
          />
          <Button title="Search" onClick={handleSearch} />
        </SearchArea>

        {loading ? (
          <LoadingOverlay>
            <LoadingCard />
          </LoadingOverlay>
        ) : (
          <>
            <ResultGrid>
              {characters.map((char) => (
                <Card
                  key={char.id}
                  imageUrl={char.image}
                  name={char.name}
                  species={char.species}
                  onClick={() => handleCharacterClick(char.id)}
                />
              ))}
            </ResultGrid>
            
            <PaginationWrapper>
              <Pagination
                currentPage={page}
                totalPages={totalPages}
                onPageChange={setPage}
              />
            </PaginationWrapper>
          </>
        )}
      </Container>

      {selected && (
        <CharacterModal
          onClose={() => setSelected(null)}
          data={{
            image: selected.image,
            name: selected.name,
            species: selected.species,
            status: selected.status,
            gender: selected.gender,
            type: selected.type || "Unknown",
            last_episode: selected.last_episode || "Unknown",
            originName: selected.origin?.name || "Unknown",
            originDimension: selected.origin?.dimension || "Unknown",
            originResidents: selected.origin?.residents_count || 0,
            locationName: selected.location?.name || "Unknown",
            locationDimension: selected.location?.dimension || "Unknown",
            locationResidents: selected.location?.residents_count || 0,
          }}
        />
      )}
    </>
  );
};;
