import React from "react";
import { StyleCard, ImageWrapper, Image, Info, Name, Species } from "./styles";

interface CardProps {
  imageUrl: string;
  name: string;
  species: string;
  onClick?: () => void;
}

export const Card: React.FC<CardProps> = ({ 
	imageUrl, 
	name, 
	species,
	onClick
}) => {
  return (
    <StyleCard onClick={onClick}>
      <ImageWrapper>
        <Image src={imageUrl} alt={name} />
      </ImageWrapper>
      <Info>
        <Name>{name}</Name>
        <Species>{species}</Species>
      </Info>
    </StyleCard>
  );
};
