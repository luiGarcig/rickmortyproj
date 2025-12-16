import React from "react";
import { StyledButton } from "./styles"; 

interface ButtonProps {
  title: string;
  onClick?: () => void;
}

export const Button: React.FC<ButtonProps> = ({ title, onClick }) => {
  return (
    <StyledButton onClick={onClick}>
      {title}
    </StyledButton>
  );
};
