import styled from "styled-components";

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3rem;
  padding: 1rem;
`;

export const HomeLogo = styled.img`
  width: 60rem;
  max-width: 100%;
  object-fit: contain;
`;

export const SearchArea = styled.div`
  display: flex;
  gap: 1rem;
  justify-content: center;
  width: 100%;
  flex-wrap: wrap;
`;

export const ResultGrid = styled.div`
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
  width: 100%;
  max-width: 600px;
  padding: 1rem 0;

  @media (max-width: 768px) {
    grid-template-columns: repeat(2, 1fr);
  }

  @media (max-width: 480px) {
    grid-template-columns: 1fr;
  }
`;

export const PaginationWrapper = styled.div`
  margin-bottom: 5rem;
`;

export const LoadingOverlay = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
  position: fixed;
  top: 0;
  left: 0;
  backdrop-filter: blur(15px);
`;
