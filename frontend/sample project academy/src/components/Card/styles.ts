import styled from "styled-components";

export const Image = styled.img`
  width: 100%;
  height: 100%;
  object-fit: cover;

  filter: grayscale(100%);
  transition: 0.3s ease;
`;

export const StyleCard = styled.div`
  width: 18rem;
  border-radius: 1rem;
  overflow: hidden;

  border: 2px solid transparent;
  transition: 0.3s ease;
  background: #111;

  display: flex;
  flex-direction: column;
  cursor: pointer; 

  
  &:hover {
    border-color: #b9ff3b; 
    box-shadow: 0 0 12px rgba(185, 255, 59, 0.7);

    ${Image} {
      filter: grayscale(0%);
    }
  }
`;

export const ImageWrapper = styled.div`
  width: 100%;
  aspect-ratio: 1 / 1;
  overflow: hidden;
`;

export const Info = styled.div`
  background: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.75),
    rgba(0, 0, 0, 0.95)
  );
  padding: 1rem 1.2rem;
`;

export const Name = styled.h3`
  font-size: 1.5rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0;
`;

export const Species = styled.span`
  font-size: 1.3rem;
  color: #d0d0d0;
`;
