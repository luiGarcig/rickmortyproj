import styled, { keyframes } from "styled-components";


const blink = keyframes`
  0% { opacity: 0.5; }
  50% { opacity: 1; }
  100% { opacity: 0.5; }
`;

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  max-width: 250px;
  width: 100%;
  cursor: default;
  align-items: center;
`;

export const LoadingImage = styled.img`
  width: 60%;
  height: 150px;
  object-fit: cover;
  opacity: 0.8;
  border-radius: 15px;
  border: 3px solid gray;
  box-sizing: border-box;
`;

export const InfoWrapper = styled.div`
  padding: 12px;
  display: flex;
  justify-content: center;
  width: 100%;
`;

export const LoadingText = styled.span`
  color: #fff;
  font-size: 1.2rem;
  font-weight: bold; 
  animation: ${blink} 1.5s infinite;
`;
