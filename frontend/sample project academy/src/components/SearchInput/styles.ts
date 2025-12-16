import styled from "styled-components";

export const Input = styled.input`
  padding: 1rem 1.6rem;
  font-size: 1.6rem;

  background: rgba(0, 0, 0, 0.4);
  color: #fff;

  border: 2px solid rgba(255, 255, 255, 0.5);
  border-radius: 1rem;

  backdrop-filter: blur(4px); 
  outline: none;
  transition: border-color 0.2s ease, background 0.2s ease;

  &::placeholder {
    color: rgba(255, 255, 255, 0.7);
  }

  &:focus {
    border-color: #b9ff3b;
    background: rgba(0, 0, 0, 0.6);
  }
`;
