import React from "react";
import {
  Overlay,
  ModalWrapper, 
  ContentCard,  
  CloseButton,
  CharacterImage,
  CardInfo,
  Name,
  Species,
  RightSection,
  Section,
  SectionTitle,
  DescriptionText,
  Label,
  Value,
  SubValue,
  Residents,
  LeftCard,
  LeftSection
} from "./styles";
import { buildCharacterDescription } from "../../utils/aboutContent";

interface CharacterModalProps {
  onClose: () => void;
  data: any; 
}

export const CharacterModal: React.FC<CharacterModalProps> = ({ onClose, data }) => {
  
  const description = buildCharacterDescription({
    name: data.name,
    species: data.species,
    status: data.status,
    gender: data.gender,
    type: data.type,
    last_episode: data.last_episode
  });

  return (
    <Overlay>
     <ModalWrapper>

       <LeftCard>
          <CharacterImage src={data.image} alt={data.name} />
          <CardInfo>
            <Name>{data.name}</Name>
            <Species>{data.species}</Species>
          </CardInfo>
        </LeftCard>

        <ContentCard>

          <LeftSection>
            <CloseButton onClick={onClose}>Close</CloseButton>
          </LeftSection>
        
          <RightSection>
            <Section>
              <SectionTitle>ABOUT</SectionTitle>
              <DescriptionText>{description}</DescriptionText>
            </Section>

            <Section>
              <SectionTitle>ORIGIN</SectionTitle>
              <Label>Planet</Label>
              <Value>{data.originName}</Value>
              <SubValue>{data.originDimension}</SubValue>
              <Residents>{data.originResidents} residents</Residents>
            </Section>

            <Section>
              <SectionTitle>LOCATION</SectionTitle>
              <Label>Planet</Label>
              <Value>{data.locationName}</Value>
              <SubValue>{data.locationDimension}</SubValue>
              <Residents>{data.locationResidents} residents</Residents>
            </Section>
          </RightSection>
          
        </ContentCard>
      </ModalWrapper>
    </Overlay>
  );
};
