import React from "react";
import { Container, PageButton, ArrowButton } from "./styles";

interface PaginationProps {
  currentPage: number;
  totalPages: number;
  onPageChange: (page: number) => void;
}

export const Pagination: React.FC<PaginationProps> = ({ 
  currentPage, 
  totalPages, 
  onPageChange 
}) => {

    const getPageRange = () => {
    const maxButtons = 5;
    
    let start = Math.max(1, currentPage - 2);
    let end = Math.min(totalPages, start + maxButtons - 1);

    if (end - start + 1 < maxButtons) {
      start = Math.max(1, end - maxButtons + 1);
    }

 
    const range = [];
    for (let i = start; i <= end; i++) {
      range.push(i);
    }
    
    return range;
  };

  const pages = getPageRange();

  return (
    <Container>
      
      <ArrowButton 
        onClick={() => onPageChange(currentPage - 1)}
        disabled={currentPage === 1}
      >
        &lt;
      </ArrowButton>

      {pages.map((page) => (
        <PageButton
          key={page}
          onClick={() => onPageChange(page)}
          $active={page === currentPage} 
        >
          {page}
        </PageButton>
      ))}

      <ArrowButton 
        onClick={() => onPageChange(currentPage + 1)}
        disabled={currentPage === totalPages}
      >
        &gt;
      </ArrowButton>

    </Container>
  );
};
