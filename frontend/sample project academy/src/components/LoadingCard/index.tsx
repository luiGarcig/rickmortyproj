import React from "react";

import { Container, LoadingImage, InfoWrapper, LoadingText } from "./styles";
import LoadingImg from "../../assets/loading.jpg"; 

export const LoadingCard: React.FC = () => {
  return (
    <Container>
      <LoadingImage 
        src={LoadingImg} 
        alt="Loading..." 
      />
      
      <InfoWrapper>
        <LoadingText>Loading</LoadingText>
      </InfoWrapper>
    </Container>
  );
};;
