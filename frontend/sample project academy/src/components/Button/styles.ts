import styled from "styled-components";

export const StyledButton = styled.button`
  padding: 1rem 2rem;
  font-size: 1.6rem;
  font-weight: 500;

  background: rgba(0, 0, 0, 0.5);
  color: #fff;

  border: 2px solid rgba(255, 255, 255, 0.7);
  border-radius: 1rem;

  cursor: pointer;
  transition: 0.2s ease;


  &:hover {
    background: rgba(255, 255, 255, 0.1);
    transform: scale(1.05);
  }
`;
