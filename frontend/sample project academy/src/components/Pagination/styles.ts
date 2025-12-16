import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px; /* Reduzi levemente o espaço entre os botões */
  margin-top: 30px;
  padding: 10px;
  background-color: transparent;
`;

interface PageButtonProps {
  $active?: boolean;
}

export const PageButton = styled.button<PageButtonProps>`
  background: none;
  border: none;
  font-family: inherit;
  font-size: 16px; /* Ajustado para ficar proporcional */
  transition: all 0.2s ease;
  min-width: 30px; /* Garante que números de 1 ou 2 dígitos tenham largura similar */
  
  cursor: ${(props) => (props.$active ? "default" : "pointer")};
  font-weight: ${(props) => (props.$active ? "bold" : "normal")};
  color: ${(props) => (props.$active ? "#eab308" : "#9ca3af")};
  
  /* Adicionei um leve scale no hover para feedback visual */
  &:hover {
    color: ${(props) => (props.$active ? "#eab308" : "#d1d5db")};
    transform: ${(props) => (props.$active ? "none" : "scale(1.1)")};
  }
`;

export const ArrowButton = styled.button`
  background: none;
  border: none;
  font-family: inherit;
  cursor: pointer;
  transition: transform 0.2s ease, color 0.2s ease;
  
  color: #ffffff;
  font-size: 20px;
  font-weight: bold;
  padding: 0 10px;

  &:hover:not(:disabled) {
    transform: scale(1.2);
    color: #eab308; /* Destaque na seta ao passar o mouse */
  }

  &:disabled {
    color: #374151;
    cursor: not-allowed;
    transform: none;
    opacity: 0.5;
  }
`;
